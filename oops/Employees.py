

from multiprocessing import managers


class Employee:
    def __init__(self,name,lastName) -> None:
        self.name=name
        self.lastName=lastName
class Manager(Employee):
    def __init__(self, name, lastName,managerName) -> None:
        super().__init__(name, lastName)
        self.managerName=managerName
    def printDetails(self):
        print(self.name+" "+self.lastName+" Working with "+self.managerName)
class Salary(Manager):
    def __init__(self, name, lastName, managerName,Salary) -> None:
        super().__init__(name, lastName, managerName)
        self.Salary=Salary
    def salaryDetails(self):
        print("Hike of 50% "+str(self.name)+" "+str(self.lastName)+" 700000")

santhosh=Salary("santhosh","vempali","siddharth",45000)
santhosh.printDetails()
santhosh.salaryDetails()

