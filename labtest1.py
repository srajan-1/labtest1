#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[46]:


cityx=[100,120,85,90,110,95]
cityy=[80,75,60,95,85,90]
cityz=[150,140,135,160,155,180]


# In[47]:


cx=np.array(cityx)
cy=np.array(cityy)
cz=np.array(cityz)


# In[57]:


print("Total rain in city x:")
print(sum(cx))
print("Avg rain in city x:")
print(sum(cx)/6)
print("Total rain in city y:")
print(sum(cy))
print("Avg rain in city y:")
print(sum(cy)/6)
print("Total rain in city z:")
print(sum(cz))
print("Avg rain in city z:")
print(sum(cz)/6)


# In[49]:


sumarr=cx+cy+cz;
avgarr=sumarr/3
print("Average rainfall in each corrresponding month across all cities")
print(avgarr)


# In[50]:


x=np.arange(1,7)
# print(x)
plt.plot(x,cx,label="rainfall")
plt.legend()
plt.title("Rainfall data in city X")
plt.xlabel("Month")
plt.ylabel("Rainfall in mm")


# In[51]:


x=np.arange(1,7)
# print(x)
plt.plot(x,cy,label="rainfall")
plt.legend()
plt.title("Rainfall data in city Y")
plt.xlabel("Month")
plt.ylabel("Rainfall in mm")


# In[52]:


x=np.arange(1,7)
# print(x)
plt.plot(x,cz,label="rainfall")
plt.legend()
plt.title("Rainfall data in city Z")
plt.xlabel("Month")
plt.ylabel("Rainfall in mm")


# In[53]:


range1=np.max(cx)-np.min(cx)
print("Range of city X :")
print(range1)

range2=np.max(cy)-np.min(cy)
print("Range of city Y :")
print(range2)

range3=np.max(cz)-np.min(cz)
print("Range of city Z :")
print(range3)


# In[56]:


r=[range1,range2,range3]
# xdata=np.linspace(1,4,1)
plt.bar(np.arange(1,4),r)
# plt.bar(xdata,r)


# In[ ]:





# In[ ]:




