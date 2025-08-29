import requests

url = "http://127.0.0.1:5000/submit"

header = {"Content-Type":"application/json"}

response = requests.post(url, json = payload, headers = header)

print(response.status_code)
print(response.json())
