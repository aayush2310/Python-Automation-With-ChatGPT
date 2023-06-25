#we want these python scripts to take our input whenever we start the script of what use case we want to automate with python.
#So, the promt "Write python script for ..." should not be hard coded there, rather take inputs from us and execute that as a prompt.

import requests
import argparse
#argparse is different from requests library which we needed to install using pip3, it is a built in module,so no installation required.
#it helps us parse the cpmmand line arguements that we provide to the python application.


parser = argparse.ArgumentParser()   #so, this is an object that has a method that allows us to read the parameters/arguements that we provide in terminal
parser.add_argument("prompt",help="The prompt to send to the OpenAI API")     #adding description is optional about what that promt is 
#using the parser object i am going to call a method called parse_args(), which will go through whatever arguements we have added here 
args = parser.parse_args()
#args here refer to the input i provide to the script.
#and now i can access the value provided in my terminal using args.prompt

#Parameterized my script


api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    "Content-Type": "application/json",
    "Authorization" : "Bearer" + api_key
}

request_data = {
    "model" : "text-davinci-003",
    "prompt" : f"Write python script to {args.prompt}. Provide only code, no text",    #variable reference
    #so, this is going to be our input for whatever usecase we provide as an input and then the rest of them will stay the same.
    #The things that always apply are that we always want the python script and we always want the code and  not the text.
    #So xxx has to be parameterized and we need to get that from the user input
    "max_tokens": 100,
    "temperature" : 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
               print(response.json()["choices"][0]["text"])
else:
               print(f"Request failed with status code: {str(response.status_code)}")



#now i need to provide arguement while running my python script.
#everytime i execute the script, it makes a new request to the api and we are getting different response

#when we will have this script ready, i am gonna actually execute two usecases-
# extracting the headers from blog article and translating to spanish
# cleaning up my downloads folder with all the files that are older than 30 days.


#I need to write a python script code that insted of printing out the result in the console, saves it in a file.