from project import Employee
from python_oop_part_2.inheritance.exr.person.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
