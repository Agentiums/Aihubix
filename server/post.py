import requests


test = "天空为什么是蓝色的"

system_data = {
			"text": test
		}
		
headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.2987.133 Safari/537.36'
		}
url = 'http://127.0.0.1:11801/api/v1/text'

response = requests.post(url, headers=headers, verify=False, json=system_data)

print(response.json())

if response.json()['model'] == "chat":
	print("chat")
else:
	print("code")

