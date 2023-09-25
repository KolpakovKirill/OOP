from page.page_people import Person
import random


class Teacher(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.num_students = 0

    def teach(self, material, *students):
        for student in students:
            student.take(material)
        self.num_students += 1


class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.knowledge = []

    def take(self, material):
        self.knowledge.append(material)    #добавляет переданный материал в конец списка

    def forget(self):
        if self.knowledge:
            index = random.randint(0, len(self.knowledge) - 1)   # len определения длины списка
            self.knowledge.pop(index)

    def __len__(self):                 # Когда вызывается функция len() для объекта класса Student, будет возвращена длина списка
        return len(self.knowledge)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Knowledge: {self.knowledge}"


class LearningMaterial:
    def __init__(self, *materials):
        self.materials = list(materials)

    def __len__(self):                  #возвращает длину списка
        return len(self.materials)

    def __str__(self):
        return f"Number of materials: {len(self.materials)}"


materials = LearningMaterial("Python", "Version Control Systems", "Relational Databases", "NoSQL databases", "Message Brokers")
teacher = Teacher("Иванов", 35, "М")
student1 = Student("Петрова", 27, "Ж")
student2 = Student("Сидорова", 24, "Ж")
student3 = Student("Попов", 30, "М")
student4 = Student("Смирнов", 29, "М")

teacher.teach(materials.materials[0], student1, student2)
teacher.teach(materials.materials[1], student2, student3, student4)
teacher.teach(materials.materials[2], student1, student3, student4)
teacher.teach(materials.materials[3], student1, student2, student3)
teacher.teach(materials.materials[4], student4)

print(f"{student1.name} (Возраст: {student1.age}, Пол: {student1.gender}) Список знаний: {student1.knowledge}")
print(f"{student2.name} (Возраст: {student2.age}, Пол:: {student2.gender}) Список знаний: {student2.knowledge}")
print(f"{student3.name} (Возраст: {student3.age}, Пол:: {student3.gender}) Список знаний: {student3.knowledge}")
print(f"{student4.name} (Возраст: {student4.age}, Пол:: {student4.gender}) Список знаний: {student4.knowledge}")

print(len(materials))
print(len(student1))
print(len(student2))
print(len(student3))
print(len(student4))

student1.forget()
student2.forget()
student3.forget()
student4.forget()

print(f"\nAfter forgetting:")
print(f"{student1.name} (Возраст: {student1.age}, Пол: {student1.gender}) Список знаний: {student1.knowledge}")
print(f"{student2.name} (Возраст: {student2.age}, Пол:: {student2.gender}) Список знаний: {student2.knowledge}")
print(f"{student3.name} (Возраст: {student3.age}, Пол:: {student3.gender}) Список знаний: {student3.knowledge}")
print(f"{student4.name} (Возраст: {student4.age}, Пол:: {student4.gender}) Список знаний: {student4.knowledge}")