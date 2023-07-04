import requests
response= requests.get("https://229d-83-120-58-38.ngrok-free.app/")
print(response.status_code,response.json(),sep="\n")