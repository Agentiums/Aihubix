# Aihubix

基于 BERT 模型的文本分类，对用户的查询进行分类，并将其匹配到最合适的 LLAMA 代理节点。利用人工智能驱动的自然语言处理和知识图推理，确保高效、准确的查询处理。

## 环境

python 3.8

torch 

tqdm

sklearn

transformers 

## 数据集

目前共有2个类别：chat、code，可以匹配到聊天模型和代码模型。数据集按如下划分：

- 训练集：36000条标题，每个类别的标题数为18000
- 验证集：2000条标题，每个类别的标题数为1000
- 测试集：2000条标题，每个类别的标题数为1000

可以按照 data 文件夹中的数据格式来准备自己任务所需的数据，并调整 config.py 中的相关配置参数。

## 预训练 BERT 模型

从 huggingface 官网上下载 bert-base-chinese 模型权重、配置文件和词典到 pretrained_bert 文件夹中，下载地址：https://huggingface.co/bert-base-chinese/tree/main

## 模型训练

文本分类模型训练：

```shell
python main.py --mode train --data_dir ./data --pretrained_bert_dir ./pretrained_bert
```

训练中间日志如下：

<img src="https://github.com/Agentiums/Aihubix/blob/main/train/image/a1.png?raw=true" alt="a1" style="zoom:80%;" />

模型在验证集上的效果如下：

<img src="https://github.com/Agentiums/Aihubix/blob/main/train/image/a2.png?raw=true" alt="a2" style="zoom:80%;" />

### 模型预测

对 data 文件夹下的 input.txt 中的文本进行分类预测：

```shell
python main.py --mode predict --data_dir ./data --pretrained_bert_dir ./pretrained_bert --input_file ./data/input.txt
```

输出如下结果：

<img src="https://github.com/Agentiums/Aihubix/blob/main/train/image/a3.png?raw=true" alt="a3" style="zoom:80%;" />
