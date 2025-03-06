# HuggingfaceTransfer
HuggingfaceTransfer is a project for uploading or downloading huggingface files.
## Install
```
git clone https://github.com/RobertLau666/HuggingfaceTransfer.git
cd HuggingfaceTransfer
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Network Proxy Configuration
### Setting global proxy
```
export ALL_PROXY=http://127.0.0.1:7890
```
### Verify that the configuration is successful
```
curl www.google.com
```
### Setting huggingface token
Create and get [Access Tokens](https://huggingface.co/settings/tokens) in [Hugging Face](https://huggingface.co/), and store it in parameter ```token``` of config.py.
## Usge
### Download
#### Entire repository
```
python download_repository.py
```
or Clone repository, e.g.:
```
git clone https://huggingface.co/spaces/omni-research/Tarsier2-7b
```
#### A single file
It will automatically download to the previous path, no dragging
```
python download_file.py
```
### Upload
#### files under folder
```
python upload_folder.py
```
#### A single file
```
python upload_file.py
```