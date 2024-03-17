#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program for find first Non-Repeating Element 
def first_non_repeating(data):
    from collections import Counter

    counts = Counter(data)
    for num in data:
        if counts[num] == 1:
            return num

data = [10, 9, 10, 1, 1, 2]

first_non_repeating_element = first_non_repeating(data)

print("First non-repeating element:", first_non_repeating_element)


# In[ ]:




