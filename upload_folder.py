import os
from tqdm import tqdm
from huggingface_hub import HfApi, login
from huggingface_hub.utils import RepositoryNotFoundError
from config import token

login(token=token)
api = HfApi()

repo_id = "RobertLau/Stars"
repo_type = "dataset"
folder_path = "/data/code/chenyu.liu/Datasets/Stars/man"
dir_in_repo = "man"

# ------------------- 检查 dataset 是否存在 -------------------
try:
    api.dataset_info(repo_id)
    print(f"The repository {repo_id} already exists.")
except RepositoryNotFoundError:
    print(f"{repo_id} not found. Creating...")
    api.create_repo(repo_id=repo_id, repo_type=repo_type, private=False)
    print("Repository created.")


# ------------------- 收集所有文件 -------------------
all_files = []
for root, _, files in os.walk(folder_path):
    for f in files:
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, folder_path)
        repo_target_path = f"{dir_in_repo}/{rel_path}"   # 上传到 repo 的 man/ 下
        all_files.append((full_path, repo_target_path))

print(f"Total files to upload: {len(all_files)}")


# ------------------- tqdm 进度条上传 -------------------
print("Uploading files with progress bar...")

for local_path, repo_path in tqdm(all_files, desc="Uploading", unit="file"):
    api.upload_file(
        path_or_fileobj=local_path,
        path_in_repo=repo_path,
        repo_id=repo_id,
        repo_type=repo_type,
        create_pr=False,       # 直接上传，不走 PR
    )

print("Upload completed!")