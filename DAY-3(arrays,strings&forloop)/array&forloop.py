class Solution(object):
    def runningSum(self, nums):
        s=0
        tot=[]
        for i in range(len(nums)):
            s=s+nums[i]
            tot.append(s)
        return tot
            

nums =[1, 2, 3,4]
obj=Solution()
print(obj.runningSum(nums))