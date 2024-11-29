from matplotlib.font_manager import weight_dict

from classes import Student


class Course:
    code: str
    weight: dict[str, int]
    enrollment: int
    exam: int
    start: int
    end: int

    def __init__(self, code: str):
        self.code = code
        self.enrollment = 0
        self.weight = {}
        self.exam = 0
        self.start = 0
        self.end = 0

    def get_code(self):
        return self.code

    def set_weight (self, course_code: str):
        self.weight.setdefault(course_code,0)
        self.weight[course_code]+=1

    def add_student (self):
        self.enrollment+=1




