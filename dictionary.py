#stores data in key:value pairs
student={
    "name":"mary",
    "age":19,
    "course":"python"
}
print(student)
print(type(student))
#accessing values[]
print(student["name"])
print(student["course"])
#add key:value pair
student["town"]="nairobi"
print(student)
#change value
student["name"]="john"
print(student)
#keys()-returns all keys()
print(student.keys())
#values-returns all values
print(student.values())
#items()-returns key:value pairs
print(student.items())
#loop
for x,y in student.items():
    print(x,":",y)