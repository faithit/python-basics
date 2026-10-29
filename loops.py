#loop executes a block 
#FOR LOOP
""" for variable in collection:
        block of code"""
#loop through a list
students=["mary","john","cate","kamau"]
print(type(students))
for x in students:
    print(x)
#loop through a string
for y in "javascript":
    print(y)
#range(stop)
#loop through a range
for i in range(7):
    print(i)
#loop through a range(start,stop)
for a in range(3,9):
    print(a)
#loop throgh a range(start,stop,step)
for b in range(2,10,2):
    print(b)
#break is used to terminate a loop
for c in "python":
    if c=="h":
        break
    print(c)
#continue
for z in range(1,5):
    if z==3:
        continue
    print(z)
