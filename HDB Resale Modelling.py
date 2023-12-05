#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns #visualization


# In[2]:


hdb=pd.read_csv("FINAL_clean_merged_data_09102021.csv")


# In[3]:


hdb.head(10)


# In[4]:


#hdb = hdb.drop(columns=['MRT Latitude', 'MRT Longitude','School Latitude', 'School Longitude','Hawker Longitude','Hawker Latitude'])
#hdb = hdb.drop(columns=['Hawker Longitude','Hawker Latitude'])

hdb = hdb.drop(columns=['Longitude','Latitude'])


# In[5]:


hdb.head(10)


# In[8]:


hdb1 = hdb.drop(columns=['No. of Units', 'Postal Code', 'Unit Price ($psf)'])


# In[9]:


hdb2 = hdb1[hdb1.columns.drop(list(hdb1.filter(regex='Latitude')))]


# In[10]:


hdbcorr = hdb2[hdb2.columns.drop(list(hdb2.filter(regex='Longitude')))]


# In[13]:


#We want to try to find out which variables are useful than the others and 
#are there any variables which you can eliminate

cor = hdbcorr.corr(method='kendall')

#by default it uses Pearson Correlation coefficient

#correlation quantifies the relationship between the variables (-1 to 1)

plt.figure(figsize=(20,20))

sns.heatmap(cor,annot = True)


# In[12]:


hdbcorr.head(10)


# In[ ]:




