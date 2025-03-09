''''
Problem Statement
Given an array of integers nums and an integer target, return the indices of the two numbers such that their sum equals target.

Each input has exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9
'''

def two_sum(nums, target):
    hashmap = {}  # Dictionary to store visited numbers and their indices
    
    for i, num in enumerate(nums):  # Iterate through the list
        complement = target - num  # Calculate the complement
        
        if complement in hashmap:  # If complement exists, return indices
            return [hashmap[complement], i]
        
        hashmap[num] = i  # Store the current number with its index
    
    return []  # No valid pair found


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
