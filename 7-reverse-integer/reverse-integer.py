class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        negative = x < 0
        if negative:
            x = -x
        reversed_x = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if reversed_x > (INT_MAX - pop) // 10:
                return 0
            reversed_x = reversed_x * 10 + pop
        if negative:
            reversed_x = -reversed_x
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        return reversed_x
