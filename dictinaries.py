dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict2 = {'Name': 'Kara', 'Age': 15, 'Class': 'Economy'}
print(type(dict))
# cmp(dict, dict2)
print(dict['Name'])
dict['Age'] = 20
print(dict['Age'])
dict['Location'] = 'Brooklyn'
print(dict)

# del dict['Name']
# print(dict)
# dict.clear()
# print(dict)
# del dict
# print(dict)
for key, value in dict.items():
    print(f"key: {key}")
    print(f"value: {value}")

for i in range(3):
    for j in  range(3):
        print("#", end="")
    print()
