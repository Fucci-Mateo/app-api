import requests
from credentials import creds

url = "https://api.airtable.com/v0/"
base_id = creds['BASE_ID']
poses_table = creds['POSES_TABLE']
models_table = creds['MODELS_TABLE']



headers = {
    "Authorization": "Bearer {}".format(creds["AIRTABLE_TOKEN"]),
    "Content-Type": "application/json"
}

def push_pose_to_airtable(pose_name ,pose_image_url, skeleton_image_url):
    url = f"https://api.airtable.com/v0/{base_id}/{poses_table}"

    data = {"records": [{"fields": {"name": pose_name, "image": [{'url':pose_image_url}], "skeleton": [{'url':skeleton_image_url}]}}]}


    response = requests.post(url, headers=headers, json=data)
    return response.json()


def get_pose_by_name(pose_name):
    url = f"https://api.airtable.com/v0/{base_id}/{poses_table}"
    params = {
        'maxRecords': '1',
        'filterByFormula': "name='{}'".format(pose_name),
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()


def push_model_to_airtable(user_id,model_images):
    url = f"https://api.airtable.com/v0/{base_id}/{models_table}"
    data = {"records": [{
        "fields": {
            "images": [{'url':model_images[0]},{'url':model_images[1]},{'url':model_images[2]},{'url':model_images[3]}], 
            "user_id": user_id
            }
        }]
    }
    print("DATA : ")
    print(data)

    response = requests.post(url, headers=headers, json=data)
    return response.json()