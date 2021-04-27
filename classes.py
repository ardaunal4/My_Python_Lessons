import datetime
# class user:
#     pass # passes line and that does nothing

# user1 = user() # object
# user1.first_name = "AHmet"
# user1.last_name = "Besr"

# print(user1.first_name)
# first_name = 'Arthur'
# second_name = 'Clark'

# user2 = user()
# user2.first_name, user2.second_name = first_name, second_name
# print(user2.first_name)

#Class Features
class User:
    """ Docstring explains the duty of class here when class call with help function"""
    #try with help(user)
    def __init__(self, full_name, birthday): #initialization function
        self.name = full_name
        # left birthday represents field that stores the value and right birthday user input
        self.birthday = birthday  #yyyymmdd
        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    def age(self):
        """Return age of user in years."""
        today = datetime.date(2001, 5, 12)
        yyyy = self.birthday[0:4]
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(int(yyyy), mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User("Dave Bowman", 19710315)
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)
print(user.age())





