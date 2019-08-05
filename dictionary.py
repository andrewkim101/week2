# # dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# # dict2 = {'Name': 'Kara', 'Age': 15, 'Class': 'Economy'}
# # print(type(dict))
# # # cmp(dict, dict2)
# # print(dict['Name'])
# # dict['Age'] = 20
# # print(dict['Age'])
# # dict['Location'] = 'Brooklyn'
# # print(dict)

# # # del dict['Name']
# # # print(dict)
# # # dict.clear()
# # # print(dict)
# # # del dict
# # # print(dict)
# # for key, value in dict.items():
# #     print(f"key: {key}")
# #     print(f"value: {value}")

# # person1 = {}
# # person1['name']='Zara'
# # person1['occupation']='specialist'
# # person1['age']=25
# # person1['isSingle']=True
# # print(person1)

# # person12 ={}
# # person12['name']= 'Alina'
# # person12['age']=25
# # person12['sex']='F'
# # person12['ethnicity']='asian'

# # for k,v in person1.items():
# #     print(k,v)


# word = input("Input word:")
# vowels = ['a','e','i','o','u']
# res = {}
# # for c in word:
# #     if c in vowels:
# #         res = res + c
# # print(res)
# for c in word:
#     if c in vowels:
#         # if c in res:
#         #     res[c]+=1
#         # else:
#         #     res[c]=1
#         #setdefault
#         res.setdefault(c,0)
#         res[c] +=1

# print(f"Phrase was given: {word}")
# for key, value in res.items():
#     print(f"Value {key} is used {value} times")

# phrase = input("Enter phrase:")
# print(f"Phrase length {len(phrase)}")

lily ={"name":"Lily", "kind":"cat","owner":"Alisa"}
mao ={"name":"Mao","kind":"dog","owner":"Anya"}
horse ={"name":"Pony","kind":"horse","owner":"Alyona"}
pets = [lily,mao,horse]

for el in pets:
    print(f"{el['name']} is a {el['kind']}, it's {el['owner']}'s pet ")


lily ={"name":"Lily", "kind":"cat","owner":"Alisa"}
mao ={"name":"Mao","kind":"dog","owner":"Anya"}
horse ={"name":"Pony","kind":"horse","owner":"Alyona"}
pets_dict = {}
pets_dict['1']=lily
pets_dict['2']=mao
pets_dict['3']=horse
#print(pets_dict)
for key, value in pets_dict.items():
    print(f"{key}. {value['name']} is a {value['kind']}, it's {value['owner']}'s pet ")
