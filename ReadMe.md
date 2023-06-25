In this Project I am going to use Python to automate things so that we don't have to do them manually. I am going to automate 2 use cases:

1) I will write a Python program that takes any blog article or any web page and it extracts all the headers from that page or article and then it translates all those headers to Spanish and saves it into its own HTML file so I can open it in the browser and basically see all the headers of that specific blog article translated in Spanish.
2) I am going to write a Python program that goes through all the files in our downloads folder it then checks if I have any files that are older than 30 days or were last used more than 30 days ago and it takes all these files and puts that into a new folder called "to_delete" which we can then review and basically delete if needed. So basically it helps us clean up our messy downloads folder with a bunch of old downloaded files in there.

But here's even more interesting thing I will do .I will use an artificial intelligence tool called ChatGPT and I will tell Python to use ChatGPT's API or the underlying API that ChatGPT is also using to generate the Python scripts for those two use cases that I mentioned.


So, basically I am going to write a python program that will accept an input from us about the automation use cases and then go to Chatgpt and say give me a python script this automation usecase and then I will save it into a seperate python file.

Why to use Python for automation ?
=>There are so many programming languages out there and they all seem to be doing the same thing.So what is there in Python that gives it the monopoly on automation ?
1) Large ecosystem of Python libraries for automation
2) Simple ,flexible and easy to learn language-It happened that most low level automation tools were written in python.These libraries can talk to the  server operating system, to cloud platforms allowing configuring infrastructure , networking  ,accessing various api(s) and this may be a small stand alone library or a complex automation tool like Ansible which also have this re-written with python.
3) Every language is good for a specific task and is best in it like python for autoamtion, javascript for web-development, etc.

First I write a python program to connect to an api (chatgpt api-technically an openAI api-which the chatgpt uses underneath).Chatgpt uses OpenAI's powerful models, but has been further fine-tuned
OpenAI provides API to access their pre-trained AI models.Using this API , developers can connect and easily integrate AI capabilities into their own apps and scripts that drives and powers Chatgpt for example and many startups and developers actualluy use this api to build some cool new tools.

How do we connect to the openAI api in general regardless of what programming language we are using?
=>First of all I need to Create an account on OpenAI platform.This way I am kind of creating my own space on openAI for my user and one of the reasons that I have to sign up is that the compute resources needed and the processing that takes place by AI in background needs some compute resources and processing power.So, obviously they cannot provide this limitless.So, they have limit for users so that everyone can access them and use it for free.
=>Then create an API Key -unique key for my user account used for authentication
   "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"


OpenAI has a library for python and nodejs for eg. and i can see the usage of the library for each language and its called the openAI.So I can install OpenAI library and import it in my code and use it.I can see the syntax and how to use the library in official documentation of that specific tool like what 
methods or objects I have available and so on and this will be more useful if i am doing more complex things or making more complex queries to the API and I 
want the libraries to do those things without overcomplicating my code.

OpenAI is pretty recent so they are continously adding things in their libraries, so their syntaxes and methods might change.So,I am going to stick to the generic requests library in this project.

In the first usecase, when I will open my output.tf file, i will see the headers of the blog only and that also in spanish.

Blog link - " https://www.techworld-with-nana.com/post/a-guide-of-how-to-get-started-in-it-in-2023-top-it-career-paths "

BeautifulSoup library: " https://www.crummy.com/software/BeautifulSoup/bs4/doc/ "

OpenAI API: " https://platform.openai.com/docs/introduction/overview "

Requests Python library: " https://www.crummy.com/software/BeautifulSoup/bs4/doc/ "