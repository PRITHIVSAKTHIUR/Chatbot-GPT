---
title: StrangerX AI Bot
emoji: 🔥
colorFrom: blue
colorTo: pink
sdk: streamlit
sdk_version: 1.33.0
app_file: app.py
pinned: false
license: creativeml-openrail-m
---

🚀Check out the configuration reference at : https://huggingface.co/docs/hub/spaces-config-reference

🚀Huggingface space : https://huggingface.co/spaces/prithivMLmods/StrangerX-AI-Bot

🚀To Clone Just Install Git Past the Command : git clone https://huggingface.co/spaces/prithivMLmods/StrangerX-AI-Bot

ℹ️Generated Result in Huggingface Spaces:

ℹ️Text-2-Text Inference

![alt text](assets/1.png)

🔮Sample Prompt & Output

![alt text](assets/2.png)


.

.

.

You can use your own model like mistral & phi3 (or) refer the my hugging face repo for the model 

''' 
import requests

API_URL = "https://api-inference.huggingface.co/models/prithivMLmods/Dorado-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})
'''
