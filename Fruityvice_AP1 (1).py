#!/usr/bin/env python
# coding: utf-8

# # FruitVice API
# using the requests library

# In[1]:


import requests
import json


# In[2]:


import pandas as pd


# **Obtain the [fruityvice](https://www.fruityvice.com/) API data using requests.get("url") function**

# In[3]:


url="https://www.fruityvice.com/api/fruit/all"


# In[4]:


fruit_data=requests.get(url)


# **Retriving the data using json.load() function**

# In[5]:


fruit_data=json.loads(fruit_data.text)


# **Converting fruit data to a dataframe**

# In[6]:


fruit_data1=pd.DataFrame(fruit_data)
fruit_data1.head()


# In[7]:


fruit_data1['nutritions'].head()


# **the nutrutions col contained subcolumns that needs to be normalized/flattened**

# In[8]:


fruits = pd.json_normalize(fruit_data)


# In[9]:


fruits.tail()


# **display the family and order of jackfruit

# In[10]:


jack_fruit=fruits[fruits['name']=='Jackfruit']

(jack_fruit.iloc[0]['name'],jack_fruit.iloc[0]['family'])


# **display the number of calories in banana**

# In[13]:


# Write your code here
banana_data=fruits[fruits['name']=='Banana']
banana_data.iloc[0]['name'],banana_data.iloc[0]['nutritions.calories']


# # Official Joke API
# 
# **This API can be used to get random jokes from a database**, the url is https://official-joke-api.appspot.com/jokes/ten

# In[15]:


joke=requests.get("https://official-joke-api.appspot.com/jokes/ten")


# *obtaining the result of the json.load function*

# In[17]:


joke_result=json.loads(joke.text)


# **converting the json file to dataframe and dropping the id and type** 

# In[18]:


joke_result=pd.DataFrame(joke_result)
joke_result.drop(columns=['id','type'],inplace=True)
joke_result

