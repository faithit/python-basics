# with ..as
with open("chrome.txt","w") as f:
    f.write("hello this python file handling")
    f.write(" \n files")
#read
with open("chrome.txt","r") as file:
    print(file.read())