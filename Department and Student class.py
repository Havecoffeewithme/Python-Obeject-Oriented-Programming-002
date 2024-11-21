

# class department

class Department():
    def __init__(self, dept, chair):
        self.deptName = dept
        self.director = chair

    # returning the object
    def __str__(self):
        return self.deptName


class Student():
    def __int__(self, name, major, crs):
        self.name =  name
        self.major = major
        self.course = [crs]

    def __str__(self):
        return f"student {self.name} in {self.major} has the classes {self.course}"

    # adding more courses
    def add(self, crs):
        self.course.append(crs)


    # getting GPA based on the class grades
    def calcGPA(self, **grades):
        noClasses = len(grades.keys())
        sum = 0
        for each in grades:
            if grades[each] == "A":
                sum += 4.25
            elif grades[each] == "A-":
                sum += 4.0
            elif grades[each] == "B+":
                sum += 3.67
            elif grades[each] == "B":
                sum += 3.33
            elif grades[each] == "B-":
                sum += 3.0
            elif grades[each] == "C+":
                sum += 2.67
            elif grades[each] == "C":
                sum += 2.3
            elif grades[each] == "C-":
                sum += 2.0
            elif grades[each] == "F":
                sum += 0
            return sum/noClasses


class Section():
    students = {}
    instructor = ""
    title = ""

    def __init__(self, stuD, inst, tit):
        self.students = {stuD}
        self.instructor = inst
        self.title = tit

    def __str__(self):
        return "students {} enrolled in {} taught by {}".format(self.students, self.title, self.instructor)

    def grading(self, grade):
        if grade > 90 :
            lGrade = "A"
        elif grade > 80 :
            lGrade = "B"
        elif grade > 70 :
            lGrade = "C"
        elif grade > 60 :
            lGrade = "D"
        else:
            lGrade = "F"
        return lGrade

# department
dept1 = Department("IT", "Letlotlo")
dept2 = Department("Maintance", "Victor")

# section
sec1 = Section("Lee", "Java", "001")
sec2 = Section( "vIC", "C++", "002")

# objects of student
# stud1 = Student("Bob", dept1, [])

print(sec1)

















