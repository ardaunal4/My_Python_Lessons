from untitled0 import website

class website1(website):
    def __init__(self, name, surname, ids):
        website.__init__(self, name, surname) 
        self.ids = ids
        
    def login(self):
        print(self.name + ' ' + self.surname + ' ' + self.ids)
        
user1 = website('name', 'surname')
user1.loginInfo()
#%%

user2 = website1('name', 'surname', '123')
user2.login() # from childe class
user2.loginInfo() # from parent class
print(user2.name)