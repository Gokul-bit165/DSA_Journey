class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x *= sign
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit
        rev *= sign
        return rev
x = int(input("Enter a num: "))
obj = Solution()
print("Reversed num:", obj.reverse(x))