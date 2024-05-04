class Student:
    def __init__(self,name,roll_num,password):
        self.name=name
        self._roll_num=roll_num
        self.__password=password
    def display_details(self):
        print("Name:",self.name)
        print("Roll_number:",self._roll_num)
        print("Password:",self.__password)
    def get_password(self):
        return self.__password
student=Student("Alice","A001","secure_password")
print("Name(public):",student.name)
print("Roll number(Protected):",student._roll_num)
print("password(private):",student.get_password())
