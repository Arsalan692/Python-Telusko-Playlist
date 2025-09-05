import requests
from bs4 import BeautifulSoup

user_input = input("Enter the word: ")
url = f"https://www.dictionary.com/browse/{user_input}"
r = requests.get(url)
if r.status_code == 404:
    print("Not Found")
    quit()
con = r.content

soup = BeautifulSoup(con, "html.parser")
str1 = soup.find(class_="one-click-content css-nnyc96 e1q3nk1v1")
print(f"{user_input.title()} meaning:\n\t{str1.get_text()}")






