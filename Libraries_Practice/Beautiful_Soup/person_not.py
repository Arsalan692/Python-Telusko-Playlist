import requests
from bs4 import BeautifulSoup

req = requests.get("https://thispersondoesnotexist.com/image")
con = req.content
print(con)

