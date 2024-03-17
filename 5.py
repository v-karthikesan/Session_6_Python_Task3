#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program for Distributing mangoes among students
def distribute_mangoes(mangoes):
    min_mangoes = min(mangoes)
    max_mangoes = max(mangoes)
    difference = max_mangoes - min_mangoes
    return difference

mangoes = [15, 12, 18, 10]  # Sample list
students = 4  # Number of students

difference = distribute_mangoes(mangoes)

print("Minimum difference in mangoes:", difference)


# In[ ]:




