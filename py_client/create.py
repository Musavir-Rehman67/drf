import requests

headers = {
    'Authorization': 'Bearer ae8e5c31f9a7023c26518716570ff2df3d6e54a5'
}

endpoint = "http://localhost:8000/api/products/" 

data = {
    "title":"This field is done",
    "price":32.99
}

get_response = requests.post(endpoint,json=data,headers=headers)
print(get_response.json())