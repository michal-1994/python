from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen("https://michalgrzegorczyk.pl/")
html = response.read()
soup = BeautifulSoup(html, "html.parser")
titles_elem = soup\
    .find_all("h3")

for title in titles_elem:
    print(title.text)