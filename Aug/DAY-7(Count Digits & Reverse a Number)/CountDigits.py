class Solution(object):
    def findNumbers(self, nums):
        even=0
        for i in nums:
            count = 0
            while i > 0:
                count += 1
                i //= 10
            if(count%2==0):
                even+=1
        return even
                

num =[12,345,2,6,7896]
count=0

obj=Solution()
print(obj.findNumbers(num))