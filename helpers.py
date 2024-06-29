import glob
import cloudinary_api
import airtable_api
import threading
import time
import os


def get_model_pics(model_id):
    model_pics=sorted(glob.glob("/home/flowingbe/ComfyUI/output/temporal/model-{id}_*".format(id=model_id)))
    return model_pics

def get_pose_pics(pose_id):
    pose_pics=sorted(glob.glob("/home/flowingbe/ComfyUI/output/temporal/pose-{id}_*".format(id=pose_id)))
    return pose_pics


def delayed_delete(cloudinary_ids,model_pics):
    print("deletion process started, now sleeping 10 secs.")
    time.sleep(10)
    for pic in model_pics:
        print('rm -rf {pic}'.format(pic=pic))
        os.system('rm -rf {pic}'.format(pic=pic))

    for public_id in cloudinary_ids:
        cloudinary_api.delete_image_cloudordinary(public_id)

    print("deletion process ended")
    

def upload_model(user_id,model_id):
    #get path to model pics
    model_pics = get_model_pics(model_id)
    
    #create list of cloudinary ids & urls
    model_urls = []
    cloudinary_ids=[]

    #upload model pics to cloudinary
    for pic in model_pics:
        public_id = pic.split("_")[-1].split(".")[0]
        model_urls += [cloudinary_api.upload_cloudinary(pic, public_id)]
        cloudinary_ids += [public_id]
    
    #push model to airtable
    resp = airtable_api.push_model_to_airtable(user_id, model_urls)
    print(resp)

    deletion_thread = threading.Thread(target=delayed_delete, args=(cloudinary_ids,model_pics)).start()
    
    return f"done with uploading of model {model_id}"