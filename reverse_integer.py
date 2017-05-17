class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = x * sign
        revStr = str(x)[::-1]
        result = int(revStr) * sign
        return 0 if (sign > 0 and result >= 2147483647) or (sign < 0 and result <= -2147483648) else result


print Solution().reverse(1534236469)
