import requests

endpoint = "http://localhost:8000/api/products/1289498588937584/" 

get_response = requests.get(endpoint)
print(get_response.json())