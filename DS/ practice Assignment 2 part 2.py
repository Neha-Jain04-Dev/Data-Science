#!/usr/bin/env python
# coding: utf-8

# Practice Assignment 2 Part 2

# Perform all basic set operation such as-add,remove,pop
# 

# In[31]:


basket={'apple','orange','apple','pear','orange','banana'}
print(basket)


# In[4]:


basket.add("guava")
basket.add('strawberry')
basket


# In[5]:


basket.pop()


# In[7]:


basket.remove("orange")
basket


# Dictionary

# In[8]:


tel={'jack':4098,'sape':4139}


# In[10]:


tel['guido']=4127
tel['irv']=4127
tel


# In[11]:


tel['jack']


# In[12]:


del tel['sape']
tel


# In[13]:


my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}

print("username :", my_dict['username'])

print("email : ", my_dict["email"])

print("location : ", my_dict["location"])


# In[14]:


#adding key
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}

my_dict['name']='Nick'

print(my_dict)


# In[15]:


#updating value
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}

my_dict["username"] = "ABC"

print(my_dict)


# In[16]:


del my_dict['location']
my_dict


# In[17]:


my_dict.pop("username")


# In[18]:


print(my_dict)


# In[19]:


my_dict.clear()
my_dict


# Task : Do create dictionary with keys : Sportsid ,Sportname ,playername and give related values .
# 
# Perform add,update with new key : country with value , delete and clear operation on this dictionary.

# In[24]:


dict1={
    "sportsid":101,"sportname":"cricket","playername":"hardik"}
print("sportsid :", dict1['sportsid'])

print("sportname : ", dict1["sportname"])

print("playername: ", dict1["playername"])


# In[25]:


dict1['country']='INDIA'
dict1


# In[26]:


dict1["sportsid"]=102
dict1


# In[27]:


del dict1['country']


# In[28]:


dict1


# In[29]:


dict1.pop('sportsid')
dict1


# In[30]:


dict1.clear()
dict1


# In[ ]:





# In[ ]:




