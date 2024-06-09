from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.quintoandar.com.br/comprar/imovel/sao-paulo-sp-brasil"

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

houses = soup.find_all('div', attrs={"data-testid": "house-card-details"})
print(len(houses))