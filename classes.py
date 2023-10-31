class Diary:
    def __init__(self, pages, marks):
        self.pages = pages
        self.marks = marks
    def netik(self):
        return f"страниц мало{self.pages} и плохие оценки {self.marks}"  
        
class Subject:
    def __init__(self,name):
        self.name = name
    def info (self):
        return f"{self.name}
class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def description(self):
        return f"Students name {self.name}, surname {self.surname} and his age {self.age}"
        
d1 = Diary(12,5)
d1.netik()
s1 = Subject("math")
s1.info()
st = Student("Aijan", "Tashkulova", "19")
st.description()
