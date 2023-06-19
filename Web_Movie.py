from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text

movie_soup = BeautifulSoup(movies, "html.parser")
movies = movie_soup.find_all(name="h3", class_="title")
movie_list = [movie.getText() for movie in movies]
movie_list.reverse()

with open("movies.txt", "w", encoding="UTF8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
