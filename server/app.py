import os
import torch
import numpy as np
from transformers import BertConfig, BertTokenizer, BertForSequenceClassification
import uvicorn
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
import time


app = FastAPI(docs_url=None, redoc_url=None)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = None
model = None
#label_list = None
label_list = ['chat', 'code']


def set_seed(seed):
	np.random.seed(seed)
	torch.manual_seed(seed)
	torch.cuda.manual_seed_all(seed)
	torch.backends.cudnn.deterministic = True
	

def load_model():
	global tokenizer
	global model
	#global label_list
	
	set_seed(1)
	pretrained_bert_dir = "bert"
	model_dir = os.path.join("data/model/bert_model.pth")
	#label_file = "data/label.txt"
	#label_list = [label.strip() for label in open(label_file, "r", encoding="UTF-8").readlines()]
	num_labels = len(label_list)
	
	tokenizer = BertTokenizer.from_pretrained(pretrained_bert_dir)
	bert_config = BertConfig.from_pretrained(pretrained_bert_dir, num_labels=num_labels)
	model = BertForSequenceClassification.from_pretrained(
		os.path.join(pretrained_bert_dir),
		config=bert_config
	)
	model.to(device)
	
	# 加载模型
	model.load_state_dict(torch.load(model_dir, map_location=device))
	model.eval()
	
	# gc.freeze()
	print('load model')
	
	
# 加载模型
load_model()


class Hint(BaseModel):
	text: str


@app.post("/api/v1/text")
async def data(request_body: Hint):
	start = time.time()
	
	# 获取值
	message = request_body.text
	# print(message)

	inputs = tokenizer(message,
		max_length=128,
		truncation="longest_first",
		return_tensors="pt")
	
	inputs = inputs.to(device)
	
	with torch.no_grad():
		outputs = model(**inputs)
		logits = outputs[0]
		label = torch.max(logits.data, 1)[1].tolist()
		
		data_label = label_list[label[0]]
		
		print("分类结果: " + data_label)
		
		end = round(time.time() - start, 2)
		print("耗时:", end)
		
		message_text = {
			"model": data_label,
			"time": end,
			"text": message
		}
		
		return message_text


if __name__ == "__main__":
	uvicorn.run("app:app", host="0.0.0.0", port=11801)


