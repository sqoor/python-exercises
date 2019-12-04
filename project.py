from tkinter import *
from tkinter import messagebox
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


# ---------------------------------------------------------------------------

employees_list = []
students_list = []

# ---------------------------------------------------------------------------


root = Tk(className="My First GUI")
root.geometry('500x500+500+100')

top = Menu(root)
root.config(menu=top)


def open_about():
    messagebox.showinfo('About Us', 'Made by Asma Al-Fauri & Abdullah Al-Sqoor & Shaker Abady')


def open_reports():
    c = Toplevel(root)
    c.title("Reports")
    c.geometry("500x500+510+230")
    Label(c, text="Reports").grid()

    employees_number = len(employees_list)
    students_number = len(students_list)

    for employee in employees_list:
        employee.printInfo()
        print('Total Loans: ', employee.getTotalLoans())
        print('\n\n')

    highest_student_average = 0

    for student in students_list:
        if highest_student_average < student.getAverage():
            highest_student_average = student.getAverage()

    # employee_has_loans = list(filter(lambda e: e.getMinLoans(), employees_list))
    # min_employee_loan = min(list(map(lambda e: e.getMinLoans(), employee_has_loans)))

    # max_employee_loan = max(list(map(lambda e: e.getMaxLoans(), employee_has_loans)))
    #
    # employees_loans = list(map(lambda e: e.getLoans(), employee_has_loans))
    # employees_total_loans = list(map(lambda e: e.getTotalLoans(), employee_has_loans))

    data = f'''
            Total Employees Number: {employees_number}
            Total Students Number: {students_number}
            Highest Student Average: {highest_student_average}
        '''

    Label(c, text=data).grid()


def add_employee():
    c = Toplevel(root)
    c.title("Add New Employee")
    c.geometry("500x500+510+230")
    Label(c, text="Add New Employee").grid()

    employee_number = Label(c, text="Employee Number").place(x=20, y=20)
    name = Label(c, text="Name").place(x=20, y=40)
    address = Label(c, text="Address").place(x=20, y=60)
    salary = Label(c, text="Salary").place(x=20, y=80)
    job_title = Label(c, text="Job Title").place(x=20, y=100)
    loans = Label(c, text="Loans").place(x=20, y=120)

    employee_number_value = IntVar()
    name_value = StringVar()
    address_value = StringVar()
    salary_value = IntVar()
    job_title_value = StringVar()
    loans_value = IntVar()

    e1 = Entry(c, textvariable=employee_number_value).place(x=150, y=20)
    e2 = Entry(c, textvariable=name_value).place(x=150, y=40)
    e3 = Entry(c, textvariable=address_value).place(x=150, y=60)
    e4 = Entry(c, textvariable=salary_value).place(x=150, y=80)
    e5 = Entry(c, textvariable=job_title_value).place(x=150, y=100)
    e6 = Entry(c, textvariable=loans_value).place(x=150, y=120)

    loans = []

    def save_employee():
        employee = Employee(
            employee_number_value.get(),
            name_value.get(),
            address_value.get(),
            salary_value.get(),
            job_title_value.get(),
            loans
        )

        employee.printInfo()
        employees_list.append(employee)

    def add_loan():
        print('add loan', loans_value.get())
        loans.append(loans_value.get())
        print(loans)

    Button(c, text="Add Loan", command=add_loan).place(x=300, y=120)
    Button(c, text="Save", command=save_employee).place(x=30, y=150)


def view_employee():
    c = Toplevel(root)
    c.title("View Employee")
    c.geometry("500x500+510+230")
    Label(c, text="View Employee").grid()

    for employee in employees_list:
        data = f"Name: {employee.getName()} \t" \
               f"Address: {employee.getAddress()} \t" \
               f"Number: {employee.employee_number} \t" \
               f"Title: {employee.getJobTitle()} \t" \
               f"Salary: {employee.getSalary()} \t" \
               f"Loans: {employee.getLoans()} \t" \
               f""
        Label(c, text=data).grid()


def delete_employee():
    c = Toplevel(root)
    c.title("Delete Employee")
    c.geometry("500x500+510+230")
    Label(c, text="Delete Employee").grid()

    Label(c, text="Employee Number").place(x=20, y=20)
    employee_number_value = IntVar()

    def del_employee():
        global employees_list
        old_length = len(employees_list)
        employees_list = list(filter(lambda e: not e.employee_number == employee_number_value.get(), employees_list))
        new_length = len(employees_list)

        if not old_length == new_length:
            messagebox.showinfo('Success', f'Employee has been deleted, with number {employee_number_value.get()}')
        else:
            messagebox.showinfo('warning', 'There is not employee with the provided number')

    Entry(c, textvariable=employee_number_value).place(x=150, y=20)
    Button(c, text="Delete", command=del_employee).place(x=20, y=40)


def add_student():
    c = Toplevel(root)
    c.title("Add New Student")
    c.geometry("500x500+510+230")
    Label(c, text="Add New Student").grid()

    student_number = Label(c, text="Student Number").place(x=20, y=20)
    name = Label(c, text="Name").place(x=20, y=40)
    address = Label(c, text="Address").place(x=20, y=60)
    subject = Label(c, text="Subject").place(x=20, y=100)
    Label(c, text="Mark Title").place(x=20, y=120)
    Label(c, text="Mark value").place(x=20, y=140)

    student_number_value = IntVar()
    name_value = StringVar()
    address_value = StringVar()
    subject_value = StringVar()
    marks_title = StringVar()
    marks_value = IntVar()

    e1 = Entry(c, textvariable=student_number_value).place(x=150, y=20)
    e2 = Entry(c, textvariable=name_value).place(x=150, y=40)
    e3 = Entry(c, textvariable=address_value).place(x=150, y=60)
    e5 = Entry(c, textvariable=subject_value).place(x=150, y=100)
    e6 = Entry(c, textvariable=marks_title).place(x=150, y=120)
    e7 = Entry(c, textvariable=marks_value).place(x=150, y=140)

    marks = {}

    def save_student():
        # student_number, name, address, subject, marks
        student = Student(
            student_number_value.get(),
            name_value.get(),
            address_value.get(),
            subject_value.get(),
            marks
        )

        student.printInfo()
        students_list.append(student)

    def add_mark():
        print('add mark', marks_value.get())
        # marks.update(marks_title.get(), marks_value.get())
        marks[marks_title.get()] = marks_value.get()
        print(marks)

    Button(c, text="Add Mark", command=add_mark).place(x=300, y=140)
    Button(c, text="Save", command=save_student).place(x=30, y=180)


def view_student():
    c = Toplevel(root)
    c.title("View Student")
    c.geometry("500x500+510+230")
    Label(c, text="View Student").grid()

    for student in students_list:
        data = f"Name: {student.getName()} \t" \
               f"Address: {student.getAddress()} \t" \
               f"Number: {student.student_number} \t" \
               f"Title: {student.getSubject()} \t" \
               f"Marks: {student.getMarks()} \t" \
               f""
        Label(c, text=data).grid()


def delete_student():
    c = Toplevel(root)
    c.title("Delete Student")
    c.geometry("500x500+510+230")
    Label(c, text="Delete Student").grid()

    Label(c, text="Student Number").place(x=20, y=20)
    student_number_value = IntVar()

    def del_student():
        global students_list
        old_length = len(students_list)
        students_list = list(filter(lambda e: not e.student_number == student_number_value.get(), students_list))
        new_length = len(students_list)

        if not old_length == new_length:
            messagebox.showinfo('Success', f'Student with number "{student_number_value.get()}" has been deleted')
        else:
            messagebox.showinfo('Warning', 'There is not student with the provided number')

    Entry(c, textvariable=student_number_value).place(x=150, y=20)
    Button(c, text="Delete", command=del_student).place(x=20, y=40)


top = Menu(root)
root.config(menu=top)

file = Menu(top, tearoff=0)
file.add_command(label="Reports", command=open_reports)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)
top.add_cascade(label="File", menu=file)

employees = Menu(top, tearoff=0)
employees.add_command(label='Add', command=add_employee)
employees.add_command(label='View', command=view_employee)
employees.add_command(label="Delete", command=delete_employee)
top.add_cascade(label="Employees", menu=employees)

students = Menu(top, tearoff=0)
students.add_command(label="Add", command=add_student)
students.add_command(label="View", command=view_student)
students.add_command(label="Delete", command=delete_student)
top.add_cascade(label="Students", menu=students)

help_menu = Menu(top, tearoff=0)
help_menu.add_command(label='About', command=open_about)
top.add_cascade(label="Help", menu=help_menu)

root.mainloop()
