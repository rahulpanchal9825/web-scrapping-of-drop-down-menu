#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# In[14]:


browser = webdriver.Chrome(executable_path=r"D:\\\chromedriver.exe")
url = ('https://www.kaspersky.co.in/antivirus')
browser.get(url)


# In[16]:


element = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "PlanSelect_plan__1l6py"))).click()


# In[17]:


browser.find_elements(By.CLASS_NAME,value='PlanSelect_needMore__1gPlt')


# In[18]:


element = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "PlanSelect_needMore__1gPlt"))).click()


# In[19]:


browser.find_elements(By.CLASS_NAME,value='BBModalRadioOptionsV2_option__2lT3F')


# In[20]:


pcList = browser.find_elements(By.CLASS_NAME,value='BBModalRadioOptionsV2_option__2lT3F')


# In[21]:


for data in pcList:
    print(data.text)


# In[22]:


import pandas as pd


# In[23]:


NumberOfPC = []
Duration = []
OriginalPrice = []
DiscountPrice = []
for data in pcList:
    NumberOfPCList = data.find_elements(By.CLASS_NAME,value='Option_pack__11_XL')
    for data1 in NumberOfPCList:
        NumberOfPC.append(data1.text)
    DurationList = data.find_elements(By.CLASS_NAME,value='Option_term__12otL')
    for data2 in DurationList:
        Duration.append(data2.text)
    OriginalPriceList = data.find_elements(By.CLASS_NAME,value='Option_cutPrice__1t1Yn')
    for data3 in OriginalPriceList:
        OriginalPrice.append(data3.text)
    DiscountPriceList = data.find_elements(By.CLASS_NAME,value='Option_priceHtml__2yvkW')
    for data4 in DiscountPriceList:
        DiscountPrice.append(data4.text)
        
print(NumberOfPC)
print(Duration)
print(OriginalPrice)
print(DiscountPrice)
        
PCDataList = pd.DataFrame({'Number of PC':NumberOfPC,
                           'Duration':Duration,
                           'Original Price':OriginalPrice,
                           'Discount price':DiscountPrice})
PCDataList


# In[24]:


browser.close()


# In[ ]:





# In[ ]:




