#creating,write,read
#open(filename,mode)
#mode-read(r),write(w),append(a)
#write(w)
#write()
f=open("demo.txt","w")
f.write("hello this is python")
f.close()
#r-read
#read()-to read the contents
x=open('demo.txt','r')
print(x.read())
x.close()
#append
y=open('demo.txt','a')
y.write("\n this is some appended text")
y.close()

#read() readline()readlines()
file=open('demo.txt','r')
print(file.read())
file.close()

