class Solution(object):
    def isPowerofTwo(self, n):
        if n<=0:
            return False
        while n % 2 == 0:
            n/=2
        return n==1
        
obj=Solution()
n=int(input("enter a num:"))
print(obj.isPowerofTwo(n))