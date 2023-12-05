#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openpyxl
import math
import pandas as pd


# In[2]:


hdb = pd.read_excel('DemoData.xlsx',sheet_name='HDB Resale + URA', header=0,index_col=False,keep_default_na=True)


# In[3]:


hdb.head(10)


# In[4]:


mrt = pd.read_excel('mrt.xlsx',sheet_name='Sheet1', header=0,index_col=False,keep_default_na=True)


# In[5]:


mrt.head(10)


# In[6]:


hdb.iloc[0]


# In[ ]:





# In[8]:


for i in range(len(hdb)) :
    min= 100
    lat1 = math.radians(hdb.loc[i, "latitude"] ) 
    lon1 = math.radians(hdb.loc[i, "longitude"] ) 
    for j in range(len(mrt)) :
        lat2 = math.radians(mrt.loc[j, "lat"] ) 
        lon2 = math.radians(mrt.loc[j, "lng"] ) 
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        R = 6373.0
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        #Haversine formula
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        if min > distance:
            min = distance
            mrtMin=mrt.loc[j,"station_name"]
    print(min)
    hdb.loc[i, "Nearest MRT(km)"] = min
    hdb.loc[i, "MRT"] = mrtMin


# In[9]:


min


# In[ ]:





# In[10]:


hdb


# In[11]:


hdb.to_csv('mrt_distance.csv',index=False)


# In[ ]:


R = 6373.0
#radius of the Earth


# In[ ]:





# In[ ]:


lat1 = math.radians(1.36200453938712)
lon1 = math.radians(103.8538799)
lat2 = math.radians(1.349069)
lon2 = math.radians(103.749596)
#coordinates


# In[ ]:





# In[ ]:


dlon = lon2 - lon1
#change in coordinates


# In[ ]:


dlat = lat2 - lat1


# In[ ]:


a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
#Haversine formula


# In[ ]:


c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
distance = R * c


# In[ ]:


print(distance)


# In[ ]:





# In[ ]:


#pip install --upgrade google-auth-oauthlib


# In[ ]:


#pip install geopy


# In[ ]:


import geopy
from geopy.distance import geodesic

# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers
lat1 = math.radians(1.36200453938712)
lon1 = math.radians(103.8538799)
lat2 = math.radians(1.333207)
lon2 = math.radians(103.742308)
origin = geopy.Point(lat1, lon1)
destination = VincentyDistance(kilometers=d).destination(origin, b)

lat2, lon2 = destination.latitude, destination.longitude


# In[ ]:


# Importing the geodesic module from the library
from geopy.distance import geodesic
lat1 = math.radians(1.36200453938712)
lon1 = math.radians(103.8538799)
lat2 = math.radians(1.333207)
lon2 = math.radians(103.742308)
# Loading the lat-long data for Kolkata & Delhi
amk = (1.36200453938712,103.8538799)
mrt = (1.333207, 103.742308)
  
# Print the distance calculated in km
print(geodesic(amk, mrt).km)


# In[ ]:


from geopy.distance import great_circle

print(great_circle(amk, mrt).km)


# In[ ]:


from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km


# In[ ]:


from math import radians, cos, sin, asin, sqrt
# convert decimal degrees to radians 
lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
# haversine formula 
dlon = lon2 - lon1 
dlat = lat2 - lat1 
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * asin(sqrt(a)) 
# Radius of earth in kilometers is 6371
km = 6371* c
print(km)


# In[ ]:




