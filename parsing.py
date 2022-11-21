

import requests
from bs4 import BeautifulSoup
import csv

def write_to_csv(data):
    with open('data.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'],data['price'],data['image']])
    

def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_page(html):
    soup = BeautifulSoup(html,'lxml')
    lastpage = soup.find('div',class_='pager-wrap').find('ul',class_="pagination pagination-sm").find_all('li')
    lastpage = lastpage[-1].text
    print(lastpage)
    return int(lastpage)
    
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find('div', class_='list-view').find_all('div',class_='item')
    
    for product in product_list:
        title = product.find('div', class_='listbox_title oh').find('strong').text
   

        price = product.find('div', class_='listbox_price text-center').find('strong').text
  

        image = product.find('img').get('src')
        image = 'https://www.kivano.kg/'+image
        
        dict_ = {'title':title, 'price':price, 'image': image}
        write_to_csv(dict_)
        
   

def main():
    nb_url = 'https://www.kivano.kg/noutbuki'
    pages = '?page='
    html  = get_html(nb_url)
    number = get_total_page(html)
    # get_data(html)
    for i in range(1,number+1):
        url_pages = nb_url + pages +str(i)
        print(url_pages)
        htmml = get_html(url_pages)
        get_data(htmml)
        
with open('data.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['title','price','image'])
    
main()


"""""EVR DATABASE"""
def write_to_csv(database):
    with open('EVR.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([database['title'],database['link'],database['image']])

def get_html(url):
    res = requests.get(url)
    return res.text

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    products = soup.find_all('div',class_="wrap")


    for p in products:
        title = p.find("span",class_="title").text.strip()
        
        
        link = p.find('a', href = True).get('href')
        if link.startswith('java'):
            pass
        else:
            link = 'https://rt.pornhub.com' + link
            
        image = p.find('img').get('src')
       
       
        dict_ = {'title':title,'link':link,'image':image}
        write_to_csv(dict_)
        



def main():
    url = 'https://rt.pornhub.com/gay/video/search?search=porn'
    html = get_html(url)
    database = get_data(html)
    for i in range(2,50):
        url = url + '&page=' + str(i)
        htmml = get_html(url)
        get_data(htmml)
    
    
   
with open('EVR.csv', 'w') as file:
     write = csv.writer(file)
     write.writerow(['title','price','image'])
    
    
main()


python3 -m venv venv - creates venv
. venv/bin/activate - activates venv
pip3 install -r req.txt

"""""CARS.KG"""""


def request(url):
    html = requests.get(url)
    return html.text

def data(html):
    soup = BeautifulSoup(html,"lxml")
    product = soup.find_all('a', class_="catalog-list-item")
    for i in product:
        try:
            title = i.find('span', class_='catalog-item-caption').text.strip()
            # print(title)
            
            price = i.find("span", class_="catalog-item-price").text.strip()
            # print(price)
            
            img = i.find('img').get('src')
        except:
            None
        # print(img)
        

        dict_ = {'title':title, "price":price, "image": img}
        write_to_csv(dict_)
        
def write_to_csv(database):
    with open('cars.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([database['title'],database['price'],database['image']])

def main():
    url = "https://cars.kg/offers"
    html = request(url)
    data(html)
    for i in range(2,20):
        url_new= f'{url}/{i}'
        html_new = request(url_new)
        data(html_new)
        print(i)
        
    

with open('cars.csv','w') as f:
    write = csv.writer(f)
    write.writerow(["car","price","image",])

main()