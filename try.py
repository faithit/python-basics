#try and except is used for exception handling
"""
try:
        block of code that can cause an error
except:
        code that runs incase of an error
        """
try:
    num=int(input("enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("you cannot divide a  number by zero")
#name error
try:
    print(x)
except NameError:
    print("The variable is not defined")
#try..except ..else..finally
#else block runs only if no exeption occurs
#finally always run,exeption or not
try:
    age=int(input("enter your age :"))
except ValueError:
    print("enter a valid number")
else:
    print(f"hey,you are {age} years old")
finally:
    print("this always runs")