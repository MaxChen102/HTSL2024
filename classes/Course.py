from matplotlib.font_manager import weight_dict

from classes import Student


class Course:
    code: str
    weight: dict[str, int]
    enrollment: int

    def __init__(self, code: str):
        self.code = code
        self.enrollment = 0
        self.weight = {}

    # use student list to determine course capacity and weighting
    def get_values(self, all_students: list[Student]):
        self.enrollment = 0
        self.clear_weight()
        for student in all_students:
            courses = student.get_courses
            if self.code in courses:
                self.enrollment += 1
                self.update_weight(courses)

    def update_weight (self, enrolled_courses: list[str]):
        for course in enrolled_courses:
            if course is not self.code:
                self.weight.setdefault(course, 0)
                self.weight[course] += 1

    def clear_weight (self):
        for course in self.weight:
            self.weight[course] = 0






