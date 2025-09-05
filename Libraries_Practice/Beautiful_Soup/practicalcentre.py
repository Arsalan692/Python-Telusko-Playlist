import requests
from bs4 import BeautifulSoup

req_pc = requests.get("http://practicalcentre.blogspot.com/2017/03/work-power-and-energy-questions-and-answers-physics-xi.html")
con_pc = req_pc.content
soup = BeautifulSoup(con_pc, "html.parser")
links = soup.find(id="bigimages").find_all("img")
for i in links:
    if "questions-and-answers" in i["src"]:
        print(i["src"])









