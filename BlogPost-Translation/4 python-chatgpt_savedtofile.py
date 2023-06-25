import requests
import argparse

parser = argparse.ArgumentParser() 
parser.add_argument("prompt",help="The prompt to send to the OpenAI API")  

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
              with open("output.py", "w") as file:
                      file.write(response_text)
              #open will create a new file.The second arguement is about writing or appending to our file.
              #this line basically goes and tries to find a file called output.py , if it doesn't find one, it creates one and opens it in the mode we specify
              #These two lines allow us to save the response text to a seperate python file.
else:
               print(f"Request failed with status code: {str(response.status_code)}")


# Now I want that i should save my outputs in the file but they should not overwrite each other everytime i run my command on the terminal.It should 
# create a nw seperate output.py file every time.

