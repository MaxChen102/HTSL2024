from classes import Student, Course, CourseOrganizer, Room


# Initializing organizer
organizer = CourseOrganizer()
students = []
courses = []
rooms = []

# reading the courses data
f = open("test_course1", "r")
line = f.readline()
while line != "":
    if line == int(line):
        time = int(line)
    elif line == str(line):
        contain = False
        for student in students:
            if student.username == str(line):
                contain = True
        if not contain:
            students.append(Student(str(line)))
    else:
        courses.append(Course(line))
    line = f.readline()

# reading the rooms data
f = open("rooms", "r")


# setting
organizer.set_students(students)
organizer.set_courses(courses)
organizer.set_rooms(rooms)

# adding the weight
organizer.set_all_weight_enrollment()

# making empty schedule


# ML stuff

