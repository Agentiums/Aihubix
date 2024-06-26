<h1 align="center">
  <b>Aihubix</b>
  <br>
</h1>
<p align="center">基于 BERT 模型的文本分类，对用户的查询进行分类，并将其匹配到最合适的 LLAMA 代理节点。利用人工智能驱动的自然语言处理和知识图推理，确保高效、准确的查询处理。</p>

<p align="center">
<a href="https://github.com/Agentiums/Aihubix/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/Agentiums/Aihubix"><img alt="Release" src="https://img.shields.io/badge/LICENSE-MIT-important"></a>
</p>

<p align="center">
  <a href="/README.md">English Documentation</a> •
  <a href="/train/README.md">训练模型</a> 
</p>



## 环境

python 3.8

torch 

tqdm

sklearn

transformers 

## 类别

目前共有2个类别：chat、code，可以匹配到聊天模型和代码模型。

## 预训练 BERT 模型

从 huggingface 官网上下载 bert-base-chinese 模型权重、配置文件和词典到 pretrained_bert 文件夹中，下载地址：https://huggingface.co/bert-base-chinese/tree/main

## 已训练 BERT 模型

从 huggingface 官网上下载 bert_model.pth 训练好的模型权重到 data/model/ 文件夹中，下载地址：https://huggingface.co/huggingfacess/Aihubix-v1

## 运行 web 后端

```shell
cd server
uvicorn app:app --reload --host 0.0.0.0 --port 11801
```

### 测试模型

```
cd server
python3 post.py
```

### 运行速度

识别的速度还是很快的，耗时:  0.02秒

<img src="https://github.com/Agentiums/Aihubix/blob/main/image/001.png?raw=true" alt="001" style="zoom:80%;" />

### 参考

https://github.com/zejunwang1/bert_text_classification

### 关注历史

[![Star History Chart](https://api.star-history.com/svg?repos=Agentiums/Aihubix&type=Date)](https://star-history.com/#Agentiums/Aihubix&Date)

