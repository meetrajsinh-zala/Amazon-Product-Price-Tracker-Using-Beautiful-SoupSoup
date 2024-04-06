import requests
import bs4
from datetime import datetime
import sqlite3
from re import search

now = datetime.now()

base_url = 'https://www.amazon.in'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

base_response = requests.get(base_url, headers=headers)
cookies = base_response.cookies

def create_table():
    conn = sqlite3.connect('amztracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS prices(asin TEXT, title TEXT, price FLOAT, img_url TEXT, rating TEXT, date DATE)''')
    return conn

def get_product_price(soup):
    price_lines = soup.find(class_='a-price-whole')
    final_price = str(price_lines)
    final_price = final_price.replace('<span class="a-price-whole">','')
    final_price = final_price.replace('<span class="a-price-decimal">.</span>','')
    final_price = final_price.replace('</span>','')
    final_price = final_price.replace(',','')
    if(final_price != 'None'):
        return int(final_price)
    else:
        return False

def get_product_title(soup):
    product_title = soup.find(id='productTitle')
    product_title = str(product_title)
    product_title = product_title.replace('<span class="a-size-large product-title-word-break" id="productTitle">','')
    product_title = product_title.replace('</span>','')
    if(product_title != 'None'):
        return product_title.strip()
    else:
        return False

def get_product_rating(soup):
    product_ratings = soup.findAll(class_='a-icon-alt')
    if(product_ratings):
        product_ratings = str(product_ratings[0])
        product_ratings = product_ratings.replace('<span class="a-icon-alt">','')
        product_ratings = product_ratings.replace('</span>','')
        return product_ratings.strip()
    else:
        return False

def get_product_image(soup):
    product_image = soup.find(id='imgTagWrapperId').find(id='landingImage')['src']
    if(product_image != 'None'):
        return product_image
    else:
        return False
    
def get_product_asin(soup):
    product_asin = soup.find(id="productDetails_detailBullets_sections1")
    if(product_asin):
        product_asin = product_asin.find(class_ = 'a-size-base prodDetAttrValue')
        product_asin = str(product_asin) 
        product_asin = product_asin.replace('<td class="a-size-base prodDetAttrValue">','')
        product_asin = product_asin.replace('</td>','')
        return product_asin.strip()
    else:
        return False
    
def fatch_product_url(search_query):
    Product_Url = []
    Base_Url = 'https://www.amazon.in/s?k='
    product_page = requests.get(Base_Url+search_query,headers=headers,cookies=cookies)
    soup = bs4.BeautifulSoup(product_page.text,'lxml')
    all_product = soup.find(class_='s-result-list').find_all(class_='a-link-normal s-no-outline')
    for prod in range(len(all_product)):
        Product_Url.append(all_product[prod]['href'])
        print(Product_Url)
    return Product_Url

def fatch_product_detils(Search_Query):
    conn = create_table()
    c = conn.cursor()
    url = 'https://www.amazon.in/'
    Product_Url = fatch_product_url(Search_Query)
    dummy_query = Search_Query.split()
    for prod in Product_Url:
        if(prod.startswith('https://aax-eu.amazon.in/')):
            product_response = requests.get(prod,headers=headers,cookies=cookies)
        else:
            product_response = requests.get(url+prod,headers=headers,cookies=cookies)
        soup = bs4.BeautifulSoup(product_response.text, 'lxml')
        price = get_product_price(soup)
        title = get_product_title(soup)
        rating = get_product_rating(soup)
        image = get_product_image(soup)
        asin = get_product_asin(soup)
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        if(asin and price and title and rating and image):
            Match_keyword = []
            for Keyword in dummy_query:
                temp = title.lower()
                if(search(Keyword.lower(),temp)):
                    Match_keyword.append(True)
                else:
                    Match_keyword.append(False)
            if(sum(Match_keyword) == len(dummy_query)):
                print(Match_keyword)
                c.execute('''INSERT INTO prices VALUES(?,?,?,?,?,?)''',(asin,title,price,image,rating,date_time))
                print(f'Added Data For {asin} => {title} => Rs {price}')
                print()

    conn.commit()
    print('Committed New Entries To Database')

def auto_scrapper():
    Data = set()
    url = 'http://www.amazon.in/dp/'
    conn = create_table()
    c = conn.cursor()
    c.execute('''SELECT asin FROM prices''')
    asins = c.fetchall()
    for asin in asins:
        Data.add(asin[0])
    
    asins = list(Data)
    for asin in asins:
        product_response = requests.get(url+asin,headers=headers,cookies=cookies)
        soup = bs4.BeautifulSoup(product_response.text, 'lxml')
        price = get_product_price(soup)
        title = get_product_title(soup)
        rating = get_product_rating(soup)
        image = get_product_image(soup)
        asin_ = get_product_asin(soup)
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        if(asin and price and title and rating and image):
            c.execute('''INSERT INTO prices VALUES(?,?,?,?,?,?)''',(asin_,title,price,image,rating,date_time))
            print(f'Added Data For {asin} => {title} => Rs {price}')

    conn.commit()
    print('Committed New Entries To Database')