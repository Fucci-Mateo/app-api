import glob
import cloudinary_api
import airtable_api
import threading
import time
import os


def get_model_pics(model_id):
    model_pics=sorted(glob.glob("/home/flowingbe/ComfyUI/output/temporal/model-{id}_*".format(id=model_id)))
    return model_pics

def get_inference_result(gen_id):
    results=sorted(glob.glob("/home/flowingbe/ComfyUI/output/temporal/inference-{id}_*".format(id=gen_id)))
    return results

def get_pose_pics(pose_id):
    pose_pics=sorted(glob.glob("/home/flowingbe/ComfyUI/output/temporal/pose-{id}_*".format(id=pose_id)))
    return pose_pics

def upload_inference_results(gen_id):
    #get path to model pics
    inference_result_path = get_inference_result(gen_id)[0]
    
    result_url = cloudinary_api.upload_cloudinary(inference_result_path, f"inference-{gen_id}")
    
    return result_url


def delayed_delete(cloudinary_ids,model_pics):
    print("DELETION PROCESS STARTED. SLEEP 10.")
    time.sleep(10)
    for pic in model_pics:
        os.system('sudo rm -rf {pic}'.format(pic=pic))

    for public_id in cloudinary_ids:
        cloudinary_api.delete_image_cloudordinary(public_id)

    print("DELETION PROCESS FINISHED.")
    

def upload_model(user_id,gen_id,model_setup):
    #get path to model pics
    model_pics = get_model_pics(gen_id)
    
    #create list of cloudinary ids & urls
    model_urls = []
    cloudinary_ids=[]

    #upload model pics to cloudinary
    for pic in model_pics:
        public_id = pic.split("_")[-1].split(".")[0]
        model_urls += [cloudinary_api.upload_cloudinary(pic, public_id)]
        cloudinary_ids += [public_id]
    
    #push model to airtable
    resp = airtable_api.push_model_to_airtable(user_id, model_urls,model_setup)
    

    threading.Thread(target=delayed_delete, args=(cloudinary_ids,model_pics)).start()
    
    return resp