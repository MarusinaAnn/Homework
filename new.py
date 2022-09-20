class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avgrade(self):
        result = (sum(*self.grades.values()) / len(*self.grades.values()))
        return result

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания:{self._avgrade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self._avgrade() < other._avgrade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avgrade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result

    def __str__(self):
        res = '\n'f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции:{self._avgrade()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self._avgrade() < other._avgrade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = '\n'f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n'
        return res


student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Anna', 'Brown', 'female')
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Alice', 'One')
reviewer2.courses_attached += ['Git']

lecturer1 = Lecturer('Alex', 'Smith')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Kate', 'Tig')
lecturer2.courses_attached += ['Git']

student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Git', 8)

reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Git', 7)

student1.add_courses('Power BI')

student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]


def avg_grade_st(student_list, course):
    for student in student_list:
        for key, value in student.grades.items():
            if key == course:
                avggr = sum(student.grades[key]) / len(student.grades.values())
                print(f'Cредняя оценка за домашние задания: {avggr}')


def avg_grade_lect(lecturer_list, course):
    for lecturer in lecturer_list:
        for key, value in lecturer.grades.items():
            if key == course:
                avggrlec = sum(lecturer.grades[key]) / len(lecturer.grades.values())
                print(f'Cредняя оценка за лекции: {avggrlec}')


print(student1)
print(student1 < student2)
print(lecturer1)
print(lecturer1 < lecturer2)
print(reviewer1)
print(reviewer2)
print(student1.grades)
print(student2.grades)
avg_grade_st(student_list, 'Git')
avg_grade_lect(lecturer_list, 'Git')
print(student2.courses_in_progress)
print(student1.finished_courses)