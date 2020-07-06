#!/usr/bin/env python
# coding: utf-8

# <h1>MINI PROJECT - MAHARASTRA INFORMATION JULY(2020) COVID19</h1>

# <h4>ANAND KUMAR SINGH</h4>

# In[101]:


import pandas as pd
import matplotlib.pyplot as plt


# <h2>Reading DataSet</h2>

# In[102]:


Data=pd.read_csv('covid_19_india.csv')
Data.head()


# In[103]:


Data.describe()


# <h2>Data types of Dataframe</h2>

# In[104]:


Data.dtypes


# In[105]:


Data['Date']=pd.to_datetime(Data['Date'])
start='2020-06-01'
end='2020-06-30'
Data.info()


# <h2>Slicing Dataframe to obtain the desired result</h2>

# In[106]:


new_data=Data[((Data['Date']>=start)&(Data['Date']<=end))& (Data['State/UnionTerritory']=='Maharashtra')]
new_data


# In[107]:


new_data.describe()


# <h2>Ploting line chart to show relation among Cured, Death & Confirmed cases

# In[148]:


fig=plt.figure(figsize=(32,15))
fig.suptitle('Death, cured and confirmed comparision Maharastra july 2020',fontsize=15)

ax1=fig.add_subplot(231)
ax1.set_title('Deaths')
ax1.plot(new_data['Date'],new_data['Deaths'],color='red')

ax2=fig.add_subplot(232)
ax2.set_title('Cured')
ax2.plot(new_data['Date'],new_data['Cured'],color='green')

fig1=plt.figure(figsize=(13,4))
ax3=fig1.add_axes([0,0,1,1])
ax3.set_title('Confirmed')
ax3.plot(new_data['Date'],new_data['Confirmed'],color='orange')


# In[ ]:




