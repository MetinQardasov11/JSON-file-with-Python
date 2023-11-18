import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        self.loadUser()
    
    
    def loadUser(self):
        if os.path.exists('Users_menu.json'):
            with open('Users_menu.json','r') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user['username'],password=user['password'],email=user['email'])
                    self.users.append(newUser)
            print(self.users)
                
                
    def register(self, user: User):
        self.users.append(user)
        self.saveToFiles()
        print('User successfully registered !!!...')
        
        
    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Login successful !!!...')
                break
            else:
                self.isLoggedIn = False
                print('Login failed !!!...')

        
    def logOut(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Logout successful !!!...')
    
    def identity(self):
        if self.isLoggedIn:
            print(f'Username: {self.currentUser.username}')
        else:
            print('Not logged in !!!...')
    
    
    def saveToFiles(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        
        with open('Users_menu.json','w') as file:
            json.dump(list, file,ensure_ascii=False,indent=4)


repository = UserRepository()


while True:
    print(' Menu '.center(40,'*'))
    choice = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nYour choice: ')
    
    if choice == '5':
        break
    else:
        if choice == '1':
            username = input('Username: ')
            password = input('Password: ')
            email = input('Email: ')
            
            user = User(username,password,email)
            repository.register(user)
            
        elif choice == '2':
            if repository.isLoggedIn:
                print('You already have logged in !!!...')
            else:
                username = input('Username: ')
                password = input('Password: ')
                repository.login(username,password)    
        elif choice == '3':
            repository.logOut()
        elif choice == '4':
            repository.identity()
        else:
            print('Invalid choice !!!...')