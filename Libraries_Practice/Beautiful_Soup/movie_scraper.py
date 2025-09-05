
import requests
from bs4 import BeautifulSoup

user_input = input("Enter the name of the movie: ").replace(" ", "-").strip()

req = requests.get(f"https://myflixer.to/search/{user_input}")
con = req.content

soup = BeautifulSoup(con, "html.parser")
film_name = soup.find(class_="film-name").get_text()

film_poster_img = soup.find(class_="film-poster-img lazyload").get("data-src")
movie_link = f'https://myflixer.to{soup.find(class_="film-name").find("a").get("href")}'











