#list-used to store multiple items in a sigle variable
#lists are ordered,allow duplicates  and cn be modifed(mutable)
courses=["html","css","python","django"]
print(courses)
print(type(courses))
#accessing list item using index[]
print(courses[0])
print(courses[2])
#change list item
courses[1]="javascript"
print(courses)
#list methods append()
#append()-adds an element to the end of the list
courses.append("kotlin")
print(courses)
#insert()-adds an element at a specific index
courses.insert(2,"bootstrap")
print(courses)
#sort()-alaphabetically
courses.sort()
print(courses)
# len()-number of items
print(len(courses))
#remove()-removes an item
courses.remove("html")
print(courses)
#loop
for course in courses:
    print(course)

