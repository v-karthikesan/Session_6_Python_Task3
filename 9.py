#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program for finding triplets with a given sum
def find_triplet(nums, target):
    nums.sort()
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return None

numbers = [10, 20, 30, 9]
target_sum = 59
triplet = find_triplet(numbers, target_sum)
print("Triplet with sum", target_sum, ":", triplet)


# In[ ]:




