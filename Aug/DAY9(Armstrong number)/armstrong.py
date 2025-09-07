class Solution:
    def isArmstrong(self, nums):
        l=0
        temp=nums
        while nums:
            dig = nums%10
            l=l+dig**3
            nums=nums//10
        return l==temp

num=int(input())
obj=Solution()
if obj.isArmstrong(num):
    print(f"it is an Armstrong number {num}")
else:
    print(f"Not an Armstrong number {num}")