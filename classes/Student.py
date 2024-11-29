class student:
    courses: list[int]

    def __init__(self):
        self.courses = []

    def add_course(self, code: int):
        self.courses.append(code)
