from classes import Course


class Student:
    username: str
    courses: list[Course]

    def __init__(self, username: str):
        self.username = username
        self.courses = []

    def add_course(self, code: Course):
        self.courses.append(code)

    def get_courses(self):
        return self.courses
