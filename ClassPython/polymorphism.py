# Polymorphism -> cok sekillilik yada cok cesitlilik demek
class Employee:

    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * raise_rate
        print('Employee:', result)

class CompEng(Employee):

    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100 * raise_rate
        print('Employee:', result)

class EEE(Employee):

    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100 * raise_rate
        print('Employee:', result)

e1 = Employee()
ce = CompEng()
eee = EEE()

employee_list = [e1, ce, eee]

for employee in employee_list:
    employee.raisee()
