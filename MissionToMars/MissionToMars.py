#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import time
from pprint import pprint 


# In[2]:


#chromedriver
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html
#create soup object and use beautiful soup to parse html. 
soup = BeautifulSoup(html, 'html.parser')


# In[4]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[5]:


news_title = soup.find('div', class_='content_title').text
print("The news title of the day is " + news_title)

news_para = soup.find('div', class_='article_teaser_body').text
print("The news body is " + news_para)


# In[6]:


mars_mission_dict=dict()


# In[7]:


#chromedriver
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[23]:


#JPL Mars Space Images
time.sleep(15)
url_2='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


# In[26]:


results = soup_2.find_all('a',id="full_image")
print(results)


# In[25]:


#browser.click_link_by_partial_text('FULL IMAGE')


# In[20]:


#browser.click_link_by_partial_text('more info')


# In[27]:


html_2 = browser.html
soup_2 = BeautifulSoup(html_2, 'html.parser')


# In[28]:


pic=soup_2.find('figure', class_='lede').a['href']
featured_image_url=f'https://www.jpl.nasa.gov{pic}'
featured_image_url


# In[29]:


#Mars Weather


# In[31]:


#Mars Weather, return most recent
url_3='https://twitter.com/marswxreport?lang=en'
browser.visit(url_3)
html_3 = browser.html
soup3 = BeautifulSoup(html_3, 'html.parser')
mars_weather = soup3.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)


# In[32]:


#Mars Facts
url_facts='https://space-facts.com/mars/'
res = requests.get(url_facts)
soup = BeautifulSoup(res.content,'html')
table = soup.find_all('table',id='tablepress-p-mars')[0]
df = pd.read_html(str(table))[0]
df.head()


# In[33]:



mars_facts=df.rename(columns={0:"Mars",1:"Planet Profile"})
mars_facts


# In[34]:


#Convert to HTML Table
mars_html_table =mars_facts.to_html()


mars_html_table


# In[35]:


mars_html_table.replace('\n', '')


# In[36]:


#saved to html for later
mars_facts.to_html('mars_facts.html')


# In[37]:


#Mars Hemispheres
url_hemis='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url_hemis)
time.sleep(10)
html_5 = browser.html
soup_5 = BeautifulSoup(html_5, "html.parser")


# In[38]:


hemi_results=soup_5.find('div', class_="collapsible results")
hemis_items = hemi_results.find_all('div',class_='item')
print(hemis_items)


# In[39]:


hemis_img_urls_list=list()
img_urls_list = list()
title_list = list()
for h in hemis_items:
    #save title
    hemis_title = h.h3.text
    title_list.append(hemis_title)
    
    # find the href link.
    h_href  = "https://astrogeology.usgs.gov" + h.find('a',class_='itemLink product-item')['href']
    
    #print(h_title,h_href)
    
    #browse the link from each page
    browser.visit(h_href)
    time.sleep(5)
    #Retrieve the  image links and store in a list. 
    html5   = browser.html
    soup_img = BeautifulSoup(html5, 'html.parser')
    h_img_url = soup_img.find('div', class_='downloads').find('li').a['href']
    print("h_img_url" + h_img_url)
    img_urls_list.append(h_img_url)
    
    # create a dictionary with  each image and title and append to a list. 
    hemispheres_dict = dict()
    hemispheres_dict['title'] = hemis_title
    hemispheres_dict['img_url'] = h_img_url
    
    hemis_img_urls_list.append(hemispheres_dict)
    
print(hemis_img_urls_list)
print(title_list)
print(img_urls_list)


# In[40]:


mars_mission_dict["Mars_news_title"] = news_title
mars_mission_dict["Mars_news_para"] = news_para
mars_mission_dict["Mars_featured_image_url"] = featured_image_url
mars_mission_dict["Mars_html_table"] = mars_html_table
mars_mission_dict["Mars_HemIimage_urls"] = hemis_img_urls_list
pprint(mars_mission_dict)


# In[ ]:


get_ipython().system('pip install ipython')
get_ipython().system('pip install nbconvert')


# In[ ]:


ipython nbconvert--to script MissionToMars.ipynb


# In[ ]:




