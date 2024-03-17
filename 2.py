#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program for list the Prime Numbers count and prime Numbers list 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

data = [10, 501, 22, 37, 100, 999, 87, 351]

prime_count = sum(is_prime(num) for num in data)
prime_numbers = [num for num in data if is_prime(num)]

print("Number of prime numbers:", prime_count)
print("Prime numbers:", prime_numbers)


# In[ ]:




