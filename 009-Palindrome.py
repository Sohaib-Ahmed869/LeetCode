class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        i = 0
        origin = x
        while x>0:
            extract = x%10
            i = i*10 + extract
            x = x//10

        return origin == i
