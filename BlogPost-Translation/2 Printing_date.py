import requests


api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    "Content-Type": "application/json",
    "Authorization" : "Bearer" + api_key
}

request_data = {
    "model" : "text-davinci-003",
    "prompt" : "Write python script for printing out today's date. Provide only code, no text",
    "max_tokens": 100,
    "temperature" : 0.5
}

#Chatgpt returns additional text apart from the code we want i.e the explanations. So we can get that here as well.

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
               print(response.json()["choices"][0]["text"])
else:
               print(f"Request failed with status code: {str(response.status_code)}")
