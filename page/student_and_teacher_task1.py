from page.page_people import Person
class Teacher(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.name = name
        self.num_students = 0

    def teach(self, material, *students):
        for student in students:
            student.take(material)
        self.num_students += 1


class Student(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.name = name
        self.knowledge = []

    def take(self, material):
        self.knowledge.append(material)


class LearningMaterial:
    def __init__(self, *materials):
        self.materials = list(materials)


# Test the program
materials = LearningMaterial("Математика", "Физика", "Python", "SQL",
                             "Физкультура")
teacher = Teacher("Иванов", 35, "М")
student1 = Student("Петрова", 27, "Ж")
student2 = Student("Сидорова", 24, "Ж")
student3 = Student("Попов", 30, "М")
student4 = Student("Смирнов", 29, "М")

teacher.teach(materials.materials[0], student1, student2)      #5 раз вызовите метод teach
teacher.teach(materials.materials[1], student2, student3, student4)
teacher.teach(materials.materials[2], student1, student3, student4)
teacher.teach(materials.materials[3], student1, student2, student3)
teacher.teach(materials.materials[4], student4)

print(f"{student1.name} knowledge: {student1.knowledge}")
print(f"{student2.name} knowledge: {student2.knowledge}")
print(f"{student3.name} knowledge: {student3.knowledge}")
print(f"{student4.name} knowledge: {student4.knowledge}")