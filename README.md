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

### 2. other methods
#### Setting global proxy
```
export ALL_PROXY=http://127.0.0.1:7890
```
#### Verify that the configuration is successful
```
curl www.google.com
```

## Download methods

### 1. [huggingface-cli](https://hf-mirror.com/docs/huggingface_hub/guides/download#download-from-the-cli) (recommend)

huggingface-cli is a command line tool provided by Hugging Face, which provides a perfect downloading function.

```Network Proxy Configuration``` is not required.

reference link: https://hf-mirror.com.

```shell
# 1. Install
pip install -U huggingface_hub

# 2. Setting environment variables
# Linux: It is recommended to write the previous line to ~/.bashrc, or you must rerun in each terminal which need download.
export HF_ENDPOINT=https://hf-mirror.com
# Windows Powershell
$env:HF_ENDPOINT = "https://hf-mirror.com"

# 3. Download
# --repo-type: model, dataset, space
# You can add --local-dir-use-symlinks False to disable soft links to files so that what you see is what you get under the download path, as explained in the tutorial mentioned above.
huggingface-cli download --repo-type model --resume-download xx/xx --local-dir xx_xx

# for example: 
# 3.1 Download model
huggingface-cli download --repo-type model --resume-download RobertLau/convnext --local-dir RobertLau_convnext
huggingface-cli download --repo-type model --resume-download facebook/detr-resnet-50 --local-dir facebook_detr-resnet-50
huggingface-cli download --repo-type model --resume-download skytnt/anime-aesthetic --local-dir skytnt_anime-aesthetic
huggingface-cli download --repo-type model --resume-download google/gemma-3n-e4b-it --local-dir google_gemma-3n-e4b-it
huggingface-cli download --repo-type model --resume-download SliverHand/RealESRGAN_x4plus --local-dir SliverHand_RealESRGAN_x4plus
huggingface-cli download --repo-type model --resume-download Lightricks/LTX-Video-0.9.7-dev --local-dir Lightricks_LTX-Video-0.9.7-dev
huggingface-cli download --repo-type model --resume-download Lightricks/ltxv-spatial-upscaler-0.9.7 --local-dir Lightricks_ltxv-spatial-upscaler-0.9.7
huggingface-cli download --repo-type model --resume-download Wan-AI/Wan2.1-I2V-14B-720P-Diffusers --local-dir Wan-AI_Wan2.1-I2V-14B-720P-Diffusers
huggingface-cli download --repo-type model --resume-download OpenGVLab/InternVideo2_5_Chat_8B --local-dir OpenGVLab_InternVideo2_5_Chat_8B
huggingface-cli download --repo-type model --resume-download PhilipC/HumanOmniV2 --local-dir PhilipC_HumanOmniV2
huggingface-cli download --repo-type model --resume-download Video-R1/Video-R1-7B --local-dir Video-R1_Video-R1-7B
huggingface-cli download --repo-type model --resume-download Kwai-Keye/Keye-VL-8B-Preview --local-dir Kwai-Keye_Keye-VL-8B-Preview
huggingface-cli download --repo-type model --resume-download omni-research/Tarsier-34b --local-dir omni-research_Tarsier-34b
huggingface-cli download --repo-type model --resume-download omni-research/Tarsier-7b --local-dir omni-research_Tarsier-7b
huggingface-cli download --repo-type model --resume-download Lightricks/LTX-Video-0.9.8-13B-distilled --local-dir Lightricks_LTX-Video-0.9.8-13B-distilled
huggingface-cli download --repo-type model --resume-download csebuetnlp/mT5_multilingual_XLSum --local-dir csebuetnlp_mT5_multilingual_XLSum
huggingface-cli download --repo-type model --resume-download CompVis/stable-diffusion-v1-4 --local-dir CompVis_stable-diffusion-v1-4
huggingface-cli download --repo-type model --resume-download openai/clip-vit-large-patch14 --local-dir openai_clip-vit-large-patch14
huggingface-cli download --repo-type model --resume-download booksforcharlie/stable-diffusion-inpainting --local-dir booksforcharlie_stable-diffusion-inpainting
huggingface-cli download --repo-type model --resume-download CompVis/stable-diffusion-safety-checker --local-dir CompVis_stable-diffusion-safety-checker
huggingface-cli download --repo-type model --resume-download CompVis/stable-diffusion-v-1-4-original --local-dir CompVis_stable-diffusion-v-1-4-original
huggingface-cli download --repo-type model --resume-download google/flan-t5-xl --local-dir google_flan-t5-xl
huggingface-cli download --repo-type model --resume-download microsoft/phi-2 --local-dir microsoft_phi-2
huggingface-cli download --repo-type model --resume-download Qwen/Qwen3-4B-Base --local-dir Qwen_Qwen3-4B-Base
# Some files may fail to be downloaded after the preceding command is executed. Do not run the preceding command again. Instead, add '--include', for example, run the following  command to download missing files one by one.
huggingface-cli download --repo-type model google/gemma-3n-e4b-it --include "model-00002-of-00004.safetensors" --local-dir .
huggingface-cli download --repo-type model Kijai/WanVideo_comfy --include "Wan21_CausVid_14B_T2V_lora_rank32.safetensors" --local-dir .
huggingface-cli download --repo-type model PhilipC/HumanOmniV2 --include "model-00001-of-00004.safetensors" --local-dir .
huggingface-cli download --repo-type model omni-research/Tarsier-7b --include "model-00001-of-00003.safetensors" --local-dir .
huggingface-cli download --repo-type model Lightricks/LTX-Video-0.9.8-13B-distilled --include "transformer/diffusion_pytorch_model-00004-of-00006.safetensors" --local-dir .
huggingface-cli download --repo-type model SanctumAI/Meta-Llama-3-8B-Instruct-GGUF --include "meta-llama-3-8b-instruct.Q4_0.gguf" --local-dir .

# 3.2 Download dataset
huggingface-cli download --repo-type dataset --resume-download wikitext --local-dir wikitext

# 3.2 Download space
huggingface-cli download --repo-type space --resume-download depth-anything/Depth-Anything-V2 --local-dir depth-anything_Depth-Anything-V2
huggingface-cli download --repo-type space --resume-download multimodalart/wan2-1-fast --local-dir multimodalart_wan2-1-fast
huggingface-cli download --repo-type space --resume-download Miragic-AI/Miragic-Speed-Painting --local-dir Miragic-AI_Miragic-Speed-Painting
huggingface-cli download --repo-type space --resume-download Kwai-Keye/Keye-VL-8B-Preview --local-dir Kwai-Keye_Keye-VL-8B-Preview
huggingface-cli download --repo-type space --resume-download hysts/PnP-diffusion-features --local-dir hysts_PnP-diffusion-features
# Some files may fail to be downloaded after the preceding command is executed. Do not run the preceding command again. Instead, add '--include', for example, run the following  command to download missing files one by one.
huggingface-cli download --repo-type dataset BestWishYsh/ConsisID-preview-Data --include "masks/masks.tar.partaa" --local-dir .
# If it is a certain folder
huggingface-cli download --repo-type dataset BestWishYsh/ConsisID-preview-Data --include "masks/*" --local-dir .

# 4. Upload
# You can either upload a single file or an entire folder: (This method has not been proven to work)
# Usage:  huggingface-cli upload [repo_id] [local_path] [path_in_repo]
huggingface-cli upload RobertLau/ChildClassification \
/data/code/chenyu.liu/others/child_train/ChildClassification/checkpoint/traintitle:anime_trainindex:3/20250423162336/output_focal_convnext/traintitle:anime_trainindex:3_20250423162336_output_focal_convnext_epoch:34.pth \
anime/traintitle:anime_trainindex:3_20250423162336_output_focal_convnext_epoch:34.pth
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
