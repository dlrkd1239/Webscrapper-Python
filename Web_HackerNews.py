# # Beautiful soup -> 파이썬 라이브러리. HTML, XML에서 데이터 추출하는데 씀.
from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get(url="https://news.ycombinator.com/news")

news = response.text

soup = BeautifulSoup(news, "html.parser")

titles = soup.find_all(name="span", class_="titleline")
titles_title = [title.getText() for title in titles]
titles_link = [title.find("a").get("href") for title in titles]
scores = soup.find_all(name="span", class_="score")
scores_score = [score.getText().split()[0] for score in scores]
index_max_score = scores_score.index(max(scores_score))

print(titles_title[index_max_score])
print(titles_link[index_max_score])
print(scores_score[index_max_score])


#
# with open("website.html", "rt", encoding="UTF8") as web:
#     content = web.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# print(soup.title.string)
# print(soup.title.name)
# print(soup.li) #첫번째 태그 하나만
# all_a_tags = soup.find_all(name="a")
# for a in all_a_tags:
#     print(a.get("href"))
#
# headone = soup.find(name="h1", id="name")
# head_three = soup.find(name="h3", class_="heading")
# print(headone)
# print(head_three.string)
#
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
