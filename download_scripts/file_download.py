import time
from huggingface_hub import hf_hub_download
from util import create_dir_or_file

repo_id = "diffusers/stable-diffusion-xl-1.0-inpainting-0.1"
root_dir = '../temp'
local_dir = root_dir + '/' + repo_id.replace('/','_')
cache_dir = local_dir + "/cache"
filename= "text_encoder/model.fp16.safetensors"

create_dir_or_file(root_dir)
create_dir_or_file(local_dir)
create_dir_or_file(cache_dir)

try:
    hf_hub_download(
        cache_dir=cache_dir,
        local_dir=local_dir,
        repo_type=None, # Accepted repo types are: [None (default), 'model', 'dataset', 'space']
        repo_id=repo_id,
        filename=filename,
        local_dir_use_symlinks=False,
        resume_download=True,
        etag_timeout=100
    )
except Exception as e:
    print(e)
else:
    print('下载完成')
