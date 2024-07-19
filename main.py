from bs4 import BeautifulSoup
import requests

URL = ("https://appbrewery.github.io/instant_pot/")

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="aok-offscreen").getText()
float_price = float(price.replace(" $", ""))

print(type(float_price))


