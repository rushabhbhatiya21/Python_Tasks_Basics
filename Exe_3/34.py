from prettytable import PrettyTable


class Student:
    def __init__(self, name: str, regNo: str, rollNo: str, standard: str, admissionYear: str) -> None:
        self.name = name if name.isalpha() else print("Invalid Student Name")
        self.regNo = regNo if regNo.isalnum() else print("Invalid Reg Number")
        self.rollNo = rollNo if rollNo.isnumeric() else print("Invalid Roll Number")
        self.standard = standard if standard.isnumeric() else print("Invalid Standard")
        self.admissionYear = admissionYear if admissionYear.isnumeric() else print("Invalid admission year")
        self.marks = dict()

    def update_marks(self, marks: dict):
        self.marks.update(marks)
        # print(self.marks)

    def generate_result(self):
        determineRes = lambda val: 'Pass' if val >= 40 else 'Fail'
        self.marks = {key: {'Marks': value, 'Result': determineRes(value)} for key, value in self.marks.items()}
        # print(self.marks)

    def calculate_grade(self, percentage):
        if type(percentage) is str:
            return 'F'
        else:
            if percentage >= 95:
                return 'O+'
            elif 95 > percentage >= 90:
                return 'O'
            elif 90 > percentage >= 85:
                return 'A+'
            elif 85 > percentage >= 80:
                return 'A'
            elif 80 > percentage >= 75:
                return 'B+'
            elif 75 > percentage >= 70:
                return 'B'
            elif 70 > percentage >= 60:
                return 'C'
            elif 60 > percentage >= 50:
                return 'D'
            elif 50 > percentage >= 40:
                return 'E'
            else:
                return 'F'

    def print_student(self):
        # Create a header table
        header_table = PrettyTable()
        header_table.field_names = ["Name", "Roll No", "Standard"]
        header_table.add_row([self.name, self.rollNo, self.standard])

        # Create a subject-wise details table
        subject_table = PrettyTable()
        subject_table.field_names = ["Subject", "Total Marks", "Passing Marks", "Obtained Marks", "Result"]
        for key, value in self.marks.items():
            subject_table.add_row([
                key, 100, 40, value["Marks"], value["Result"]
            ])

        # Add a line or divider
        subject_table.add_row(["-" * len(header) for header in subject_table.field_names])

        overall_result = 'Fail' if (
            any(result == 'Fail' for result in map(lambda x: x['Result'], self.marks.values()))) else 'Pass'
        total_marks = sum(item['Marks'] for item in self.marks.values())
        subject_table.add_row([
            'TOTAL', len(self.marks) * 100, len(self.marks) * 40, total_marks, overall_result
        ])

        # Create a bottom table for overall result and percentage
        bottom_table = PrettyTable()
        bottom_table.field_names = ["Result", "Percentage", "Grade"]

        overall_percentage = (total_marks / (len(self.marks) * 100 * 1.0)) * 100 if overall_result == 'Pass' else '--'

        overall_grade = self.calculate_grade(overall_percentage)

        bottom_table.add_row(
            [overall_result,
             f"{overall_percentage:.2f}%" if type(overall_percentage) is not str else overall_percentage,
             overall_grade])

        # Combine header table and subject table
        combined_table = f"""{header_table}\n\n{subject_table}\n\n{bottom_table}"""
        print(combined_table)


student = Student(name='rushabh', regNo='abc123', rollNo='123', standard='12', admissionYear='2024')
print(student.name)

marks = {
    'Maths': 90,
    'Science': 82,
    'English': 86,
    'Social Science': 20
}

student.update_marks(marks)
student.generate_result()
student.print_student()
