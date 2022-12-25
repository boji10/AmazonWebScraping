#!/usr/bin/env python
# coding: utf-8

# In[6]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[5]:


# Connect to Website and pull in data

URL = 'https://www.amazon.ca/Witty-Fashions-Cassette-T-Shirt-Charcoal/dp/B07M9H9DDQ/ref=sr_1_15?keywords=data%2Banalyst%2Btshirt&qid=1672008396&sr=8-15'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

print(title)
print(price)












# In[ ]:


# Clean up the data a little bit

price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[ ]:


# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today()

print(today)


# In[ ]:


# Create CSV and write headers and data into the file

import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:


#Now we are appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


#Combine all of the above code into one function


def check_price():
    URL = 'https://www.amazon.ca/Witty-Fashions-Cassette-T-Shirt-Charcoal/dp/B07M9H9DDQ/ref=sr_1_15?keywords=data%2Banalyst%2Btshirt&qid=1672008396&sr=8-15'

    

    page = requests.get(URL)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='priceblock_ourprice').get_text()

    price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
 


# In[ ]:


# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'AmazonWebScraperDataset.csv')

print(df)


# In[ ]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('bjumagiliyage@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Bojitha, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! "
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'bjumagiliyage@gmail.com',
        msg
     
    )

