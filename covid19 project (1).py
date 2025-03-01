#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing required libraries
import pandas as pd
import numpy as np


# In[2]:


#loading the data set
data=pd.read_csv("file.csv")
data


# In[ ]:





# In[3]:


#to check the how many rows and columns
data.shape


# In[4]:


#access the frist rows
data.head()


# In[5]:


#access the last five rows
data.tail()


# In[6]:


#displaying total columns from data set
data.columns

Data cleaning 
# In[7]:


#checking column type
data.dtypes


# In[8]:


#data frame information
data.info()


# In[9]:


#checking the missing values
data.isnull()


# In[10]:


#checking missing values count on each column
data.isnull().sum()


# In[11]:


##checking missing values count on each column,applying sorting
data.isnull().sum().sort_values(ascending=True)


# In[12]:


#droping a null values in data frame
#create a variable ("df")
df=data.dropna()
df


# In[13]:


#after droping missing values then again checking missing values
df.isnull().sum()


# In[14]:


#data frame description
df.describe()


# 1Q) Show the number of confiormed,Deaths and Recovered Cases in each Region

# In[15]:


#check the five rows 
df.head(2)


# In[16]:


#to show the confirmed ,Deaths and ,Recovered cases
df.groupby('Region').sum()


# In[17]:


#check the which region how many cases confirmed
df.groupby('Region')['Confirmed'].sum().sort_values(ascending=True).head(10)


# In[18]:


df.groupby('Region')[['Confirmed','Recovered']].sum().head(10)


# 2Q)Remove all the record where confirmed cases is less than 10

# In[19]:


#Filtering the entair the data 
#check the less than 10 confirmed cases


# In[20]:


data[data.Confirmed<10].head(5)


# 3Q) in which Region ,maximum number of confirmed cases were recorded?

# In[21]:


df.groupby('Region').Confirmed.sum().sort_values(ascending= False)


# 4Q) in which Region ,maximum number of Death  cases were recorded?

# In[22]:


df.groupby('Region').Deaths.sum().sort_values(ascending=True)


# 5Q)How many Confirmed, Death and Recovered cases were reported from india till 29 April 2020?

# In[27]:


data[data.Region=='India']


# 6Q)Sort the entire data wrt no of Confirmed cases in ascend order

# In[34]:


df.sort_values(by=['Confirmed'],ascending=True)


# 7Q)Sort the entire data wrt no of Confirmed cases in descending  order

# In[35]:


df.sort_values(by=['Confirmed'],ascending=True)


# In[38]:


df.head()


# Data visuvalization 

# In[49]:


import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np


# In[41]:


data.head()


# In[44]:


#check the null values in heatmap
sns.heatmap(data.isnull())
plt.show()


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




