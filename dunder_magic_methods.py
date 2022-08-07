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

emp1 = Employee(["e1","e2", "e3","e4"])

