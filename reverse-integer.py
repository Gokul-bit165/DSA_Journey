class Solution(object):
    def reverse(self, x):

        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x *= sign

        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10

            rev = rev * 10 + digit

        rev *= sign

        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
x = int(input("Enter an integer: "))
obj = Solution()
print("Reversed integer:", obj.reverse(x))