#!/usr/bin/env python
# coding: utf-8

# # Functions

# In[2]:


def square(x):
    return x*x


print(square(4))


# In[8]:


def add_numbers(x,y):
    sum= x+y
    return sum
print("The sum is: ", add_numbers(4,5))


# In[10]:


def greet(name, msg):
    print("Hello", name+","+msg)
    
greet("Andrew", "Good morning!")


# In[22]:


#Task:Write a program to create a function that takes two arguments, name and age, and print their value.
def print_two_args(name,age):
    print("My name is",name,"and age is",age)
    
print_two_args("Neha",30)


# In[23]:


#Task : Write a function absolute_value to find absolute of a given number.
def absolute_value(num):
    if num>=0:
        return num
    else:
        return abs(num)
print(absolute_value(2))
print(absolute_value(-4))   


# In[25]:


#Task : write a function multiply to calculate multiplication of two numbers by taking as a arguments.
def multiplication(a,b):
    print("value of a=",a)
    print("value of b=",b)
    #return a*b
    print("product of",a,"and",b,"is",a*b)
    
    
multiplication(2,4)


# In[35]:


#Task : write a function division to calculate division of two numbers by taking as a arguments.
def div(a,b):
    print("value of a=",a)
    print("value of b=",b)
    try:
        a/b==0
    except ZeroDivisionError:
        print("division by Zero")
    else:
        print("division of",a,"and",b,"is",a/b)
    
    
div(2,4)


# #local variables and global variables

# In[38]:


x=20
def my_func():
    x=10
    print("Value inside function:",x)
#x = 20
my_func() 
print("Value outside function:",x)


# In[40]:


squares = list(map(lambda x: x**2, range(10)))
squares


# In[42]:


squares=[x**2 for x in range(10)]
squares


# In[44]:


#Task : Write the above code to find cube of x
cubes = list(map(lambda x: x**3, range(10)))
cubes


# In[45]:


sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result= map(lambda x:x*x,sequences)
print(list(filtered_result))


# In[46]:


sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result= map(lambda x:x*x*x,sequences)
print(list(filtered_result))


# In[47]:


filtered_result = filter (lambda x: x > 4, sequences)
print(list(filtered_result))


# In[49]:


sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 5, sequences)
print(list(filtered_result))


# In[50]:


squares = []
for x in range(10):
    squares.append(x**2)
print(squares)


# In[12]:


def square():
    squares = []
    for x in range(10):
        squares.append(x**2)
    print(squares)


# In[13]:


square()


# In[14]:


#Given two integer numbers return their product only if the product is equal to or lower than 1000,
#else return their sum.
def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2
# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)
# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)


# In[15]:


#Task: Check if the first and last number of a list is the same.
#Write a function to return True if the first and last number of a given list is same. 
#If numbers are different then return False.

def first_last_same(numberList):
    print("Given list:", numberList)
    first_num = numberList[0]
    last_num = numberList[-1]
    if first_num == last_num:
        return True
    else:
        return False
numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))



# In[ ]:




