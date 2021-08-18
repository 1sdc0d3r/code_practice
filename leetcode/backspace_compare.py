# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.


def backSpaceCompare(S, T):
    def back(x):
        newString = list()
        for l in x:
            if l is not "#":
                newString.append(l)
            elif l is "#" and len(newString) > 0:
                newString.pop()
        return "".join(newString)
    if back(S) == back(T):
        return True
    return False


s1 = "ab#c"
t1 = "ad#c"
s2 = "ab##"
t2 = "c#d#"
s3 = "a##c"
t3 = "#a#c"
s4 = "a#c"
t4 = "b"
s5 = "y#fo##f"
t5 = "y#f#o##f"
s6 = "hd#dp#czsp#####"
t6 = "hd#dp#czsp#######"
print(backSpaceCompare(s1, t1))  # True
# print(backSpaceCompare(s2, t2))  # True
# print(backSpaceCompare(s3, t3))  # True
# print(backSpaceCompare(s4, t4))  # False
# print(backSpaceCompare(s5, t5))  # True
# print(backSpaceCompare(s6, t6))  # True
