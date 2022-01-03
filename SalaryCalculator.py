from abc import ABCMeta, abstractmethod
class Employee(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self):
        return 15000

class Programmer(Employee):

    def __init__(self, name, hours=0):
        # super(Programmer, self).__init__(name)
        super().__init__(name)
        self._hours = hours
    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        self._hours = hours if hours > 0 else 0

    def get_salary(self):
        return 150 * self._hours


class Salesman(Employee):

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200 + self._sales * 0.05

def main():
    employees = [Manager('Lee'), Programmer('Sin'), Programmer('Yen'), Salesman('Min')]
    for emp in employees:
        if isinstance(emp, Programmer):
            emp.hours = int(input("Please enter number of work hours for %s : " %emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input ("Please enter the total amount of sales by %s : " %emp.name))
        print("The total salary for %s is : %s" %(emp.name, emp.get_salary()))

if  __name__  ==  "__main__" :
     main ()



