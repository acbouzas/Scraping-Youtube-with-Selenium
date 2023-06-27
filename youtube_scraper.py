#!/usr/bin/env python
# coding: utf-8

# In[1]:


# We import the necessary libraries. Since Youtube loads dinamyc content,
# requests + beautifull soup won't work.

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


# In[2]:


# use the Selenium driver to access the page
driver = webdriver.Chrome()


# In[3]:


url = 'https://www.youtube.com/@MindfulScience/videos'


# In[11]:


# Testing if it works
driver.get(url)


# In[12]:


# Since we are trying to find top popular videos, views and when were they posted,
# We search for the path that leads us to click the "popular" button.

driver.find_element(By.XPATH, '//*[@id="chips"]/yt-chip-cloud-chip-renderer[2]').click()


# In[13]:


# Scroll down until the page finishes loading
while True:
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    
    # Wait for some time to let the content load
    time.sleep(2)
          
    margin = 100  # Adjust the margin as needed
    if driver.execute_script("return window.innerHeight + window.pageYOffset >= document.documentElement.scrollHeight - {};".format(margin)):
        break


# In[14]:


# We use the driver to find in the html the elements we are looking for
videos = driver.find_elements(By.CLASS_NAME,'style-scope ytd-rich-grid-media')


# In[15]:


# Create a video list and append to it all the info collected from each individual video.

video_list = []

for video in videos:
    title = video.find_element(By.XPATH,'.//*[@id="video-title"]').text
    views = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text
    vid_item = {
        'Title' : title, 
        'Views': views,
        'Posted':when
    }
    video_list.append(vid_item)
    


# In[16]:


# Attach the info to a Dataframe
df = pd.DataFrame(video_list)


# In[22]:


df


# In[20]:


# Download data as a csv

# Specify the file path and name for the CSV file
file_path = 'extracted_youtube_data.csv'

# Save the DataFrame as a CSV file
df.to_csv(file_path, index=False)


# In[ ]:




