import json

def format_workflow(workflow_string,data):
    try:
        formatted_json = workflow_string.format(**data)
        return json.loads(formatted_json), None
    except KeyError as e:
        return None, {"error": f"Missing key in data: {str(e)}"}
    
  
# URL for face pose image
face_pose_url = 'https://res.cloudinary.com/dtsxndikq/image/upload/v1719584574/face-pose.png'

# JSON template as a string with placeholders
gen_models_workflow = '''
{{
  "3": {{
    "inputs": {{
      "seed": {seed},
      "steps": 8,
      "cfg": 1.8,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "model": [
        "10",
        0
      ],
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "latent_image": [
        "5",
        0
      ]
    }},
    "class_type": "KSampler",
    "_meta": {{
      "title": "KSampler"
    }}
  }},
  "5": {{
    "inputs": {{
      "width": 512,
      "height": 512,
      "batch_size": 1
    }},
    "class_type": "EmptyLatentImage",
    "_meta": {{
      "title": "Empty Latent Image"
    }}
  }},
  "6": {{
    "inputs": {{
      "text": "realistic photograph, closeup, beautiful {gender}, closed mouth, {origin_features} features, {hair_color} hair,symmetrical features, clear skin, wearing a tank top, light makeup, {style}, refined, {features_style} features, soft lighting, natural look, {eye_color} eyes, chiseled cheekbones, slight smile, {lips_style} lips, natural hair color, (full face:1.3), (realistic eyes:1.15)\\n\\n white background, 4k, highly detailed, high-quality, masterpiece, whi",
      "clip": [
        "10",
        1
      ]
    }},
    "class_type": "CLIPTextEncode",
    "_meta": {{
      "title": "CLIP Text Encode (Prompt)"
    }}
  }},
  "7": {{
    "inputs": {{
      "text": "low quality, bad anatomy, blurry, nsfw, not centered face",
      "clip": [
        "10",
        1
      ]
    }},
    "class_type": "CLIPTextEncode",
    "_meta": {{
      "title": "CLIP Text Encode (Prompt)"
    }}
  }},
  "8": {{
    "inputs": {{
      "samples": [
        "3",
        0
      ],
      "vae": [
        "10",
        2
      ]
    }},
    "class_type": "VAEDecode",
    "_meta": {{
      "title": "VAE Decode"
    }}
  }},
  "10": {{
    "inputs": {{
      "ckpt_name": "realvisxlV40_v40LightningBakedvae.safetensors"
    }},
    "class_type": "CheckpointLoaderSimple",
    "_meta": {{
      "title": "Load Checkpoint"
    }}
  }},
  "19": {{
    "inputs": {{
      "image": "$19-0",
      "images": [
        "8",
        0
      ]
    }},
    "class_type": "PreviewBridge",
    "_meta": {{
      "title": "Preview Bridge (Image)"
    }}
  }},
  "85": {{
    "inputs": {{
      "width": 512,
      "height": 512,
      "batch_size": 4
    }},
    "class_type": "EmptyLatentImage",
    "_meta": {{
      "title": "Empty Latent Image"
    }}
  }},
  "104": {{
    "inputs": {{
      "seed": {seed},
      "steps": 8,
      "cfg": 1.8,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "model": [
        "114",
        0
      ],
      "positive": [
        "128",
        0
      ],
      "negative": [
        "128",
        1
      ],
      "latent_image": [
        "85",
        0
      ]
    }},
    "class_type": "KSampler",
    "_meta": {{
      "title": "KSampler"
    }}
  }},
  "108": {{
    "inputs": {{
      "samples": [
        "104",
        0
      ],
      "vae": [
        "10",
        2
      ]
    }},
    "class_type": "VAEDecode",
    "_meta": {{
      "title": "VAE Decode"
    }}
  }},
  "109": {{
    "inputs": {{
      "image": "$109-0",
      "images": [
        "108",
        0
      ]
    }},
    "class_type": "PreviewBridge",
    "_meta": {{
      "title": "Preview Bridge (Image)"
    }}
  }},
  "114": {{
    "inputs": {{
      "weight": 0.5,
      "start_at": 0.5,
      "end_at": 1,
      "weight_type": "standard",
      "model": [
        "115",
        0
      ],
      "ipadapter": [
        "115",
        1
      ],
      "image": [
        "8",
        0
      ]
    }},
    "class_type": "IPAdapter",
    "_meta": {{
      "title": "IPAdapter"
    }}
  }},
  "115": {{
    "inputs": {{
      "preset": "FACEID PLUS V2",
      "lora_strength": 1,
      "provider": "CPU",
      "model": [
        "10",
        0
      ]
    }},
    "class_type": "IPAdapterUnifiedLoaderFaceID",
    "_meta": {{
      "title": "IPAdapter Unified Loader FaceID"
    }}
  }},
  "118": {{
    "inputs": {{
      "output_path": "temporal",
      "filename_prefix": "model-{gen_id}",
      "filename_delimiter": "_",
      "filename_number_padding": 1,
      "filename_number_start": "false",
      "extension": "png",
      "dpi": 300,
      "quality": 100,
      "optimize_image": "true",
      "lossless_webp": "false",
      "overwrite_mode": "false",
      "show_history": "false",
      "show_history_by_prefix": "true",
      "embed_workflow": "true",
      "show_previews": "true",
      "images": [
        "109",
        0
      ]
    }},
    "class_type": "Image Save",
    "_meta": {{
      "title": "Image Save"
    }}
  }},
  "128": {{
    "inputs": {{
      "strength": 1,
      "start_percent": 0,
      "end_percent": 1,
      "positive": [
        "6",
        0
      ],
      "negative": [
        "7",
        0
      ],
      "control_net": [
        "129",
        0
      ],
      "image": [
        "131",
        0
      ]
    }},
    "class_type": "ControlNetApplyAdvanced",
    "_meta": {{
      "title": "Apply ControlNet (Advanced)"
    }}
  }},
  "129": {{
    "inputs": {{
      "control_net_name": "OpenPoseXL2.safetensors"
    }},
    "class_type": "ControlNetLoader",
    "_meta": {{
      "title": "Load ControlNet Model"
    }}
  }},
  "131": {{
    "inputs": {{
      "url_or_path": "''' + face_pose_url + '''"
    }},
    "class_type": "LoadImageFromUrlOrPath",
    "_meta": {{
      "title": "LoadImageFromUrlOrPath"
    }}
  }},
  "132": {{
    "inputs": {{
      "images": [
        "131",
        0
      ]
    }},
    "class_type": "PreviewImage",
    "_meta": {{
      "title": "Preview Image"
    }}
  }}
}}
'''

