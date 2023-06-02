# -*- coding: utf-8 -*-
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import asyncio
import discord
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
TOKEN = os.environ.get('ACCESS_TOKEN')
streets = []
areas = []
prices = []
availables = []
links = []
images = []
sent_reqs = []
import_csv = pd.read_csv("save.csv")
import_csv.head()
while True:

    def djAlex():
        driver.get('''https://www.djalexander.co.uk/property/to-rent/in-glasgow-/below-1250/''')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
        time.sleep(1)
        driver.execute_script(
            "window.scrollTo(3, document.body.scrollHeight/3*2);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(3, document.body.scrollHeight);")
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        for a in soup.findAll('div', attrs={'class': 'w-grid-item-h'}):
            street = a.find('h3', attrs={'class': 'usg_post_custom_field_1'}).find(
                'span', attrs={'class': 'w-post-elm-value'}).text
            area = a.find('h3', attrs={'class': 'usg_post_custom_field_8'}).find(
                'span', attrs={'class': 'w-post-elm-value'}).text
            available = a.find('h6', attrs={'class': 'available_from'}).find(
                'span', attrs={'class': 'w-post-elm-value'}).text
            price = a.find('h2', attrs={'class': 'tag-property-price'}).find('span', attrs={'class': 'w-post-elm-value'}).text
            link = a.find('a')['href']
            image =a.find('img', attrs={'class': 'attachment-us_600_400'})['src']
            streets.append(street)
            areas.append(area)
            availables.append(available)
            prices.append(price)
            images.append(image)
            links.append(link)
            sent_reqs.append(link)


    def rightMove():
        driver.get('''https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=USERDEFINEDAREA%5E%7B%22polylines%22%3A%22wo%60tIjraY%3FjtDb%5DtdAvu%40oFrt%40wv%40ph%40ybBaEwrGwf%40kb%40qk%40mEwl%40jp%40%7BXbkAaQ%60gB%22%7D&maxPrice=1200&sortType=2&propertyTypes=&mustHave=&dontShow=&furnishTypes=&keywords=''')
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        for a in soup.findAll('div', attrs={'class': 'l-searchResult'}):
            addr = a.find('address', attrs={'class': 'propertyCard-address'}).text
            street = addr.split(',')[0]
            area = ' '.join(addr.split(',')[1:])
            available = a.find(
                'span', attrs={'class': 'propertyCard-branchSummary-addedOrReduced'}).text
            price = a.find('span', attrs={'class': 'propertyCard-priceValue'}).text
            link = '''https://www.rightmove.co.uk''' + \
                a.find('a', attrs={'class': 'propertyCard-priceLink'})['href']
            image = a.find('div', attrs={'class': 'propertyCard-img'}).find('img')['src']
            streets.append(street)
            areas.append(area)
            availables.append(available)
            prices.append(price)
            images.append(image)
            links.append(link)
            sent_reqs.append(link)


    def zoopla():
        driver.get('''https://www.zoopla.co.uk/to-rent/property/glasgow/?polyenc=sp%7BsI%7Cd%7DXsSab%40ca%40iNah%40hY%7D%5E~cAmm%40fhCy_%40x%60Dvd%40vnBzXrm%40tRnEzO%60Hd%5CD~FcUdHwOnNoKvOmPpLePnJee%40~M%7Dr%40%60K_hAjD%7Do%40ScsAuO_%7CA&price_frequency=per_month&price_max=1250&q=Glasgow&radius=0&results_sort=newest_listings&search_source=to-rent''')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
        time.sleep(1)
        driver.execute_script(
            "window.scrollTo(3, document.body.scrollHeight/4*2);")
        time.sleep(1)
        driver.execute_script(
            "window.scrollTo(3, document.body.scrollHeight/4*3);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(3, document.body.scrollHeight);")
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        for a in soup.findAll('div', attrs={'class': 'f0xnzq2'}):
            addr = a.find('h3', attrs={'class': '_1ankud52'}).text
            street = addr.split(',')[0]
            area = ' '.join(addr.split(',')[1:])
            available = a.findAll(
                'li', attrs={'class': '_18cib8e1'})[1]
            if available:
                available = available.text
            price = a.find(
                'p', attrs={'data-testid': 'listing-price'}).text
            link = '''https://www.zoopla.co.uk''' + \
                a.find('a', attrs={'class': '_1maljyt1'})['href']
            image = a.findAll('img', attrs={'class': 'fjzuu03'})[2]['src']
            streets.append(street)
            areas.append(area)
            availables.append(available)
            prices.append(price)
            images.append(image)
            links.append(link)
            sent_reqs.append(link)
        


    def onTheMarket():
        driver.get('''https://www.onthemarket.com/to-rent/property/glasgow/?max-price=1250&view=grid''')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
        time.sleep(1)
        driver.execute_script(
            "window.scrollTo(3, document.body.scrollHeight/4*2);")
        time.sleep(1)
        driver.execute_script(
            "window.scrollTo(3, document.body.scrollHeight/4*3);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(3, document.body.scrollHeight);")
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        for a in soup.findAll('li', attrs={'class': 'otm-PropertyCard'}):
            addr = a.find('span', attrs={'class': 'address'}).text
            street = addr.split(',')[0]
            area = ' '.join(addr.split(',')[1:])
            available = "No Info"
            price = a.find('div', attrs={'class': 'otm-Price'}).text
            link = '''https://www.onthemarket.com''' + \
                a.find('div', attrs={'class': 'otm-PropertyCardMedia'}).find('a')['href']
            imageR = a.find(
                'div', attrs={'class': 'swiper-slide swiper-slide-active'})
            if imageR:
                image = imageR.find('img')['src']
            else:
                image = None
            streets.append(street)
            areas.append(area)
            availables.append(available)
            prices.append(price)
            images.append(image)
            links.append(link)
            sent_reqs.append(link)

    def openRent():
        driver.get('''https://www.openrent.co.uk/properties-to-rent/glasgow-city?term=Glasgow%20City&area=5&prices_max=1200''')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
        time.sleep(1)
        driver.execute_script(
            "window.scrollTo(3, document.body.scrollHeight/3*2);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(3, document.body.scrollHeight);")
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        for a in soup.find('div', attrs={'class': 'property-list'}).findAll('a', attrs={'class': 'pli'}):
            addr = a.find('span', attrs={'class': 'listing-title'}).text
            street = ' '.join(addr.split(',')[1:])
            area = addr.split(',')[0]
            available =  "Now"
            price = a.find('div', attrs={'class': 'pl-title'}).find('h2').text
            if 'Let' in price:
                continue
            link = '''https://www.openrent.co.uk''' + \
                a['href']
            imageR = a.find(
                'img', attrs={'class': 'propertyPic'})
            if imageR:
                image = "https:" + imageR['src']
            else:
                image = None
            streets.append(street)
            areas.append(area)
            availables.append(available)
            prices.append(price)
            images.append(image)
            links.append(link)
            sent_reqs.append(link)

    def clyde():
        driver.get('''https://www.clydeproperty.co.uk/properties/?search-type%5B%5D=rent&location_or_postcode=glasgow&latitude=&longitude=&bound_value=&place_type=&text_input=&search_expanded=1&branch=&cmdSearchProperty=&distance=&bedroom_min=&bedroom_max=&property_search_type=&rent_price_min=&rent_price_max=1000''')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
        time.sleep(1)
        driver.execute_script(
            "window.scrollTo(3, document.body.scrollHeight/3*2);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(3, document.body.scrollHeight);")
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        for a in soup.find('div', attrs={'class': 'clyde-listings-grid'}).findAll('div', attrs={'class': 'listing-grid-column'}):
            if len(a['class']) > 1:
                continue
            addr = a.find('h3', attrs={'class': 'listing-grid-title'}).findAll('a')[0]['title']
            street = addr.split(',')[0]
            area = ' '.join(addr.split(',')[2:]).strip()
            available =  "Now"
            price = "£" + a.find('div', attrs={'class': 'listing-grid-price'}).text.split("£")[1].strip()
            isLet = a.find("div", attrs={'class': 'ribbon--let-agreed'})
            if isLet and ('Let' in isLet.text):
                continue
            link = a.find("div", attrs={'class': 'listing-grid-image'}).find('a')['href']
            imageR = a.find("div", attrs={'class': 'listing-grid-image'}).find('img')["src"]
            if imageR:
                image = imageR
            else:
                image = None
            streets.append(street)
            areas.append(area)
            availables.append(available)
            prices.append(price)
            images.append(image)
            links.append(link)
            sent_reqs.append(link)

    rightMove()
    zoopla()
    onTheMarket()
    openRent()
    clyde()
    strings = []
    times = [time.strftime("%H:%M %Y/%m/%d")] * len(availables)
    df = pd.DataFrame({"Req": sent_reqs, "Street": streets, "Area": areas, "Price": prices, "Available": availables, "Link": links, "Added":  times, "Image": images})
    n_df = []
    for l, v in df.iterrows():
        if v["Link"] in import_csv.values:
            val = import_csv.loc[import_csv['Link'] == v["Link"]].values.tolist()[0][1:]
            old_date = datetime.strptime(val[6], "%H:%M %Y/%m/%d")
            current = datetime.now()
            if (current - old_date).seconds > 14400 or (current - old_date).days != 0:
                val[0] = ""
            else:
                val[0] = "TRUE"
            n_df.append(val)
        else:
            v["Req"] = "TRUE"
            n_df.append(v.values.tolist())
            string = " Found: {5}\n{0}, {1}\n Price: {2}\n Available From: {3}\n{4}".format(*[v['Street'],v['Area'],v['Price'],v['Available'],v['Link'],v['Added']])
            strings.append(string)
    n_df = pd.DataFrame(n_df, columns=import_csv.columns.values.tolist()[1:])
    with open('out.html', 'w') as fo:
        fo.write(n_df.to_html(render_links=True, escape=False))
    n_df.to_csv("save.csv")
    driver.close()
    # with open("src/out.js",'w') as fo:
    #     fo.write("export const data = { 0: \"" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\" }")
    if len(strings) > 0:
        client = discord.Client()
        @asyncio.coroutine
        def on_ready():
            channel = client.get_channel(1009529852728197274)
            for j in strings:
                yield from channel.send(j)
            yield from client.close()
        client.run(TOKEN)
    print("Checked for flats")
    time.sleep(300)