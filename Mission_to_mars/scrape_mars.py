#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pymongo
from pprint import pprint
import pandas as pd


# NASA Mars News

# In[2]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = ('https://mars.nasa.gov/news/')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


# In[4]:


print(soup.prettify())


# In[5]:


news_title = soup.find("div",class_="content_title").text
news_paragraph = soup.find("div", class_="rollover_description_inner").text
print(f"News Title: {news_title}")
print(f"News Paragraph: {news_paragraph}")


# JPL Mars Space Images - Featured Image

# In[6]:


jpl_image_url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

jpl_image_response = requests.get(jpl_image_url)
jpl_image_soup = BeautifulSoup(jpl_image_response.text, 'html.parser')


# In[7]:


print(jpl_image_soup.prettify())


# In[8]:


image = soup.find('a',class_="button fancybox")
print(image)


# In[9]:


pic = image['data-fancybox-href']

featured_image_url = 'https://www.jpl.nasa.gov' + pic
featured_image_url


# Mars Weather

# In[10]:


weather_url = ('https://twitter.com/marswxreport?lang=en')

weather_response = requests.get(weather_url)
weather_soup = BeautifulSoup(weather_response.text, 'html.parser')


# In[11]:


print(weather_soup.prettify())


# In[12]:


weather_tweet = weather_soup.find_all('div', class_ = "js-tweet-text-container")
print(weather_tweet)


# In[13]:


mars_weather_tweet = weather_soup.find_all('div', class_ = "js-tweet-text-container")


# In[14]:


for tweet in mars_weather_tweet:
    if tweet.text.strip().startswith('InSight'):
        mars_weather = tweet.text.strip()


# In[15]:


print(mars_weather)


# Mars Facts

# In[16]:


mars_facts_url = 'https://space-facts.com/mars/'

facts_response = requests.get(mars_facts_url)
facts_soup = BeautifulSoup(facts_response.text, 'html.parser')


# In[17]:


print(facts_soup.prettify())


# In[18]:


mars_facts_df = pd.read_html(mars_facts_url)
mars_facts_df = (mars_facts_df[0])


# In[19]:


mars_facts_df.columns = ["Description", "Value"]
mars_facts_df


# In[22]:


mars_facts_df = mars_facts_df.to_html(classes='mars')
facts_table_data = mars_facts_df.replace('\n', ' ')
facts_table_data


# Mars Hemispheres

# In[23]:


cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

cerberus_response = requests.get(cerberus_url)
cerberus_soup = BeautifulSoup(cerberus_response.text, 'html.parser')


# In[24]:


print(cerberus_soup.prettify())


# In[25]:


cerberus_image = cerberus_soup.find_all('div', class_="wide-image-wrapper")
print(cerberus_image)


# In[45]:


hemisphere_image_urls = []


# In[29]:


for image in cerberus_image:
    pic = image.find('li')
    full_res_image = pic.find('a')['href']
cerberus_title = "Cerberus Hemisphere"
cerberus_hem = {"Title": cerberus_title, "url": full_res_image}
print(cerberus_hem)


# In[30]:


schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

schiaparelli_response = requests.get(schiaparelli_url)
schiaparelli_soup = BeautifulSoup(schiaparelli_response.text, 'html.parser')


# In[32]:


schiaparelli_image = schiaparelli_soup.find_all('div', class_="wide-image-wrapper")
print(schiaparelli_image)


# In[33]:


for image in schiaparelli_image:
    pic = image.find('li')
    full_res_image = pic.find('a')['href']
schiaparelli_title = "Schiaparelli Hemisphere"
schiaparelli_hem = {"Title": schiaparelli_title, "url": full_res_image}
print(schiaparelli_hem)


# In[37]:


syrtis_major_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

syrtis_major_response = requests.get(syrtis_major_url)
syrtis_major_soup = BeautifulSoup(syrtis_major_response.text, 'html.parser')


# In[38]:


syrtis_major_image = syrtis_major_soup.find_all('div', class_="wide-image-wrapper")
print(syrtis_major_image)


# In[39]:


for image in syrtis_major_image:
    pic = image.find('li')
    full_res_image = pic.find('a')['href']
syrtis_major_title = "Syrtis Major Hemisphere"
syrtis_major_hem = {"Title": syrtis_major_title, "url": full_res_image}
print(syrtis_major_hem)


# In[40]:


valles_marineris_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

valles_marineris_response = requests.get(valles_marineris_url)
valles_marineris_soup = BeautifulSoup(valles_marineris_response.text, 'html.parser')


# In[41]:


valles_marineris_image = valles_marineris_soup.find_all('div', class_="wide-image-wrapper")
print(valles_marineris_image)


# In[43]:


for image in valles_marineris_image:
    pic = image.find('li')
    full_res_image = pic.find('a')['href']
valles_marineris_title = "Valles Marineris Hemisphere"
valles_marineris_hem = {"Title": valles_marineris_title, "url": full_res_image}
print(valles_marineris_hem)


# In[46]:


hemisphere_image_urls.append(cerberus_hem)


# In[47]:


hemisphere_image_urls.append(schiaparelli_hem)


# In[48]:


hemisphere_image_urls.append(syrtis_major_hem)


# In[49]:


hemisphere_image_urls.append(valles_marineris_hem)


# In[50]:


hemisphere_image_urls


# In[51]:

mars_collection["hemisphere_image"] = hemisphere_image_urls

    return mars_collection 