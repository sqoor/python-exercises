# Project 1
from functools import reduce


class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getAddress(self):
        return self._address

    def setAddress(self, address):
        self._address = address

    def __del__(self):
        print(f'Student {self._name} has been deleted')


class Employee(Person):
    def __init__(self, employee_number, name, address, salary, job_title, loans):
        super().__init__(name, address)
        self.employee_number = employee_number
        self.__salary = salary
        self.__job_title = job_title
        self.__loans = loans

    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary

    def getJobTitle(self):
        return self.__job_title

    def setJobTitle(self, job_title):
        self.__job_title = job_title

    def getTotalLoans(self):
        return sum(self.__loans)

    def getMaxLoans(self):
        if len(self.__loans) < 1:
            return None
        return max(self.__loans)

    def getMinLoans(self):
        if len(self.__loans) < 1:
            return None
        return min(self.__loans)

    def setLoans(self, loans):
        self.__loans = loans

    def getLoans(self):
        return self.__loans

    def printInfo(self):
        print(f'''
Name: {self._name}
Address: {self._address}
Employee Number: {self.employee_number}
Salary: {self.__salary}
Job Title: {self.__job_title}
Loans: {self.__loans}
        ''')

    def __del__(self):
        print(f'Employee: {self.employee_number} have been deleted')


class Student(Person):
    def __init__(self, student_number, name, address, subject, marks):
        super().__init__(name, address)
        self.student_number = student_number
        self.__subject = subject
        self.__marks = marks

    def getSubject(self):
        return self.__subject

    def setSubject(self, subject):
        self.__subject = subject

    def getMarks(self):
        return self.__marks

    def setMarks(self, marks):
        self.__marks = marks

    def getAverage(self):
        summation = 0
        length = 0

        for key, value in self.__marks.items():
            summation += value
            length += 1

        average = summation / length
        return average

    def getAllMarks(self):
        average = self.getAverage()

        if average >= 90:
            True
        else:
            return False
        # return list(filter(lambda x: x >= 90, self.__marks))

    def printInfo(self):
        print(f'''
Name: {self._name}
Address: {self._address}
Student nUmber: {self.student_number}
Subject: {self.__subject}
Marks: {self.__marks}
        ''')

    def __del__(self):
        print(f'Student: {self.student_number} I have been deleted')


employee1 = Employee(1000, 'Ahamad Yazan', 'Amman, Jordan', 500, 'HR Consultant', [434, 200, 1020])
employee2 = Employee(2000, 'Hala Rana', 'Aqaba, Jordan', 750, 'Department Manager', [150, 3000, 250])
employee3 = Employee(3000, 'Mariam Ali', 'Mafraq, Jordan', 600, 'HR S Consultant', [304, 1000, 250, 3000, 5000, 235])
employee4 = Employee(4000, 'Yasmeen Mohammad', 'Karak, Jordan', 865, 'Director', [])

student1 = Student(20191000, 'Khalid Ali', 'Irbid, Jordan', 'History', {
    'english': 80,
    'arabic': 90,
    'art': 95,
    'management': 75
})
student2 = Student(20182000, 'Reem Hani', 'Zarqa, Jordan', 'Software Eng', {
    'english': 80,
    'arabic': 90,
    'management': 75,
    'calculus': 85,
    'os': 73,
    'programming': 90
})
student3 = Student(20161001, 'Nawras Abdulllah', 'Amman, Jordan', 'Arts', {
    'english': 83,
    'arabic': 92,
    'art': 90,
    'management': 70
})
student4 = Student(20172030, 'Amal Raed', 'Tafelah, Jordan', 'Computer Eng', {
    'english': 83,
    'arabic': 92,
    'art': 90,
    'management': 70,
    'calculus': 80,
    'os': 79,
    'programming': 91
})

# 1
EmployeesList = [employee1, employee2, employee3, employee4]

# 2
StudentsList = [student1, student2, student3, student4]


# 3 & 4
def len_list(lst_name, lst):
    print(lst_name + ' has ' + str(len(lst)) + ' Persons')


len_list('EmployeesList', EmployeesList)
len_list('StudentsList', StudentsList)

# 5
for employee in EmployeesList:
    employee.printInfo()
    print('Total Loans: ', employee.getTotalLoans())
    print('\n\n')

# 6
for student in StudentsList:
    student.printInfo()
    print('Average: ' + str(student.getAverage()))

# 7
highest_student_average = 0

for student in StudentsList:
    if highest_student_average < student.getAverage():
        highest_student_average = student.getAverage()

print('Highest student average: ' + str(highest_student_average))

# 8
employee_has_loans = list(filter(lambda e: e.getMinLoans(), EmployeesList))
min_employee_loan = min(list(map(lambda e: e.getMinLoans(), employee_has_loans)))
print('Employees\' Min Loans is: ' + str(min_employee_loan))

# 9
max_employee_loan = max(list(map(lambda e: e.getMaxLoans(), employee_has_loans)))
print('Employees\' Max Loans is: ' + str(max_employee_loan))

# 10
employees_loans = list(map(lambda e: e.getLoans(), employee_has_loans))
employees_total_loans = list(map(lambda e: e.getTotalLoans(), employee_has_loans))
print(f'''
Employees Loans: {employees_loans}
Employees Total Loans: {employees_total_loans}
''')

# 11

LoanDictionary = list(map(lambda e: {e.employee_number: e.getLoans()}, employee_has_loans))
# print(LoanDictionary)
for item in LoanDictionary:
    print(item)


# 12
def get_max_loan(employee_loans):
    max_loan = reduce(lambda a, b: a if a > b else b, employee_loans)
    return max_loan


def get_min_loan(employee_loans):
    min_loan = reduce(lambda a, b: a if a < b else b, employee_loans)
    return min_loan


for employee in employee_has_loans:
    print(
        f'Employee Name: {employee._name} Min Loan: {get_min_loan(employee.getLoans())} Max Loan: {get_max_loan(employee.getLoans())}')

# 13
students_got_a = list(filter(lambda s: s.getAllMarks(), StudentsList))
for student in students_got_a:
    print(f'''
Name: {student.getName()}
Subject: {student.getSubject()}
Marks: {student.getMarks()}
''')

# 14
employee_salaries = list(map(lambda e: e.getSalary(), EmployeesList))
max_employee_salary = max(employee_salaries)
print('Maximum Employee Salary', max_employee_salary)

# 15
min_employee_salary = min(employee_salaries)
print('Minimum Employee Salary', min_employee_salary)
# 16

total_salaries = reduce(lambda a, b: a + b, employee_salaries)
print('Total Employees Salaries ', total_salaries)


# 17
def delete_object(lst_object):
    for item in lst_object:
        del item


delete_object(EmployeesList)
delete_object(StudentsList)

