#!/usr/bin/env python
# coding: utf-8

# ##### Pangram

# In[1]:


import string


# In[9]:


def pangram(str):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char  not in str.lower():
            return False
        return True
    
string=input("Enter String: ")
if(pangram(string)==True):
    print("Yes")
else:
     print("No")
        


# ##### pascal Triangle
# 

# In[ ]:


I didnt understand .


# In[ ]:





# In[ ]:




