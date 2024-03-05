from mod import Student, individual_method

student = Student(name='mitul', regNo='abc123456', rollNo='123987', standard='10', admissionYear='2024')

marks = {
    'Maths': 86,
    'Science': 82,
    'English': 86,
    'Social Science': 65
}

student.updateMarks(marks)
student.generateResult()
student.printStudent()

individual_method()
