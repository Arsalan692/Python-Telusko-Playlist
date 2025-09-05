
import requests

from bs4 import BeautifulSoup
query = input("Enter exercise: ")
adam_req = requests.get(f"https://adamjeecoaching.blogspot.com/search?q={query} - Mathematics 11th")
con = adam_req.content

soup = BeautifulSoup(con, "html.parser")
first_title_tag = soup.find(class_="post-title entry-title").a
# print(f"Chapter: {first_title_tag.get_text().strip()}")
blog_link = first_title_tag.get("href")

adam_req2 = requests.get(blog_link)
con2 = adam_req2.content
soup2 = BeautifulSoup(con2, "html.parser")
images = soup2.find_all("img")
for i in images:
    if "s1600" in i.get("src") and "In The Blanks.png" not in i.get("src"):
        print(i.get("src"))





