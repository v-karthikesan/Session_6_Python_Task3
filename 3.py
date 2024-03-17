#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program for to find the Happy numbers from the given list
def is_happy(num):
    seen = set()
    while num != 1:
        next_num = sum(int(d)**2 for d in str(num))
        if next_num in seen:
            return False
        seen.add(next_num)
        num = next_num
    return True

data = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = [num for num in data if is_happy(num)]

print("Happy numbers:", happy_numbers)


# In[ ]:




