import requests
from bs4 import BeautifulSoup

chapter_name = input("Enter chapter: ")
req1 = requests.get(f"https://adamjeecoaching.blogspot.com/search?q=[{chapter_name}] - Chapter Summary")
con = req1.content

soup = BeautifulSoup(con, "html.parser")
first_title_tag = soup.find(class_="post-title entry-title").a

blog_link = first_title_tag.get("href")

req2 = requests.get(blog_link)
con2 = req2.content
soup2 = BeautifulSoup(con2, "html.parser")
images = soup2.find_all("img")
for i in images:
    if "s1600" in i.get("src") and "MCQS.png" not in i.get("src"):
        print(f"https:{i.get('src')}")

