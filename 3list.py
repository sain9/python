# Task
# 1) Extract and print the string "goal" from the nested list.
# 2) Extract and print John's phone number ('123-456-7890') from the dictionary.

data = [
    42, 
    'hello', 
    [5, 'world', [10, {'key1': 'value1', 'key2': ['deep', 'dive', {'target': 'goal'}]}, 20]], 
    {'name': 'John', 'details': {'age': 30, 'city': 'New York', 'contacts': [{'type': 'email', 'value': 'john@example.com'}, {'type': 'phone', 'value': '123-456-7890'}]}}
]
dataEx = data[2][2][1]['key2'][2]['target']
print(dataEx)

phone = data[3]['details']['contacts'][1]['value']
print(phone)

# my_list = ['t', {'key1': 'vlaue1', 'key2': ['wow', {'key3': 'yo'}]}]

# # Access the value 'yo'
# yo_value = my_list[1]['key2'][1]['key3']

# print(yo_value)  # Output: yo
