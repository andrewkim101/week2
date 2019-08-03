# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# dict2 = {'Name': 'Kara', 'Age': 15, 'Class': 'Economy'}
# print(type(dict))
# # cmp(dict, dict2)
# print(dict['Name'])
# dict['Age'] = 20
# print(dict['Age'])
# dict['Location'] = 'Brooklyn'
# print(dict)

# # del dict['Name']
# # print(dict)
# # dict.clear()
# # print(dict)
# # del dict
# # print(dict)
# for key, value in dict.items():
#     print(f"key: {key}")
#     print(f"value: {value}")

# person1 = {}
# person1['name']='Zara'
# person1['occupation']='specialist'
# person1['age']=25
# person1['isSingle']=True
# print(person1)

# person12 ={}
# person12['name']= 'Alina'
# person12['age']=25
# person12['sex']='F'
# person12['ethnicity']='asian'

# for k,v in person1.items():
#     print(k,v)


word = input("Input word:")
vowels = ['a','e','i','o','u']
res = {}
# for c in word:
#     if c in vowels:
#         res = res + c
# print(res)
for c in word:
    if c in vowels:
        if c in res:
            res[c]+=1
        else:
            res[c]=1
        

print(res)
print(f"Value {a} is used _ times")