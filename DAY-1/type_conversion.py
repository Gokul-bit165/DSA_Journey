class Solution:
    def tofloat(self,n):
        f=float(n)
        return f
    def tostr(self,n):
        s=str(n)
        return s
    def tobool(self,n):
        b=bool(n)
        return b

object=Solution()
n=int(input("Enter an integer: "))
print("Integer:",n)
print("Float:",object.tofloat(n))
print(f"String:'{object.tostr(n)}'")
print("Boolean:",object.tobool(n))