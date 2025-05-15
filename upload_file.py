from huggingface_hub import HfApi, login
from huggingface_hub.utils import RepositoryNotFoundError
from config import token  # 确保你的 token 在 config.py 中定义

# 登录 Hugging Face
login(token=token)
api = HfApi()

# 仓库信息
repo_id = "RobertLau/ChildClassification"  # 替换为你的仓库名称
repo_type = "model"  # 仓库类型，可选值: [None (默认), 'model', 'dataset', 'space']
file_path = "/data/code/chenyu.liu/others/child_train/ChildClassification/checkpoint/traintitle:anime_trainindex:6/20250514013432/output_focal_convnext/traintitle:anime_trainindex:6_20250514013432_output_focal_convnext_epoch:29.pth"  # 替换为本地文件路径
path_in_repo = "anime/traintitle:anime_trainindex:6_20250514013432_output_focal_convnext_epoch:29.pth"  # 文件在仓库中的路径（可自定义）

# 检查仓库是否存在
try:
    # 尝试获取仓库信息
    api.model_info(repo_id)
    print(f"The repository {repo_id} already exists, directly upload the file.")
except RepositoryNotFoundError:
    # 如果仓库不存在，则创建
    print(f"The repository {repo_id} does not exist and is being created.")
    api.create_repo(
        repo_id=repo_id,
        repo_type=repo_type,
        private=False,  # 如果希望仓库是私有的，设置为 True
    )
    print(f"The repository {repo_id} is created successfully.")

# 上传文件
print("Uploading the file...")
api.upload_file(
    path_or_fileobj=file_path,  # 本地文件路径
    path_in_repo=path_in_repo,  # 文件在仓库中的路径
    repo_id=repo_id,
    repo_type=repo_type,
)
print("Upload completed!")