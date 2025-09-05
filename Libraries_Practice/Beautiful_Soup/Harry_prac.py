
import requests
from bs4 import BeautifulSoup

url = "https://parhlefailhojayega.ga"
r = requests.get(url)
code = r.content

soup = BeautifulSoup(code, "html.parser")
elem = soup.select("#sidebar-widgets")
print(elem)











