#Student_manager.py
import json
from student import Student
from storage import Storage
 
class StudentManager:
    def __init__(self):
        self.students = []
        self.storage = Storage("students.json")
        self.load_data()
 
    def load_data(self):
        data = self.storage.load()
        for student_data in data:
            student = Student(student_data)
            self.students.append(student)
 
    def save_data(self):
        student_data = [vars(student) for student in self.students]
        self.storage.save(student_data)
 
    def add_student(self, name, age, grade):
        student_id = len(self.students) 
        student = Student(student_id, name, age, grade)
        self.students.append(student)
        self.save_data()
 
    def get_all_students(self):
        return self.students
 
    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
 
    def delete_student(self, student_id):
        student = self.get_student_by_id(student_id)
        if student:
            self.students.remove(student)
            self.save_data()
            return True
        return False
 
