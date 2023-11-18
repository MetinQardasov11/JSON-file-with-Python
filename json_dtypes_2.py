import json

data = {
    "MatinGardashov": {
        "FirstName": "Matin",
        "LastName": "Gardashov"
    },
    "OmarOsmanov" : {
        "FirstName": "Omar",
        "LastName": "Osmanov"
    }
}

# with open('users2.json','w') as file:
#     json.dump(data,file,ensure_ascii=False,indent=4)
    

with open('users2.json') as file:
    users = json.load(file)
# print(users)
# print(users['MatinGardashov'])


users.update({
    "EbubekirAliyev": 
        {
            "FirstName": "Ebubekir",
            "LastName": "Aliyev",
            "Age" : 30
        }
})


# users.pop("MatinGardashov")

with open('users2.json','w') as file:
    json.dump(users,file,ensure_ascii=False,indent=4)
