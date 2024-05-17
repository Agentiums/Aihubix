<h1 align="center">
  <b>Aihubix</b>
  <br>
</h1>
<p align="center">Based on the BERT model text classification, the user query is classified and matched to the most appropriate LLAMA agent node. AI-driven natural language processing and knowledge graph reasoning are used to ensure efficient and accurate query processing.</p>

<p align="center">
<a href="https://github.com/Agentiums/Aihubix/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/Agentiums/Aihubix"><img alt="Release" src="https://img.shields.io/badge/LICENSE-MIT-important"></a>
</p>
<p align="center">
  <a href="/README_zh.md">中文文档</a> •
  <a href="/train/README.md">Training the model</a> 
</p>




## environment

python 3.8

torch 

tqdm

sklearn

transformers 

## category

There are currently two categories: chat and code, which can be matched to chat models and code models.

## Pre-trained BERT model

Download the bert-base-chinese model weights, configuration files and dictionaries from huggingface official website to the pretrained_bert folder. Download address: https://huggingface.co/bert-base-chinese/tree/main

## Trained BERT model

Download bert_model.pth from huggingface official website and put the trained model weights into data/model/ folder. Download address: https://huggingface.co/huggingfacess/Aihubix-v1

## Running the web backend

```shell
cd server
uvicorn app:app --reload --host 0.0.0.0 --port 11801
```

### Testing the Model

```
cd server
python3 post.py
```

### Running speed

The recognition speed is still very fast, time consumption: 0.02 seconds

<img src="https://github.com/Agentiums/Aihubix/blob/main/image/001.png?raw=true" alt="001" style="zoom:80%;" />

### Todo

https://github.com/zejunwang1/bert_text_classification

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Agentiums/Aihubix&type=Date)](https://star-history.com/#Agentiums/Aihubix&Date)

