import requests
r = requests.get("https://financialmodelingprep.com/api/v3/income-statement-as-reported/AAPL?apikey=demo")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)


''' 
What is HTTP?
HTTP stands for the 'Hypertext Transfer Protocol,'. It is a set of protocols that are designed to enable communication 
between clients and servers. Between clients and servers, it works as a request-response protocol. To request a response
from the server, we can request data from the server, or we can submit data to be processed to the server.

What Is Requests Module?
The response data depends on our type of request. The request module is not a built-in Python module; instead, we have 
to download it manually. Requests module is used to send all kinds of HTTP requests. It is also one of the most 
downloaded modules in Python because all the web related software and programs must have it in them.

Install Python Requests:-
To work with the requests module, the first step is to install the module in Python. To download a request module, we 
can run the code:

pip install requests

After that, we have to import our module into the program, the same as we import all other modules.

import requests

Built-in methods in the request module:-
There are a lot of built-in methods in request module, such as delete(), get(), Head(), put(), etc. We will see the 
working of the get() function in this tutorial in detail. 

get():
As from the name, we can detect that the get function returns us with some information about the site we requested. All 
the information is stored in the object we used to send the request. We can access different kinds of information through 
it, such as status, header, cookies, etc. To make a GET request, invoke

The basic syntax is:

requests.get(URL, params={key: value}, args)
URL: this is the URL of the website where we want to send the request. 

Params: this is a dictionary or a list of tuples used to send a query string. 

Args: It is optional. It can be any named arguments offered by the get method.

We can also fetch all the data from the homepage of a website into an HTML format using the request module. Few important
types of methods defined in the request module are as follows:

    1) put( ): It is used to send a put request to a variable. It is usually used to update or completely change the 
    resources of a specific URL.
    2) delete( ): Delete is used to delete the specific resource, specified by URL.
    3) head( ): The head method returns a header for a specific resource
    4) post( ): Post requests take with it the data to the server to update it with.
    5) patch( ): The patch is used to send patch requests. It is used to apply partial modifications to a resource. 
    It carries with it the instructions for the modification.
'''