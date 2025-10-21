"""
Split column pandas
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


datos = pd.read_excel("C:/Users/HP/Desktop/datos.xlsx", header=0)


# In[3]:


df = pd.DataFrame(datos)


# In[4]:


df['name ']


# In[5]:


df1= df['name '].str.split(expand=True)


# In[6]:


df2 = df.join(df1)


# In[7]:


df = df2
df


# In[8]:


df1 = df[['age', 'gender', 0,1]]


# In[9]:


df1


# In[10]:


df2 = df1.rename(columns={0: 'name', 1 :'country'})
df2


# In[11]:


df3 = df2.ffill()


# In[12]:


df3


# In[13]:


df = df3.dropna()


# In[14]:


df


# In[ ]:




