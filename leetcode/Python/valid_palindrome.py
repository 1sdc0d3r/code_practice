import re


def isPalindrome(s):
    s = re.sub('[\W_]+', '', s).lower()
    if s == s[::-1]:
        return True
    return False


s1 = "racecar"
s2 = "A man, a plan, a canal: Panama"
s3 = "Not a palendrome: nope..."
print(isPalindrome(s1))
print(isPalindrome(s2))
print(isPalindrome(s3))
