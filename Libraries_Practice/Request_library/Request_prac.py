import requests

payload = {"firstname": "Arsalan", "lastname": "Ahmed"}
req = requests.get("https://httpbin.org/get?",params=payload)
print(req.content)






