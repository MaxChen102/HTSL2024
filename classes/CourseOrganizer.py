from classes import Course, Student


class CourseOrganizer:
    all_courses: list[Course]
    all_students: list[Student]

    def __init__(self):
        self.all_courses = []
        self.all_students = []

    def set_students(self, list_students: list[Student]):
        self.all_students = list_students

    def set_courses(self, list_courses: list[Course]):
        self.all_courses = list_courses

    def set_all_weight_enrollment(self):
        for student in self.all_students:
            for course in student.get_courses:
                course.add_student()
                set_weight(course, student.get_courses)

def set_weight(c: Course, c_list: list[Course]):
     for course in c_list:
        if c.get_code is not course.get_code():
            c.set_weight(course)


