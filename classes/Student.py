from classes import Course


class Student:
    courses: list[Course]

    def __init__(self):
        self.courses = []

    def add_course(self, code: Course):
        self.courses.append(code)

    def get_courses(self):
        return self.courses
