#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program for to find the sum of the first and last digit of an integer
def sum_first_last(num):
    last_digit = num % 10
    first_digit = num // (10**(len(str(num)) - 1))
    return last_digit + first_digit

num = int(input("Enter an integer: "))  # Assuming user input

sum_of_digits = sum_first_last(num)

print("Sum of first and last digit:", sum_of_digits)


# In[ ]:




