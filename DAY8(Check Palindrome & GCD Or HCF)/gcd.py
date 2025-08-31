class Solution:
    def findGCD(self, nums):
        a = min(nums)
        b = max(nums)
        while b:
            a, b = b, a % b
        return a

num =[2,5,6,9,10]
obj=Solution()
print(obj.findGCD(num))