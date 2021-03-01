from bs4 import BeautifulSoup
import requests
from db import insert_jordan


my_data = []
html_text = requests.get('https://www.nike.com/fr/w/hommes-jordan-chaussures-37eefznik1zy7ok').text
soup = BeautifulSoup(html_text, 'lxml')
shoes = soup.find_all('div', class_ = "product-card css-p5gpvn css-z5nr6i css-11ziap1 css-zk7jxt css-dpr2cn product-grid__card")

for shoe in shoes:    
    shoe_img_noscript = shoe.find('noscript')
    shoe_img_src = shoe_img_noscript.find('img', class_ = 'css-1fxh5tw product-card__hero-image')['src']
    shoe_name = shoe.find('div', class_ = "product-card__title").text
    shoe_type = shoe.find('div', class_ = "product-card__subtitle").text
    shoe_color = shoe.find('div', class_ = "product-card__product-count").text
    shoe_price = shoe.find('div', class_ = "product-card__price").text[:-2].replace(',', '.')
    my_data.append((shoe_img_src, shoe_name, shoe_type, shoe_color, shoe_price))
    # print(f'''
    # Shoe image : {shoe_img_src},
    # Shoe name : {shoe_name}, 
    # Shoe type : {shoe_type}, 
    # Shoe number of color : {shoe_color}, 
    # Show price : {shoe_price}
    # ''')

print("shoes = ",my_data)

insert_jordan(my_data)