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

## data set

There are currently two categories: chat and code, which can be matched to chat models and code models. The dataset is divided as follows:

- Training set: 36,000 titles, 18,000 titles in each category
- Validation set: 2000 titles, 1000 titles for each category
- Test set: 2000 titles, 1000 titles in each category

You can prepare the data required for your task according to the data format in the data folder and adjust the relevant configuration parameters in config.py.

## Pre-trained BERT model

Download the bert-base-chinese model weights, configuration files and dictionaries from huggingface official website to the pretrained_bert folder. Download address: https://huggingface.co/bert-base-chinese/tree/main

## Model Training

Text classification model training:

```shell
python main.py --mode train --data_dir ./data --pretrained_bert_dir ./pretrained_bert
```

The training log is as follows:

<img src="https://github.com/Agentiums/Aihubix/blob/main/train/image/a1.png?raw=true" alt="a1" style="zoom:80%;" />

The effect of the model on the validation set is as follows:

<img src="https://github.com/Agentiums/Aihubix/blob/main/train/image/a2.png?raw=true" alt="a2" style="zoom:80%;" />

### Model predictions

Make classification predictions for the text in input.txt under the data folder:

```shell
python main.py --mode predict --data_dir ./data --pretrained_bert_dir ./pretrained_bert --input_file ./data/input.txt
```

The output is as follows:

<img src="https://github.com/Agentiums/Aihubix/blob/main/train/image/a3.png?raw=true" alt="a3" style="zoom:80%;" />
