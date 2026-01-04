"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
 

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n # 1

    prefix = 1 # 2.1
    for i in range(n): # 2.2, 
        res[i] = prefix # 2.3
        prefix *= nums[i] # 2.4

    postfix = 1 # 3.1
    for i in range(n - 1, -1, -1): # 3.2
        res[i] *= postfix # 3.3
        postfix *= nums[i]  # 3.4
    return res # 3.5


""" 
DESCRIPTION OF SUBMITIONS

input: [1,2,3,4]
Output: [24,12,8,6]


1. create a list res=[1,1,1,1]

2.1 collect a prefix for left side

2.2 i = 0, prefix = 1, res[i] = 1, nums[i] = 1
2.3 save for — res[i] = prefix — [1,...]
2.4 prefix * nums[i] — prefix = 1

2.2 i = 1, prefix = 1, res[i] = 1, nums[i] = 2
2.3 save for — res[i] = prefix — [1,1...]
2.4 prefix * nums[i] — prefix = 2

2.2 i = 2, prefix = 2, res[i] = 1, nums[i] = 3
2.3 save for — res[i] = prefix — [1,1,2...]
2.4 prefix * nums[i] — prefix = 6

2.2 i = 3, prefix = 6, res[i] = 1, nums[i] = 4
2.3 save for — res[i] = prefix — [1,1,2,6]
2.4 prefix * nums[i] — prefix = 24

# RES = [1,1,2,6]

3.1 collect postfix from right side

3.2 i = 3, postfix = 1, res[i] = 6, nums[i] = 4
3.3 save for — res[i] *= postfix — [..., 6]
3.4 postfix *= nums[i] = 4

3.2 i = 2, postfix = 4, res[i] = 2, nums[i] = 3
3.3 save for — res[i] *= postfix — [.., 8,6]
3.4 postfix *= nums[i] = 12

3.2 i = 1, postfix = 12, res[i] = 1, nums[i] = 2
3.3 save for — res[i] *= postfix — [.., 12,8,6]
3.4 postfix *= nums[i] = 24

3.2 i = 0, postfix = 24, res[i] = 1, nums[i] = 1
3.3 save for — res[i] *= postfix — [24,12,8,6]
3.4 postfix *= nums[i] = 24

"""