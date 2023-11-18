import json

with open('person.json') as file:
    data = file.read()
print(data)
print(type(data))



# OR


with open('person.json') as file:
    data = json.load(file)
print(data)
print(type(data))
print(data['LastName'])
print(data['Hobbies'])
print(data['Hobbies'][0])
print(data['Programming Language'][1]['Name'])



# OR


data = """
    {
        "FirstName": "Matin",
        "LastName": "Gardashov",
        "Hobbies" : ["Horse Riding","Coding"],
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
    """
    
new_data = json.loads(data)
print(new_data)
print(type(new_data))
print(new_data['FirstName'])
print(new_data['Age'])
print(new_data['Hobbies'][1])
print(new_data['Programming Language'][0]['Name'])