class Solution(object):
    def isPalindrome(self, x):
            if x >= 0:
                digit = 0
                temp = x
                while temp != 0:
                    l = temp % 10
                    digit = digit * 10 + l
                    temp = temp // 10
                if digit == x:
                    return True
            else:
                return False
x = 121
obj = Solution()
print(obj.isPalindrome(x))