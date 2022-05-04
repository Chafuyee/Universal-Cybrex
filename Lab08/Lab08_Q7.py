def br():
    print("=" * 20)

br()

class Student:

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.total_marks = []

    def __str__(self):
        indicator = ""
        average_grade = 0
        marks_list = sorted(self.total_marks)
        if len(marks_list) == 0:
            overall_grade = -1
        else:
            overall_grade = sum(marks_list)
            average_grade = overall_grade / len(marks_list)
        if average_grade >= 50:
            indicator = "PASS"
        elif (0 <= average_grade < 50) and (len(self.total_marks) != 0):
            indicator = "FAIL"
        return str(self.name) + " " + str(marks_list) + " " + "(" + indicator + ")"

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.total_marks += [mark]
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        else:
            return self.id_number == other.id_number


aaron = Student('Aaron', '12345')
brittany = Student('Brittany', '23456')

print(aaron)
print(brittany)

aaron.add_mark(25)
brittany.add_mark(75)

print(aaron)
print(brittany)

aaron.add_mark(100)
brittany.add_mark(10)

print(aaron)
print(brittany)

student = Student('Charles', '23456')

print(student, aaron, student == aaron)
print(student, brittany, student == brittany)

br()