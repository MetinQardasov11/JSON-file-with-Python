import json

data = [
{
    "UserName" : "MetinGardashov",
    "FirstName" : "Metin",
    "LastName" : "Gardashov"
},
{
    "UserName" : "OmarOsmanov",
    "FirstName" : "Omar",
    "LastName" : "Osmanov"
},
{
    "UserName" : "HuseyinHasanov",
    "FirstName" : "Huseyin",
    "LastName" : "Hasanov"
},
{
    "UserName" : "EbubekirAliyev",
    "FirstName" : "Ebubekir",
    "LastName" : "Aliyev"
}
]


user = {
    "UserName" : "AliOmarov",
    "FirstName" : "Ali",
    "LastName" : "Omarov"
}   


with open('users.json') as file:
    users = json.load(file)

# users.append(user)

# for user in users:
#     if user['FirstName'] == 'Metin':
#         user['FirstName'] = 'Matin'
        

# users.remove(users[5])

# with open('users.json','w') as file:
#     json.dump(users, file,ensure_ascii=False,indent=4)