#tuples-used to store multiple items in a single variable
#ordered and cannot be changed after creation(immutable)
fruits=("mangoes","apples","bananas","kiwi")
print(fruits)
print(type(fruits))
#accessing item using index
print(fruits[1])
#len()
print(len(fruits))
#loop
for fruit in fruits:
    print(fruit)