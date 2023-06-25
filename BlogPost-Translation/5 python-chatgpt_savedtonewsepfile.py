import requests
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument("prompt",help="The prompt to send to the OpenAI API")  
parser.add_argument("file_name",help="Name of the file to save Python Script")  

args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    "Content-Type": "application/json",
    "Authorization" : "Bearer" + api_key
}


request_data = {
    "model" : "text-davinci-003",
    "prompt" : f"Write python script to {args.prompt}. Provide only code, no text",  
    "max_tokens": 100,
    "temperature" : 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
              response_text = response.json()["choices"][0]["text"]
              with open("args.file_name", "w") as file:
                      file.write(response_text)
else:
               print(f"Request failed with status code: {str(response.status_code)}")

#so, instaed of hardcoding this value ("output.py"-file name) here, we are gonna also pass that as an input.We are gonna tell the python-please send the request
#to generate python script for this usecase and then save it into a file with this name.
#so, same way as i did before, first need to register that arguement(the filename given by me in terminal) and give it a name so that i can use it right there

#Now i need to extract my api key into an environment variable as it is secret.