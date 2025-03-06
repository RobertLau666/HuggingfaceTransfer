import time
from huggingface_hub import snapshot_download, login
from util import create_dir_or_file
from config import token


login(token=token)

repo_id = "omni-research/Tarsier2-Recap-7b"
root_dir = 'temp'
local_dir = root_dir + '/' + repo_id.replace('/','_')
cache_dir = local_dir + "/cache"

create_dir_or_file(root_dir)
create_dir_or_file(local_dir)
create_dir_or_file(cache_dir)

try:
    snapshot_download(
        cache_dir=cache_dir,
        local_dir=local_dir,
        repo_type='model', # Accepted repo types are: [None (default), 'model', 'dataset', 'space']
        repo_id=repo_id,
        local_dir_use_symlinks=False,
        resume_download=True,
        allow_patterns=None,
        ignore_patterns=None,
    )
except Exception as e:
    print(e)
else:
    print(f"Download '{repo_id}' finished!")