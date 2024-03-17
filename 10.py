#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Checking if there is a sublist with a sum equal to zero
def sublist_with_zero_sum(nums):
    prefix_sum = 0
    seen = set()

    for num in nums:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in seen:
            return True
        seen.add(prefix_sum)

    return False

numbers = [4, 2, -3, 1, 6]
has_zero_sum_sublist = sublist_with_zero_sum(numbers)
print("Sublist with sum zero exists:", has_zero_sum_sublist)


# In[ ]:




