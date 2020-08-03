'''
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.
'''


def isHappy(self, n):
    limit = 50
    i = 0
    while i < limit:
        print(i)
        if n == 1:
            return True
        i += 1
        s = [int(d)**2 for d in str(n)]
        n = 0
        n = sum(s)
        # for num in s:
        #     n+=num
    return False

    """
        :type n: int
        :rtype: bool
        """
