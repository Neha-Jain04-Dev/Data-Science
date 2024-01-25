#!/usr/bin/env python
# coding: utf-8

# Practice Assignment 3 (String Functions)

# In[2]:


# String Functions
name="Tesla"
name


# In[7]:


a=name.lower()
b=name.upper()
c=len(name)
d= name.capitalize()
print("name in lower case:",a)
print("name in upper case:",b)
print("length of name:",c)
print("first letter of name in capital:",d)


# In[4]:


name.isalpha()


# In[8]:


starship = "Enterprise"

starship.startswith("en")


# In[9]:


starship.endswith("rise")


# In[10]:


string = "Welcome Sir "


# In[12]:


new_string=string.replace("Welcome","GoodBye")
print(new_string)


# In[13]:


txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)


# In[14]:


phrase = "the surprise is in here somewhere"
phrase.find("surprise")


# In[16]:


text = "Hello World DataTrained"

# splits at space

print(text.split())


# In[21]:


text = "Hello,World, DataTrained"

# splits at ','

print(text.split(", "))


# In[22]:


text = "Hello,World:, DataTrained"

# Splits at ':'

print(text.split(":"))


# Task:1
# Write a program that converts the following strings to lowercase:
# 
# "Animals", "Badger", "Honey Bee", "Honey Badger". Print each lowercase string on a separate line.
# 
# 

# In[24]:


Str1= "Animals"
Str2= "Badger"
Str3= "Honey Bee"
Str4= "Honey Badger"
print("Str1:",Str1.lower())
print("Str2:",Str2.lower())
print("Str3:",Str3.lower())
print("Str4:",Str4.lower())


# Task:2
# 
# Write a program that prints out the result of .startswith("be") on
# each of the following strings:

# In[25]:


string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

string1.startswith("be")


# In[26]:


string2.startswith("be")


# In[27]:


string3.startswith("be")


# In[28]:


string4.startswith("be")


# Task:3
# 
# Using the same four strings from above, write a program that
# uses string methods to alter each string so that .startswith("be")
# returns True for all of them

# In[29]:


string1.startswith("Be")


# In[30]:


string2.startswith("be")


# In[31]:


string3.startswith("BE")


# In[32]:


string4.startswith("bE")


# Task:4 Write a program that takes input from the user and displays that
# input back.
# 

# In[33]:


print(int(input("Enter First Number")))
print(int(input("Enter Second Number")))


# Task:5
# Write a program that takes input from the user and displays the
# input in lowercase.

# In[37]:


String=input("Enter input to display in lowercase")
print("String in lowercase: ",String.lower())


# Task:6 Write a program that takes input from the user and displays the
# number of characters/len in the input.

# In[38]:


String1=input("Enter input to display the length of the string")
print("Number of Characters in String1: ",len(String1))


# In[ ]:




