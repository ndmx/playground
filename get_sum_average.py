input_string = input("Enter list elements seperated by space ")
print("\n")
user_list = input_string.split()

print("list: ", user_list)

sum = 0
length = 0
for value in user_list:
    sum +=int(value)
    length +=1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))