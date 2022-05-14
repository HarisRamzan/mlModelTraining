#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

arrest2010_present=pd.read_csv('C://Users//haris ramzan//Downloads//archive (2)//arrest-data-from-2010-to-present.csv')
crime2010_present=pd.read_csv('C://Users//haris ramzan//Downloads//archive (2)//crime-data-from-2010-to-present.csv')


# In[14]:


corrMatrix =arrest2010_present.corr()
import seaborn as sn
import matplotlib.pyplot as plt
sn.heatmap(corrMatrix, annot=True)
plt.show()


# In[10]:


arrest2010_present.head(5)


# In[15]:


corrMatrix =crime2010_present.corr()
import seaborn as sn
import matplotlib.pyplot as plt
sn.heatmap(corrMatrix, annot=True)
plt.show()


# In[8]:





# In[29]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(30,10))
sns.barplot(x='Charge Group Description',y='Neighborhood Councils (Certified)',data=arrest2010_present, palette='rainbow')
plt.xticks(rotation= 90)
plt.title("councils by charge group description")
plt.show()


# In[21]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(20,5))
sns.countplot(x='Area Name',data=arrest2010_present, palette='rainbow',hue='Sex Code')
plt.title("Count of arrests that Embarked in Each Area, Separated by Sex")
plt.xticks(rotation= 90)
plt.show()


# In[30]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
sns.boxenplot(x='Sex Code', y='Age', data=arrest2010_present, palette='rainbow', hue='Arrest Type Code')
plt.title("Distribution of Age by sex Class, Separated by arrest type")
plt.show()


# In[34]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(50,15))
sns.boxplot(x='Crime Code Description',y='Victim Age',data=crime2010_present, palette='rainbow')
plt.title("Age by crime desc")
plt.xticks(rotation= 90)
plt.show()


# In[ ]:




