import time
from huggingface_hub import hf_hub_download
from util import create_dir_or_file


repo_id = "QuanSun/EVA-CLIP"
root_dir = 'temp'
local_dir = root_dir + '/' + repo_id.replace('/','_')
cache_dir = local_dir + "/cache"
filename= "EVA02_CLIP_L_336_psz14_s6B.pt"

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
    print(f"Download '{filename}' finished!")