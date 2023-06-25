#Python script to connect to OpenAI API


#Whenever we are connecting to an external API, we are making a request. We are gonna need a python library that will allow us to send request to external 
#endpoints like API endpoints

#How do we make a request to OpenAI?
#We have 2 options-(i)We have a Generic HTTP library which is great bcz. I can use it for whatever API or whatever tool I want and not just OpenAI-if i learn
#using generic api ,i will learn making request to any api.
#(ii)OpenAI specific library-usually, the tools that provide an API will also provide a library that hides the underlying complexity of making a request, 
#setting out the parameter, etc or  setting the API key and lets you interact with the API with a more high level code.So , in that library they will give you
#objects,methods,etc that make the whole process easier so that we dont have to write everything from scratch and generally that is the purpose of a library.

import requests

#now i have a library that makes me make requests to external endpoints.
#now, i need to find out what is the endpoint of openAI API that i want to connect to 
#we are writing a python script that will take our inputs which is gonna be any automation usecase. It will then go to the api and say, for this specific use
#case that user entered here, I want to have a python script, just like i type in chatgpt to write python script for this particular usecase, so I am doing
#that programatically.

#now, I need to find out end point that allows us to do that.

#I find endpoints of API in the api documentation
#Every public API comes with a documentation that tells me how to use that API

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

#generating the request
#HTTP Request Methods:-Indicate the desired action to be performed
#  1)GET->to retrieve data
#  2)POST->To send data and optionally get back data
#  Other methods: PATCH, PUT, DELETE ....

request_headers = {
    "Content-Type": "application/json",
    "Authorization" : "Bearer" + api_key
}

#we include the request data to exactly communicate with the api endpoint and tell it exactly what we need.
#model refers to the ML model of openAI that we want to use-openAI is an organization that works on different types of AI tools like text,visuals,etc. so 
#they have various models that specialize and do different things. (23:08)
request_data = {
    "model" : "text-davinci-003",
    "prompt" : "Write python script for hello world",
    "max_tokens": 100,
    "temperature" : 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

#I am sending content type request to the api in a json format.
#Example-GPT-3 models can understand and generate natural language
#That's what a model is and when we connect to an API ,we basically select which machine learning model we want to talk to.
#In our case I want to generate a python script which will be little bit more complex task, so i will go with the best option i have.
#Codex is a model that can understand and generate codes including translating natural language to code.It builds on top of gpt-3 model.
#I am choosing "text-davinci-003" model which works perfectly for my usecase and generates really good code with consistent results.
#The great thing about using this API is that i can just replace the model name with any other model names i see here including the two models under Codex
#I dont need to adjust or change the code, i only change th model name.

#The second parameter in the request is promt bcz. promt is the main part of the request that tells what we are asking for exactly.

#Max tokens limits the response that i get in tokens.-Using this parameter i am controlling the behaviour of the API model when generating the text.
#This specifies the maximum number of tokens such as words or puncuation marks that the API model should generate in its response.
#hello world python script will not contain more than 100 words.

#temperature tells the ML model , when you are creating your response, be sure to be super creative(temperature=1) or be as precisice and predictible as possible(temperature=0)

if response.status_code == 200:
               print(response.json()["choices"][0]["text"])
else:
               print(f"Request failed with status code: {str(response.status_code)}")

#i am sending json and also receiving json response,this is how i can grab the json response using .json

#i recieved couple of more things in response in addition to the python script i requested for.
#just like i have metadata on requests, i have meta data on response as well.
#When we run our python script,we make a new request like entering question in the chatgpt everytime.
#now we can send whatever promt i want programatically and then i will receive a response from the api i am connecting to.