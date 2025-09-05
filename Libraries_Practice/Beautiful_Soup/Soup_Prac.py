import requests
from bs4 import BeautifulSoup


# Step 1: Get the HTML
# res = requests.get("https://www.movieswatch24.pk")
# web_content = res.content
#
# # Step 2: Parse the HTML
# soup = BeautifulSoup(web_content, "html.parser")
# soup.prettify()
# # print(type(soup))
# print(type(soup.title.string))
# # Get the title of page
# print(type(soup.title))

# Get all the anchor tag
# anchors = soup.find_all("a")
# for i in anchors:
#     print(i)

# Get all the paragraph tag
# paras = soup.find_all("p")
# for i in paras:
#     print(i)

# Find the first tag of anchor
# anchor = soup.find("a")
# print(anchor)

# Find the first tag of para
# para = soup.find("p")
# print(para)

# Find all the elements with class lead
# print(soup.find("p", class_='lead'))

# Get the text in a paragraph
# print(soup.find("p").get_text())

# Get the links in a page
# anchors = soup.find_all("a")
# all_links = set()
# for i in anchors:
#     all_links.add(i.get("href"))
# for j in all_links:
#     if "https://" in j:
#         print(j)
#     else:
#         print(f"https://www.movieswatch24.pk{j}")


# Get the comment type
s_code = "<p><!-- This is a comment --><p/>"
soup2 = BeautifulSoup(s_code, "lxml")
print(type(soup2.p.string))

















