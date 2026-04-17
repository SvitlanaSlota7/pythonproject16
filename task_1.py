class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Привіт, мене звати {self.name}, мені {self.age} років."

    def get_role(self):
        return "Людина"

class Student(Person):
    """Клас для учнів успадковує Person."""
    def __init__(self, name: str, age: int, gender: str, grade_level: int):
        super().__init__(name, age, gender)
        self.grade_level = grade_level  # 10-й клас
        self.grades = []                # Список оцінок

    def add_grade(self, grade: int):
        """Специфічний метод для учня"""
        if 1 <= grade <= 12:
            self.grades.append(grade)
            print(f"Оцінку {grade} додано для {self.name}.")

    def get_average_score(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_role(self):
        return f"Учень {self.grade_level}-го класу"


class Teacher(Person):
    """Клас для вчителів успадковує Person"""
    def __init__(self, name: str, age: int, gender: str, subject: str, salary: float):
        super().__init__(name, age, gender)
        self.subject = subject  # Предмет, який викладає вчитель
        self.salary = salary    # Зарплата вчителя

    def set_salary(self, new_salary: float):
        """Метод для зміни зарплати."""
        self.salary = new_salary
        print(f"Зарплату вчителя {self.name} оновлено.")

    def get_role(self):
        return f"Вчитель предмету {self.subject}"

math_teacher = Teacher("Олександр Петрович", 45, "Чоловік", "Математика", 15000.0)
student_ivan = Student("Іван", 15, "Чоловік", 9)

print(math_teacher.introduce())
print(student_ivan.introduce())

student_ivan.add_grade(11)
student_ivan.add_grade(9)
print(f"Середній бал Івана: {student_ivan.get_average_score()}")

print(f"Роль вчителя: {math_teacher.get_role()}")
print(f"Зарплата вчителя: {math_teacher.salary} грн")