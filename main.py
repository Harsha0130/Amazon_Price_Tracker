from bs4 import BeautifulSoup
import requests
import os
import smtplib

URL = ("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
EMAIL = os.environ["EMAIl"]
PASSWORD = os.environ["PASSWORD"]
TO_ADDRESS = os.environ["TO_ADDRESS"]

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


response = requests.get(url=URL, headers=header)

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
