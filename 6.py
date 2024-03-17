#!/usr/bin/env python
# coding: utf-8

# In[1]:


#program for to finding duplicates in three lists:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [2, 4, 7, 8]

duplicates = set(list1).intersection(set(list2)).intersection(set(list3))

print("Duplicates:", duplicates)


# In[ ]:




