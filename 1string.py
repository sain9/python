
str = 'hussain'
greet = ',good morning!'

#concatenation
print(str + greet)


print(f"str = {str}, len = ",len(str))
# print(f"str = {str}, len = ",len(greet))

print("str[0] :",str[0])

print(str)
print("from index 0 up to (but not including) index 4.")
print("str[0:4] :",str[0:4])
print("from the beginning up to (but not including) index 4.")
print("str[:4] :",str[:4])
print("from index 4 to the end of the string")
print("str[4:] :",str[4:])
print("from index 3 up to (but not including) index 7")
print(str[3:7])

print("str*2 : ",str*2)
print("\n",greet)
print("greet.split(' ') : ",greet.split(' '))# splitted by space
print("greet.split(',') : ",greet.split(','))# splitted by ,
print('note: split takes a single argument and a delimeter and provides list ,separated upon delimeter (like space or ,)')

st = ' hi how are you, '

print(st + 'buddy')
print("strip() removes the initial(left) and end(right) blank spaces ")
print(st.strip() + 'buddy')
print("rstrip() removes the end(right) blank spaces only ")
print(st.rstrip() + 'buddy')

