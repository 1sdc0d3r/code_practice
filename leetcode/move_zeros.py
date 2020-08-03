'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.'''


def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)
    return nums


print(moveZeroes([0, 1, 2, 0, 3, 4, 0, 0, 0, 5, 0]))
print(moveZeroes([0, 1, 0, 3, 12]))
