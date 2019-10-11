#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Import libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Markdown

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


## Define the working directory. (This should be executed just once)
os.chdir(os.path.join('..'))
working_path = os.getcwd()
print('The working directory will be {}'.format(working_path))

# Define the path where the data sets are located
datasets_path = os.path.join(working_path, 'Datasets')
print('The datasets will be placed in: {}'.format(datasets_path))


# In[3]:


# Display information about the dataset

with open(os.path.join(datasets_path, 'README.MD'), encoding = 'utf-8') as f:
    md = f.read()
    
Markdown(md)


# In[4]:


## Define paths for each dataset

uber_trips_2014 = os.path.join(datasets_path, 'uber_trips_2014.csv')
uber_trips_2015 = os.path.join(datasets_path, 'uber_trips_2015.csv')
demographics = os.path.join(datasets_path, 'demographics.csv')
geographic = os.path.join(datasets_path, 'geographic.csv')
green_trips = os.path.join(datasets_path, 'green_trips_new_2.csv')
mta_trips = os.path.join(datasets_path, 'mta_trips.csv')
weather = os.path.join(datasets_path, 'weather.csv')
yellow_trips = os.path.join(datasets_path, 'yellow_trips_new.csv')
zones = os.path.join(datasets_path, 'zones.csv')


## Create dataframe for eache dataset

df_uber_trips_2014 = pd.read_csv(uber_trips_2014)
df_uber_trips_2015 = pd.read_csv(uber_trips_2015)
df_demographics = pd.read_csv(demographics)
df_geographic = pd.read_csv(geographic)
df_green_trips = pd.read_csv(green_trips)
df_mta_trips = pd.read_csv(mta_trips)
df_weather = pd.read_csv(weather)
df_yellow_trips = pd.read_csv(yellow_trips)
df_zones = pd.read_csv(zones)


# In[5]:


df_uber_trips_2014.head()


# In[ ]:




