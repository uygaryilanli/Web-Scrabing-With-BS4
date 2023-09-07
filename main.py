from bs4 import BeautifulSoup
import requests
import pandas as pd

items = []
links = []
prices = []

toplam_sayfa = 4

for page in range(1, toplam_sayfa + 1):
    response = requests.get(f"https://www.smokshop.org/index.php?route=product/category&path=59&page={page}").text

    soup = BeautifulSoup(response, "html.parser")

    get_items = soup.select("div .name")
    items.extend([item.getText() for item in get_items])

    get_links = soup.select("div .name a")
    links.extend([link.get("href") for link in get_links])

    get_price = soup.find_all(name="span", class_="price-normal")
    prices.extend([price.getText() for price in get_price])

df = pd.DataFrame({
    "Urun" : items,
    "Fiyat" : prices,
    "Link" : links
})

df.to_excel("elektronik_sigaralar.xlsx", index=False)