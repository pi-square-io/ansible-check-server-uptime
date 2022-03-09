# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 13:47:47 2022

@author: ahlem
"""
################################################################################
""" The import of the necessary libraries"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
###################################################################
"""Get the url and extract the content in which we choose the articles"""
url = "https://www.jumia.com.tn/catalog/?q=pc+gamer"
result = requests.get(url)
Content=BeautifulSoup(result.content,features="lxml")
data=Content.find_all('article')[4:44]
###################################################################
"""We create lists of all our features we want in our dataframe"""
name_article=[]
for i in range(len(data)):
    name_article.append((data[i].find_all('h3')[0]).text)
#print(name_article)
price=[]
for i in range(len(data)):
    if data[i].find_all('div', attrs={'class':'old'})==[]:
        price.append('None')
    else:
        price.append((data[i].find_all('div', attrs={'class':'old'})[0]).text)
#print(price)
##############################################################
promotion=[]
for i in range(len(data)):
    if data[i].find_all('div', attrs={'class':'prc'})==[]:
        promotion.append('None')
    else:
        promotion.append((data[i].find_all('div', attrs={'class':'prc'})[0]).text)
#print(promotion)
###############################################################
percentage_promotion=[]
for i in range(len(data)):
    if data[i].find_all('div', attrs={'class':'tag _dsct _sm'})==[]:
        percentage_promotion.append('None')
    else:
        percentage_promotion.append((data[i].find_all('div', attrs={'class':'tag _dsct _sm'})[0]).text)
#print(percentage_promotion)
###############################################################
rank=[]
for i in range(len(data)):
    if data[i].find_all('div', attrs={'class':'stars _s'})==[]:
        rank.append('None')
    else:
        rank.append((data[i].find_all('div', attrs={'class':'stars _s'})[0]).text)
#print(rank)
##################################################################
df=pd.DataFrame(columns=['name_article','prmotion','price','precentage_promotion','rank'])

for i in range(len(data)):
    name=name_article[i]
    pro=promotion[i]
    prix=price[i]
    percentage=percentage_promotion[i]
    ra=rank[i]
    df.loc[i]=[name,pro,prix,percentage,ra]
#print(df)
"""to create a csv file"""
df.to_csv('catalogue.csv',index=False)
