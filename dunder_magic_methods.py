class Employee:
    def __new__(self, emp_list):
        print("I am in __new__ dunder method.")
        self.emp_list = emp_list
        self.emp_list.append("e5") 
        print("emp_list modified in __new__ dunder method.")
        return object.__new__(self)
    
    def __init__(self, emp_list):
        print("I am in __init__ dunder method.")
        print(self.emp_list)
    
    def __add__(self, emp):
        print("i am in __add__ dunder method")
        return  ",".join(self.emp_list) + ", "+ emp
    
    def __getitem__(self, index):
        print("I am in __getitem__ dunder method.")
        return self.emp_list[index]
    
    def __setitem__(self, index, item):       
        print("I am in __setitem__ dunder method.")
        self.emp_list[index] = item
    
    def __contains__(self, item):
        print ("I am in __contains__ dunder method")
        return item in self.emp_list
    
    
emp1 = Employee(["e1","e2", "e3","e4"])  # calls __new__()  first then __init__()
#print(emp1 + "e7") calls __add__()
#print(emp1[3])  calls __getitem__()
#emp1[3] = "e5"  calls __setitem__()
#print(emp1.emp_list)  prints all the elements on the emp_list
#print("e4" in emp1) calls __contains__()
#

