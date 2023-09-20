# import requests

# # # endpoint ="https://httpbin.org/status/200"
# # # endpoint = "https://httpbin.org/anything"
# # # endpoint = "http://127.0.0.1:8000/"
# endpoint = "http://localhost:8000/api/" 

# # # requests.get() #API-->
# get_response = requests.get(endpoint,params={"abc":123}, json={"query":"Hello World"}) #http request 
# # # get_response = requests.get(endpoint,data={"query":"Hello World"}) #http request 
# # print(type(get_response))
# # print(get_response.headers)
# # print(get_response.text)
# # print(get_response.text) #print raw text response
# # # print(get_response.status_code)



# # # HTTP Request ->HTML
# # # REST API HTTP Request -> JSON(xml)
# # #JavaScript Object Nototion ~ python Dict

# print(get_response.json())
# # # print(get_response.json()['message'])
# # # print(get_response.status_code)

import requests

endpoint = "http://localhost:8000/api/" 

get_response = requests.post(endpoint,params={"abc":123}, json={"title":"abc123","content":"Hello World","price":"abc134"}) #http request 

print(get_response.json())

