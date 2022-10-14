from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class company(Employee):
    def salary(self):
        name=input("enter ur name := ")
        return  name
names=[]
company=company()
ans=company.salary()
names.append(ans)
print(*names)