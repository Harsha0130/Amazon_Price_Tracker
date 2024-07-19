from bs4 import BeautifulSoup
import requests
import os
import smtplib

URL = ("https://appbrewery.github.io/instant_pot")
EMAIL = os.environ["EMAIl"]
PASSWORD = os.environ["PASSWORD"]
TO_ADDRESS = os.environ["TO_ADDRESS"]


response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="aok-offscreen").getText()
float_price = float(price.replace(" $", ""))

title = soup.find(name="span", id="productTitle")
title = ' '.join(title.getText().strip().split())

TARGET_PRICE = 100

if float_price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=TO_ADDRESS,
                            msg=f"Subject:Amazon Price Alert!\n\n{title} is now at {price}\nBuy it here: {URL}".encode("utf-8"))
