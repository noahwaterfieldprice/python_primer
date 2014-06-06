# Exercise 7.39


class Course:

    def __init__(self, course_name, semester, credit, grade):
        self.course_name = course_name
        self.semester = semester
        self.credit = int(credit)
        self.grade = grade

    def __str__(self):
        s = 'course name: ' + self.course_name + \
            ', semester: ' + self.semester + \
            ', credit: ' + str(self.credit) + \
            ', grade: ' + self.grade
        return s

    def __repr__(self):
        return self.__str__()


class Student:

    def __init__(self, name, courses):
        self.name = name
        self.courses = courses  # list of Course instances

    def __str__(self):
        return pprint.pformat(self.courses)

    def __repr__(self):
        return self.__str__()


def load(studentfile):
    infile = open(studentfile, 'r')
    data = {}
    for line in infile:
        i = line.find('Name:')
        if i != -1:
            # line contains 'Name:', extract the name
            name = line[i + 5:]
            name = name.strip()  # strip off blanks
            student = Student(name, [])
            data[name] = student
        elif line.isspace():     # blank line?
            continue             # go to next loop iteration
        else:
            # This must be a course line
            words = line.split()
            grade = words[-1]
            credit = int(words[-2])
            semester = ' '.join(words[-4:-2])
            course_name = ' '.join(words[:-4])
            course = Course(course_name, semester, credit, grade)
            student.courses.append(course)
    infile.close()
    return data

grade2number = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
number2grade = {}  # "inverse" of grade2number
for grade in grade2number:
    number2grade[grade2number[grade]] = grade


def average_grade(data, name):
    sum = 0
    weights = 0
    for course in data[name].courses:
        weight = course.credit
        sum += grade2number[course.grade] * weight
        weights += weight
    avg = sum / float(weights)
    return number2grade[round(avg)]

if __name__ == '__main__':
    data = load('students.dat')
    import pprint
    pprint.pprint(data)

    # Sort keys in data after the last name
    def sort_names(name1, name2):
        last_name1 = name1.split()[-1]
        last_name2 = name2.split()[-2]
        if last_name1 < last_name2:
            return -1
        elif last_name1 > last_name2:
            return 1
        else:
            return 0

    print '\nAverage grades:'
    for name in sorted(data, sort_names):
        print '%s: %s' % (name, average_grade(data, name))


"""
Sample run:
python Student_Course.py
{'Jan Modaal': [course name: Calculus I, semester: 2005 fall, credit: 10, grade: A,
 course name: Calculus II, semester: 2006 spring, credit: 10, grade: A,
 course name: Introductory C++ Programming, semester: 2005 fall, credit: 15, grade: D,
 course name: Introductory Python Programming, semester: 2006 spring, credit: 5, grade: A,
 course name: Astronomy, semester: 2005 fall, credit: 10, grade: A,
 course name: Basic Philosophy, semester: 2005 fall, credit: 10, grade: F],
 'John Doe': [course name: Astronomy, semester: 2003 fall, credit: 10, grade: A,
 course name: Introductory Physics, semester: 2003 fall, credit: 10, grade: C,
 course name: Calculus I, semester: 2003 fall, credit: 10, grade: A,
 course name: Calculus II, semester: 2004 spring, credit: 10, grade: B,
 course name: Linear Algebra, semester: 2004 spring, credit: 10, grade: C,
 course name: Quantum Mechanics I, semester: 2004 fall, credit: 10, grade: A,
 course name: Quantum Mechanics II, semester: 2005 spring, credit: 10, grade: A,
 course name: Numerical Linear Algebra, semester: 2004 fall, credit: 5, grade: E,
 course name: Numerical Methods, semester: 2004 spring, credit: 20, grade: C],
 'Kari Nordmann': [course name: Introductory Python Programming, semester: 2006 spring, credit: 5, grade: A,
 course name: Astronomy, semester: 2005 fall, credit: 10, grade: D]}

Average grades:
John Doe: B
Kari Nordmann: C
Jan Modaal: C
"""
    
