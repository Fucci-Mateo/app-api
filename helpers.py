import glob
import cloudinary_api
import airtable_api

def get_model_pics(model_id):
    model_pics=sorted(glob.glob("/home/flowingbe/ComfyUI/output/temporal/model-{id}_*".format(id=model_id)))
    return model_pics

def get_pose_pics(pose_id):
    pose_pics=sorted(glob.glob("/home/flowingbe/ComfyUI/output/temporal/pose-{id}_*".format(id=pose_id)))
    return pose_pics


def upload_model(user_id,model_id):
    model_pics = get_model_pics(model_id)
    for pic in model_pics:
        model_urls = cloudinary_api.upload_cloudinary(pic, f"model-{model_id}")
    
    return airtable_api.push_model_to_airtable(user_id, model_urls)