inference_auto='''
{{
  "4": {{
    "inputs": {{
      "model_name": "GroundingDINO_SwinT_OGC (694MB)"
    }},
    "class_type": "GroundingDinoModelLoader (segment anything)",
    "_meta": {{
      "title": "GroundingDinoModelLoader (segment anything)"
    }}
  }},
  "12": {{
    "inputs": {{
      "model_name": "sam_vit_b (375MB)"
    }},
    "class_type": "SAMModelLoader (segment anything)",
    "_meta": {{
      "title": "SAMModelLoader (segment anything)"
    }}
  }},
  "14": {{
    "inputs": {{
      "garment_description": "model wearing {product_string}",
      "negative_prompt": "monochrome, lowres, bad anatomy, worst quality, low quality",
      "width": 1024,
      "height": 1024,
      "num_inference_steps": 30,
      "guidance_scale": 2,
      "strength": 1,
      "seed": {seed},
      "pipeline": [
        "16",
        0
      ],
      "human_img": [
        "53",
        0
      ],
      "pose_img": [
        "36",
        0
      ],
      "mask_img": [
        "45",
        0
      ],
      "garment_img": [
        "54",
        0
      ]
    }},
    "class_type": "IDM-VTON",
    "_meta": {{
      "title": "Run IDM-VTON Inference"
    }}
  }},
  "15": {{
    "inputs": {{
      "images": [
        "14",
        0
      ]
    }},
    "class_type": "PreviewImage",
    "_meta": {{
      "title": "Preview Image"
    }}
  }},
  "16": {{
    "inputs": {{
      "weight_dtype": "float16"
    }},
    "class_type": "PipelineLoader",
    "_meta": {{
      "title": "Load IDM-VTON Pipeline"
    }}
  }},
  "25": {{
    "inputs": {{
      "prompt": "{product_string}",
      "threshold": 0.3,
      "sam_model": [
        "12",
        0
      ],
      "grounding_dino_model": [
        "4",
        0
      ],
      "image": [
        "53",
        0
      ]
    }},
    "class_type": "GroundingDinoSAMSegment (segment anything)",
    "_meta": {{
      "title": "GroundingDinoSAMSegment (segment anything)"
    }}
  }},
  "36": {{
    "inputs": {{
      "model": "densepose_r101_fpn_dl.torchscript",
      "cmap": "Viridis (MagicAnimate)",
      "resolution": 512,
      "image": [
        "53",
        0
      ]
    }},
    "class_type": "DensePosePreprocessor",
    "_meta": {{
      "title": "DensePose Estimator"
    }}
  }},
  "45": {{
    "inputs": {{
      "mask": [
        "25",
        1
      ]
    }},
    "class_type": "MaskToImage",
    "_meta": {{
      "title": "Convert Mask to Image"
    }}
  }},
  "52": {{
    "inputs": {{
      "output_path": "temporal",
      "filename_prefix": "inference-{gen_id}",
      "filename_delimiter": "_",
      "filename_number_padding": 1,
      "filename_number_start": "false",
      "extension": "png",
      "dpi": 300,
      "quality": 100,
      "optimize_image": "true",
      "lossless_webp": "false",
      "overwrite_mode": "false",
      "show_history": "false",
      "show_history_by_prefix": "true",
      "embed_workflow": "true",
      "show_previews": "true",
      "images": [
        "14",
        0
      ]
    }},
    "class_type": "Image Save",
    "_meta": {{
      "title": "Image Save"
    }}
  }},
  "53": {{
    "inputs": {{
      "url_or_path": "{pic_url}"
    }},
    "class_type": "LoadImageFromUrlOrPath",
    "_meta": {{
      "title": "LoadImageFromUrlOrPath"
    }}
  }},
  "54": {{
    "inputs": {{
      "url_or_path": "{garment_url}"
    }},
    "class_type": "LoadImageFromUrlOrPath",
    "_meta": {{
      "title": "LoadImageFromUrlOrPath"
    }}
  }},
  "55": {{
    "inputs": {{
      "images": [
        "54",
        0
      ]
    }},
    "class_type": "PreviewImage",
    "_meta": {{
      "title": "Preview Image"
    }}
  }},
  "56": {{
    "inputs": {{
      "images": [
        "53",
        0
      ]
    }},
    "class_type": "PreviewImage",
    "_meta": {{
      "title": "Preview Image"
    }}
  }}
}}'''
