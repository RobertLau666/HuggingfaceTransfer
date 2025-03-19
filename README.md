# HuggingfaceTransfer

HuggingfaceTransfer is a project for uploading or downloading huggingface files.

## Install

```
git clone https://github.com/RobertLau666/HuggingfaceTransfer.git
cd HuggingfaceTransfer
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Network Proxy Configuration

### 1. [clash-for-linux-backup](https://github.com/Elegycloud/clash-for-linux-backup) (recommend)

### 2. others

#### Setting global proxy

```
export ALL_PROXY=http://127.0.0.1:7890
```

#### Verify that the configuration is successful

```
curl www.google.com
```

## Download method

### 1. [huggingface-cli](https://hf-mirror.com/docs/huggingface_hub/guides/download#download-from-the-cli) (recommend)

huggingface-cli is a command line tool provided by Hugging Face, which provides a perfect downloading function.

```Network Proxy Configuration``` is not required.

reference link: https://hf-mirror.com.

```shell
# 1. Install
pip install -U huggingface_hub

# 2. Setting environment variables
# Linux: It is recommended to write the previous line to ~/.bashrc.
export HF_ENDPOINT=https://hf-mirror.com
# Windows Powershell
$env:HF_ENDPOINT = "https://hf-mirror.com"

# 3. Download
# --repo-type: model, dataset, space
# You can add --local-dir-use-symlinks False to disable soft links to files so that what you see is what you get under the download path, as explained in the tutorial mentioned above.
huggingface-cli download --repo-type model --resume-download xx/xx --local-dir xx_xx

# for example: 
# 3.1 Download model
huggingface-cli download --repo-type model --resume-download QuanSun/EVA-CLIP --local-dir QuanSun_EVA-CLIP
# 3.2 Download dataset
huggingface-cli download --repo-type dataset --resume-download wikitext --local-dir wikitext
# 3.2 Download space
huggingface-cli download --repo-type space --resume-download depth-anything/Depth-Anything-V2 --local-dir depth-anything_Depth-Anything-V2
```

### 2. huggingface_hub
```Network Proxy Configuration``` is required.
####  Setting huggingface token

Create and get [Access Tokens](https://huggingface.co/settings/tokens) in [Hugging Face](https://huggingface.co/), and store it in parameter ``token`` of config.py.

#### Download

##### Entire repository

```
python download_repository.py
```

Or clone repository, e.g.:

```
git clone https://huggingface.co/spaces/omni-research/Tarsier2-7b
```

##### A single file

It will automatically download to the previous path, no dragging

```
python download_file.py
```

#### Upload

##### Files under folder

```
python upload_folder.py
```

##### A single file

```
python upload_file.py
```

### 3. modelscope

```
modelscope download --model BestWishYSH/ConsisID-preview --local-dir ckpts
```

### 4. git clone

```
git lfs install
git clone https://www.wisemodel.cn/SHYuanBest/ConsisID-Preview.git
```
