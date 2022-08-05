fruits = ["pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)
fruits.insert(0,"Orange")
print(fruits)
fruits.append("Peach")
print(fruits)
print(len(fruits))
# removing elements from a list

fruits.remove("Banana")
fruits.pop(2)
print(fruits)

fruits[2] = "Strawberry"
print(fruits)

