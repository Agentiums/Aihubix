# Aihubix

基于 BERT 模型的文本分类，对用户的查询进行分类，并将其匹配到最合适的 LLAMA 代理节点。利用人工智能驱动的自然语言处理和知识图推理，确保高效、准确的查询处理。

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

从 huggingface 官网上下载 bert_model.pth 训练好的模型权重到 data/model/ 文件夹中，下载地址：https://huggingface.co/

## 运行 web 后端

```shell
uvicorn app:app --reload --host 0.0.0.0 --port 11801
```

### 运行速度

识别的速度还是很快的，耗时:  0.02秒

<img src="https://github.com/Agentiums/Aihubix/blob/main/image/001.png" alt="001" style="zoom:80%;" />
