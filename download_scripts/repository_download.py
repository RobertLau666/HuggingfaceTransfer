import time
from huggingface_hub import snapshot_download
from util import create_dir_or_file

repo_id = "csebuetnlp/mT5_multilingual_XLSum"
root_dir = '../temp'
local_dir = root_dir + '/' + repo_id.replace('/','_')
cache_dir = local_dir + "/cache"

create_dir_or_file(root_dir)
create_dir_or_file(local_dir)
create_dir_or_file(cache_dir)

try:
    snapshot_download(
        cache_dir=cache_dir,
        local_dir=local_dir,
        repo_type=None, # Accepted repo types are: [None (default), 'model', 'dataset', 'space']
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
