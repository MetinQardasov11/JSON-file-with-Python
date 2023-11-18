import json

db = {
    "Users" : {
        "MatinGardashov" : {
            "FirstName" : "Matin",
            "LastName" : "Gardashov"
        },
        "OmarOsmanov" : {
            "FirstName" : "Omar",
            "LastName" : "Osmanov"
        }
    },
    "Products" : {
        "1" : {
            "ProductName" : "Iphone 13 pro max",
            "Price" : 1200
        },
        "2" : {
            "ProductName" : "Iphone X",
            "Price" : 700
        },
        "3" : {
            "ProductName" : "Iphone 11 pro",
            "Price" : 900
        }
    }
}

# with open('db.json','w') as file:
#     json.dump(db, file, ensure_ascii=False, indent=4)


with open('db.json') as file:
    db = json.load(file)
# print(db)
# print(db['Users']['MatinGardashov']['FirstName'])
# print(db['Products']['1']['Price'])


db['Products'].update({
    "4" : {
        "ProductName": "Iphone 15",
        "Price": 1500
    }
})


db['Users'].update({
    "EbubekirAliyev" : {
        "FirstName": "Ebubekir",
        "LastName": "Aliyev"
    },
    "AliOmarov" : {
        "FirstName": "Ali",
        "LastName": "Omarov"
    }
})




with open('db.json','w') as file:
    json.dump(db, file, ensure_ascii=False, indent=4)