import requests

from bs4 import BeautifulSoup


def email_giver():
    pass


def name_giver():
    payload = {"pg": 1}
    count = 1
    for j in range(1, 104):
        res = requests.get("https://www.businesstravelnews.com/Hotels/Rome", params=payload)
        con = res.content

        soup1 = BeautifulSoup(con, "html.parser")
        tag1 = soup1.findAll(class_="namelink")

        for i in tag1:
            print(f"Hotel {count}: {i.string}")
            count += 1

        payload["pg"] += 1


