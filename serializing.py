import json

person = {
    "FirstName": "Matin",
    "LastName": "Gardashov",
    "Hobbies" : [
        "Horse Riding",
        "Coding"
    ],
    "Age" : 20,
    "Programming Language" : [
        {
            "Name" : "Python",
            "Date" : 1970
        },
        {
            "Name" : "SQL",
            "Date" : 1989
        }
    ]   
}

print(person)
print(type(person))
print(person["FirstName"])

result = json.dumps(person,ensure_ascii=False,indent=2) # indent -> setirde ne qeder saga sutusdurmek lazimdir onu gosterir
print(result)
print(type(result))


with open('person.json','w') as file:
    json.dump(person,file,ensure_ascii=False,indent=3)