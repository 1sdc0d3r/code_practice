'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''


def maxSubArray(nums):
    max = -100000
    if len(nums) < 2:
        print("single")
        return sum(nums)
    if len(nums) == 2:
        for n in nums:
            if n > max:
                max = n
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            print(nums[i:j])
            if(sum(nums[i:j])) > max:
                max = sum(nums[i:j])

    return max


# print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
# print(maxSubArray([-2, 1]))  # 1
print(maxSubArray([-2, -1]))  # -1
