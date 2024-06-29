from flask import Flask, jsonify, request
import comfy_controllers
import workflows
import random
import comfy_controllers
import helpers

app = Flask(__name__)
temporal_files_path='/home/flowingbe/ComfyUI/output/temporal_files'


def parse_and_validate_post_request(request):
    data = request.get_json()  # Parse the incoming JSON data
    if not data:
        return None, {"error": "Invalid JSON"}, 400
    return data, None, None


@app.route('/gen-model', methods=['POST'])
def home():
    # Validate Post request
    data, error_response, status_code = parse_and_validate_post_request(request)
    if error_response:
        return jsonify(error_response), status_code
    
    # Add random generation id and seed
    data['gen_id']=str(random.randint(0, 10000))
    data['seed']='963922827393197'
    data['user_id']='1'
    # Format the JSON template with the values
    formatted_workflow, error = workflows.format_workflow(workflows.gen_models_workflow,data)

    # push to comfy queue
    comfy_response = comfy_controllers.push_queue(formatted_workflow)
    prompt_id=comfy_response['prompt_id']

    #check prompt status
    prompt_status = comfy_controllers.check_prompt_status(prompt_id)
    print({
        'gen_id':data['gen_id'],
        'prompt-id':prompt_id,
        'prompt_status': prompt_status})
    
    
    helpers.upload_model(data['user_id'],data['gen_id'])
    return (comfy_response)


@app.route('/home', methods=['GET'])
def hello():
    return 'hello home'






# @app.route('/api/data/<int:data_id>', methods=['GET'])
# def get_data_by_id(data_id):
#     sample_data = {"id": data_id, "name": "Jane Doe", "age": 25, "city": "Los Angeles"}
#     return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9099)