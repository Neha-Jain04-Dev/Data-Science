#!/usr/bin/env python
# coding: utf-8

# In[1]:


squares = [1, 4, 9, 16, 25]
squares


# In[2]:


squares[0] # indexing returns the item


# In[3]:


squares[-1]


# In[4]:


squares[-3:]


# In[5]:


squares[:]


# In[6]:


squares + [36, 49, 64, 81, 100]


# In[7]:


cubes = [1, 8, 27, 65, 125]
cubes


# In[8]:


cubes[3] = 64
cubes


# In[9]:


cubes.append(216) # add the cube of 6
cubes


# In[10]:


cubes.append(7 ** 3) # and the cube of 7
cubes


# In[11]:


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters


# In[12]:


# replace some values

letters[2:5] = ['C', 'D', 'E']
letters


# In[13]:


len(letters)


# In[14]:


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits


# In[15]:


fruits.count('apple')


# In[16]:


fruits.count('tangerine') #Return the number of times x appears in the list


# In[17]:


fruits.index('banana')


# In[18]:


fruits.index('banana', 4) # Find next banana starting a position 4


# In[19]:


fruits.reverse()
fruits


# In[20]:


fruits.append('grape')
fruits


# In[21]:


fruits.sort()
fruits


# In[23]:


fruits.pop()
fruits.pop()
fruits


# In[24]:


stack = [3, 4, 5]
stack.append(6)
stack


# In[25]:


stack.append(7)
stack


# In[26]:


stack.pop()
stack


# In[27]:


stack.pop()
stack


# In[28]:


stack.pop()
stack


# In[29]:


#Reverse a list in Python.

list1 = [100, 200, 300, 400, 500]

list1.reverse()

print(list1)


# In[38]:


list1 = [100, 200, 300, 400, 500]

list1 = list1[::-2]

print(list1)


# In[39]:


#sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)



# In[49]:


#Task: Perform all basic set operation such as-add,remove,pop

basket.add('papaya')

basket


# In[50]:


basket.pop()
basket


# In[ ]:




