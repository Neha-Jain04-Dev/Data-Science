#!/usr/bin/env python
# coding: utf-8

# # Loops/If

# In[4]:


x=0
while(x<4):
    print(x)
    x=x+1


# In[5]:


#Task: Print First 10 natural numbers using while loop
x=1
while(x<=10):
    print(x)
    x=x+1


# In[9]:


for x in range(2,7):
    print(x)


# In[11]:


Months=['Jan','Feb','March','April','May','June']
for m in Months:
    print(m)


# In[13]:


#Measure Some Strings:
words=['cat', 'window','defenestrate']
for w in words:
    print(w)
    
for w in words:
    print(w," , length of ",w,"=",len(w))


# In[16]:


for i in range(5,10):
    print(i)


# In[17]:


for i in range(0,10,3):
    print(i)


# In[18]:


list(range(9))


# In[22]:


a=['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i)


# # IF-else

# In[20]:


x=8
y=4
if(x<y):
    st="x is less than y"
else:
    st="x is greater than y"
    
print(st)


# In[ ]:


x=int(input("Enter the number for x="))
y=4
if(x<y):
    st="x is less than y"
else:
    st="x is greater than y"
    
print(st)


# In[23]:


x=int(input("please enter an integer:"))
if x<0:
    x=0
    print("Negative changed to zero")
elif x==0:
    print("Zero")
    
elif x==1:
     print("Single")

else:
    print("More")
    


# In[29]:


#Task:write a program using if-elif with different country value and total values.
total=100
country = input("Enter the country name AU/USA:")
if country=="USA":
    if total<=50:
        print("Shipping Cost is $50")
    elif total<=100:
        print("Shipping Cost is $25")
    elif total<=150:
        print("Shipping Cost is $5")
    else: 
        print("FREE")
if country=="AU":
    if total<=50:
        print("Shipping Cost is $100")
    else:
        print("FREE")
    
        


# In[ ]:


#Task : write a program to find even or odd using for loop /range function.


# In[34]:


#num= int(input("Enter the number"))
for num in range(0,10):
    if num%2==0:
        print("Found the an even number",num)
    else:
        print("Found the an odd number",num)


# In[38]:


#Task :write two different loops for break if x is even number and continue when the number is divide by 5.

for x in range(10,20):
    if (x==15):
        break
    #if(x%2==0):continue
    print(x) 
    
for x in range(10,20):
    #if (x==15): break
    if(x/5==0):
        continue
    print(x)  
    


# In[67]:


#Display numbers divisible by 5 from a list.
#Iterate the given list of numbers and print only those numbers which are divisible by 5.

num_list=[10,80,61,23,45,67,89,100]
print("Numbers which are divisible by 5 only:-")
for i in num_list:
    if i%5==0:
        print(i)
print("Sorted Numbers which are divisible by 5 only:-")
for i in sorted(set(num_list)):
    if i%5==0:
        print(i)


# In[44]:


#Task: Calculate the sum of all numbers from 1 to a given number
num= int(input("Enter a given number:"))
Sum=0
for i in range(1,num+1):
    Sum=Sum+i
    print(Sum)


# In[43]:


#Write a program to print multiplication table of a given number
num= int(input("Enter a given number for table:"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)


# List Comprehension

# In[48]:


vec=[-4,-2,0,2,4]
p= [i*2 for i in vec]
print(p)


# In[49]:


p=[i for i in vec if i>=0]
print(p)


# In[50]:


p=[abs(i) for i in vec]
print(p)


# In[57]:


freshfruit = [' banana', ' loganberry ', 'passion fruit ']
p= [weapon.strip()for weapon in freshfruit]
print(p)


# In[59]:


# create a list of 2-tuples like (number, square)
num = int(input("Enter a number for upto range:"))
p=[(i,i**2) for i in range(0,num+1)]
print(p)


# In[63]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
p=[f for f in sorted(set(basket))]
print(p)


# In[74]:


num=range(1,10,2)
print(" Sequence in forward direction:")
for j in num:
    print(j)
print (" Sequence in reverse direction:")
for j in reversed(num):
    print(j)
    



# # If-Elif

# In[77]:


today = 'Wednesday'
if today == 'Sunday':
    print("Today is the day of the sun.")

elif today == 'Monday':
    print("Today is the day of the moon.")

elif today == 'Tuesday':
    print("Today is the day of Tyr, the god of war.")

elif today == 'Wednesday':
    print("Today is the day of odin, the supreme diety.")

elif today == 'Thursday':
    print("Today is the day of Thor, the god of thunder.")

elif today == 'Friday':
    print("Today is the day of Frigga, the goddess of beauty.")

elif today == 'Saturday':
    print("Today is the day of Saturn, the god of fun and feasting.")
#else:
    #print ("NONE")
 


# In[79]:


a_number = 49

if a_number % 2 == 0:

  print('{} is divisible by 2'.format(a_number))

elif a_number % 3 == 0:

  print('{} is divisible by 3'.format(a_number))

elif a_number % 5 == 0:

  print('{} is divisible by 5'.format(a_number))

else:

  print('All checks failed!')

  print('{} is not divisible by 2, 3 or 5'.format(a_number))


# In[80]:


a_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

 

for i in range(len(a_list)):

    print('The value at position {} is {}.'.format(i, a_list[i]))

 


# In[81]:


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

 

for day in weekdays:

    print('Today is {}'.format(day))

    if (day == 'Wednesday'):

        print("I don't work beyond Wednesday!")

        break

 


# In[82]:


for day in weekdays:

    if (day == 'Wednesday'):

        print("I don't work on Wednesday!")

        continue

    print('Today is {}'.format(day))


# In[ ]:




