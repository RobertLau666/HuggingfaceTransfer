import time
from huggingface_hub import snapshot_download

repo_id = "SG161222/RealVisXL_V3.0"
root_dir = '/dfs/comicai/chenyu.liu/hf_download/temp'
local_dir = root_dir + '/' + repo_id.replace('/','_')
cache_dir = local_dir + "/cache"

try:
    snapshot_download(cache_dir=cache_dir,
    local_dir=local_dir,
    # repo_type=None, # Accepted repo types are: [None (default), 'model', 'dataset', 'space']
    repo_id=repo_id,
    local_dir_use_symlinks=False,
    resume_download=True,
    allow_patterns=["*.model", "*.safetensors", "*.pt", "*.pth", "*.ckpt", "*.bin", "*.json", "*.png", "*.jpg", "*.py", "*.md", "*.txt", "*.gitattributes", "*.ipynb"],
    ignore_patterns=["*.msgpack", "*.h5", "*.ot",],
    )
except Exception as e:
    print(e)
else:
    print('下载完成')
