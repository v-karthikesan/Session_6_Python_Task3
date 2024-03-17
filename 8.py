#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Finding the minimum element in a rotated and sorted list
def find_minimum(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[high]:
            high = mid
        elif nums[mid] > nums[high]:
            low = mid + 1
        else:
            high -= 1

    return nums[low]

rotated_sorted_list = [4, 5, 6, 7, 0, 1, 2]
min_element = find_minimum(rotated_sorted_list)
print("Minimum element:", min_element)


# In[ ]:




