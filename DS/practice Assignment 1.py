#!/usr/bin/env python
# coding: utf-8

# # Practice Assignment 1

# In[1]:


# 8+4
8+4


# In[2]:


#16*5
16*5


# In[3]:


#50-6*5
50-6*5


# In[4]:


#(50-6*5)/4
(50-6*5)/4


# In[7]:


# Now Write comment

print( "This is my first program.")

# It prints the phrase "Hello, World"
print('Hello, World')

# The comments are longer than the code!
print('The comments are longer than the code!')



# In[8]:


greeting = "Hello World of Python"

print(greeting)


# In[10]:


8 / 5 # division always returns a floating point number


# In[11]:


17 / 3 # classic division returns a float


# In[12]:


17 // 3 # floor division discards the fractional part


# In[13]:


17 % 3 # the % operator returns the remainder of the division


# In[14]:


5 * 3 + 2 # result * divisor + remainder


# In[15]:


5 ** 2 # 5 squared


# In[16]:


2 ** 7 # 2 to the power of 7


# In[17]:


width = 20

height = 5 * 9

width * height

print(width)

print('The value of width=',width)  # use single quote

print("The value of width is=", width)  # use double quote

print("Value=", width*height)


# In[18]:


#Task: Now try to print height yourself
print(height)

print('The value of width=',height)  # use single quote

print("The value of width is=", height)  # use double quote


# In[20]:


tax = 12.5 / 100

price = 100.50

price * tax

print("The value of tax=", tax)

print("The value of price=",price)  

print("The value =", price*tax)


# # String concatenation

# In[22]:


"The "+"Sun"


# In[23]:


"The "+"Moon"


# In[24]:


"Planets"+" Universe"


# In[25]:


string1 = "Elon"

string2 = "Musk"

magic_string = string1 + string2

magic_string


# In[26]:


#Task : Make variable firstname and lastname and concatnate them with space.
first_name = "Arthur"

last_name = "Dent"

full_name = first_name + " " + last_name

full_name


# In[27]:


#Task:

#1. Create two strings, concatenate them, and print the resulting string.

#2. Create two strings, use concatenation to add a space between them,and print the result.
string1="Hello"
string2="World"
full=string1+string2
full


# In[28]:


full= string1+" "+string2
full


# In[29]:


# User Input

prompt = "Hey, what's up? "

user_input = input(prompt)

print("You said: " + user_input)


# In[35]:


#Task: Take user input and make twice of that number


num = input("Enter a number to be doubled: ")

doubled_num = num*2

print(doubled_num)


# In[36]:


#Task: Take user input and make twice of that number and typecast it to float.


num = input("Enter a number to be doubled: ")

doubled_num = float(num) * 2

print(doubled_num)


# In[44]:


#Write a program that uses input() twice to get two numbers from the user, multiplies the numbers together, 
#and displays the result.If the user enters 2 and 4, then your program should print the following text: 
#The product of 2 and 4 is 8.0.

num1=int(input("Enter a First number: "))
num2=int(input("Enter a second number: "))
product=num1*num2
print("Product of"+" "+str(num1)+" and "+str(num2)+ " is ",float(product))


# In[45]:


#Calculate simple interest by taking user input for priciple,rate and time .


p=int(input("Enter principle"))
r= int(input("Enter rate"))
t= int(input("Enter time"))


simple_interest=(p*r*t)/100
simple_interest


# In[48]:


# Find length

len("abc")



# In[47]:


letters = "abc"

len(letters)


# In[49]:


#Task:Create a string and print its length using len().
string="This is my macbook Air Pro."
len(string)


# In[50]:


#A travel company wants to fly a plane to the Bahamas. Flying the plane costs 5000 dollars. 
#So far, 29 people have signed up for the trip. If the company charges 200 dollars per ticket,
#what is the profit made by the company? Create variables for each numeric quantity and
#use appropriate arithmetic operations.

planeCost= 5000
SignedUpPeople=29
ChargesPerTicket=200
amountReceived= ChargesPerTicket*SignedUpPeople
TotalProfit=amountReceived-planeCost
TotalProfit

