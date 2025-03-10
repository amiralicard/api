from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_bitcoin_price():
    url = 'https://nobitex.ir/btc/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.find(class_="text-headline-medium text-txt-neutral-default dark:text-txt-neutral-default desktop:text-headline-large")
        if price_tag:
            return price_tag.get_text(strip=True)
    return "خطا در دریافت قیمت"

def get_tether_price():
    url = 'https://nobitex.ir/usdt/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.find(class_="text-headline-medium text-txt-neutral-default dark:text-txt-neutral-default desktop:text-headline-large")
        if price_tag:
            return price_tag.get_text(strip=True)
    return "خطا در دریافت قیمت"

def get_gold_price():
    url = 'https://www.tgju.org/profile/geram18'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.find(class_="value")
        if price_tag:
            return price_tag.get_text(strip=True)
    return "خطا در دریافت قیمت"

def get_dolor_price():
    url = 'https://www.tgju.org/profile/price_dollar_rl'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.find(class_="value")
        if price_tag:
            return price_tag.get_text(strip=True)
    return "خطا در دریافت قیمت"

def get_azan():
    url = 'https://badesaba.ir/owghat/284/%D8%AA%D9%87%D8%B1%D8%A7%D9%86'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.find(class_="time-remaining text-start")
        if price_tag:
            return price_tag.get_text(strip=True)
    return "خطا در دریافت قیمت"

@app.route('/')
def home():
    bitcoin_price = get_bitcoin_price()
    tether_price = get_tether_price()
    gold_price = get_gold_price()
    dolor_price = get_dolor_price()
    azan = get_azan()
    return render_template('index.html', bitcoinprice=bitcoin_price, teterprice=tether_price, goldprice=gold_price, dolorprice=dolor_price, azan=azan)

if __name__ == '__main__':
    app.run(debug=True)
