class Solution(object):
    def isPalindrome(self, x):
            if x >= 0:
                digit = 0
                temp = x
                while temp != 0:
                    l=temp % 10
                    digit=digit * 10 + l
                    temp=temp // 10
                if digit==x:
                    return True
            else:
                return False
x = int(input("Enter a number to check if it's a palindrome: "))
obj = Solution()
if obj.isPalindrome(x):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
