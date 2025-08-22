class UserInput:
    def printnum(self,n):
        return n
n=int(input("Enter an integer: "))
object =UserInput()
print("Entered number:",object.printnum(n))