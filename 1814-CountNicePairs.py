def rev(x):
    reverse = 0
    while x>0:
        digit = x%10
        reverse = reverse*10+digit
        x = x//10
    return reverse


class Solution(object):

    def countNicePairs(self, nums):
        count = 0
        MOD = 10**9 + 7
        diff_freq = {}

        for num in nums:
            diff = num - rev(num)
            if diff in diff_freq:
                count += diff_freq[diff]
                count %= MOD
                diff_freq[diff] += 1
            else:
                diff_freq[diff] = 1

        return count % MOD
