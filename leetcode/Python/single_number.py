# Given a non-empty array of integers, every element appears twice except for one. Find that single one.


def singleNumber(self, nums):
    d = dict()
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    for i in d:
        if d[i] == 1:
            return i
    """
    :type nums: List[int]
    :rtype: int
    """
