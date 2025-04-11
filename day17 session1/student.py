class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
       
 
    def __repr__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade})"
 
 