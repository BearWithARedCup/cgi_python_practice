#! /usr/bin/python3
import os
import sys

# fname=Zachary&lname=Hargraves
def get_query_params(qstring):
    key_values = qstring.split("&")
    # ["fname=Zachary", "lname=Hargraves"] spliting at "&""
    params = {}
    for param in key_values:
        # fname=Zachary gonna loop through the first sting which is fname=Zachary
        k_v = param.split("=")
        # ["fname", "Zachary"] spilting at "=""
        params[k_v[0]] = k_v[1] 
        #storing into dictionary assigning {key : value}
    return params 
    #returning the dictionary


print("Content-type:text/plain\n\n")
# for k, v in os.environ.items():
#     print(k, v) #Prints all of the enviroment variables AKA important stuff :) (change Content-type:text/html to plain)
#REQUEST_METHOD GET | POST
if os.environ.get('REQUEST_METHOD') == 'POST':
    query = sys.stdin.read() #POST
elif os.environ.get('REQUEST_METHOD') == 'GET':
    query = os.environ.get("QUERY_STRING") or 'N/A'
else:
    print("Pound on some sand")


if query != 'N/A':
    params = get_query_params(query)
else:
    params = {'fname': 'john', 'lname' : 'doe'}


print("<html>")
print("<head>")
print("<title>Hello World - First CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hellow World! This is my first CGI program</h2>")
print(f"<p>{params['fname']}, {params['lname']}</p>")
print("</body>")
print("</html>")
