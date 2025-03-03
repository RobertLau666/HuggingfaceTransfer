from huggingface_hub import HfApi, login
from huggingface_hub.utils import RepositoryNotFoundError
from config import token


login(token=token)
api = HfApi()

repo_id = "RobertLau/age_regression"
repo_type = "model" # Accepted repo types are: [None (default), 'model', 'dataset', 'space']
folder_path = "/maindata/data/shared/public/chenyu.liu/others/1_image_eval/age_regression/model" # It won't upload this folder, just upload the files in this folder

# Check whether the repository exists
try:
    # Try to get repository information
    api.model_info(repo_id)
    print(f"The repository {repo_id} already exists, directly upload the model.")
except RepositoryNotFoundError:
    # If the repository does not exist, it is created
    print(f"The repository {repo_id} does not exist and is being created.")
    api.create_repo(
        repo_id=repo_id,
        repo_type=repo_type,
        private=False,
    )
    print(f"The repository {repo_id} is created successfully.")

print("Uploading files in the model folder...")
api.upload_folder(
    folder_path=folder_path,
    repo_id=repo_id,
    repo_type=repo_type,
)
print("Upload completed!")