#a module  is afile containing python code(functions,variables)
#built in modules eg math,random,datetime,os
import math
import os
import random 
import datetime
print(math.pi)
print(math.sqrt(36))
print(os.getcwd())
# os.mkdir("hello")
# print("hello created  successfully")
# help(os)
#random num btwn 0-1
print(random.random())
#random  intergers btw 6-19
print(random.randint(6,19))
#print current date
print(datetime.date.today())
#print current date and time
print(datetime.datetime.now())
#check if file exists
if os.path.exists("demo.txt"):
    print("file exists")
else:
    print("file does not exist")
