myList = [1,2,'mom', ['mohammad hussain'],9,8]


# print(myList[2:4])

print(myList)

# Access the nested list
nested_list = myList[3]
print("nested_list : ",nested_list)

# Access the string within the nested list
full_name = nested_list[0]
print(full_name)


# Split the string to get the last name
last_name = full_name.split()[1]
print(last_name)


# Access and print "hussain" directly
print("myList[3][0].split()[1] : ",myList[3][0].split()[1])

