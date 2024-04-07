from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
from datetime import datetime
from pymongo import MongoClient


urls = []

with open(f"./product_asins.txt", "r", encoding="utf-8") as file:
    content = file.readlines()
    urls.extend(content)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

client = MongoClient()
db = client.amazon_price


def fetch_Data():
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Can remove this argument for the browser to pop up
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument("--user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4")
    driver = webdriver.Chrome(options=chrome_options)
    i = 0
    for url in urls:
        driver.get(url) 
        pg_source = driver.page_source 
        with open(f'html_pages/{i}.html', 'w', encoding='utf-8') as f:
            f.write(pg_source)    
        i += 1

def scrape_Data ():
    html_files = os.listdir('html_pages')
    for file_name in html_files:
        with open(os.path.join('html_pages', file_name), 'r', encoding='utf-8') as f:
            html_content = f.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            table = soup.find(id='productDetails_detailBullets_sections1')
            asin = table.find(class_ = 'a-size-base prodDetAttrValue').get_text().strip()
            price = (soup.find(class_='a-price-whole').get_text()).replace('.','').replace(',','')
            title = (soup.find(class_='a-size-large product-title-word-break').get_text().strip()).split('(')[0]
            date_time = datetime.now()
            db.price.insert_one({'asin': asin, 'title': title, 'price': price, 'date_time': date_time})
            
            
       

if __name__ == "__main__":
    fetch_Data() # --> This function needs to be executed only when you want to get the data again for the next day.
    scrape_Data()

