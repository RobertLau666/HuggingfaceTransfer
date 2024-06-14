# huggingface_download
## Install
```
git clone https://github.com/RobertLau666/huggingface_download.git
cd huggingface_download
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

## Usge
### Download the entire repository
```
python repository_download.py
```
### Download a single file
It will automatically download to the previous path, no dragging
```
python file_download.py
```
