class Solution(object):
    def reverse(self, x):
        neg = False
        if x < 0:
            neg = True
            x = x*-1
        i = 0
        original = x
        while x > 0:
            digit = x%10
            if i > (2**31 - 1 - digit) // 10:
                return 0
            i = i*10 + digit
            x = x//10
        if neg:
            i = i*-1
        return i
        
