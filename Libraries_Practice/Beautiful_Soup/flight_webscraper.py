import requests
from bs4 import BeautifulSoup

count = 1
payload = {"pg": 1}
for j in range(1, 104):

    res = requests.get("https://www.businesstravelnews.com/Hotels/Rome", params=payload)
    con = res.content

    soup = BeautifulSoup(con, "html.parser")
    for i in soup.findAll(class_="namelink"):
        href_val = i.get("href")
        full_link = f"https://www.businesstravelnews.com{href_val}"
        res2 = requests.get(full_link)
        html_content = res2.content
        soup2 = BeautifulSoup(html_content, "html.parser")
        name_of_hotel = soup2.find(class_="h1").string.strip()
        try:
            email_of_hotel = soup2.find(class_="__cf_email__").string
            print(f"Hotel {count}: {name_of_hotel}, Email: {email_of_hotel}")
        except AttributeError:
            print(f"Hotel {count}: {name_of_hotel}, Email: Not given")
        count += 1

    payload["pg"] += 1













