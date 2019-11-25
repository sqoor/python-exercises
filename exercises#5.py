class Employee:
    def __init__(
            self,
            employee_number,
            name,
            address,
            salary,
            job_title
    ):
        self.employee_number = employee_number
        self.__name = name
        self.__address = address
        self.__salary = salary
        self.__job_title = job_title

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def getSalary(self):
        self.__salary

    def getJobTitle(self):
        return self.__job_title

    def print_info(self):
        print(f'''
Employee number {self.employee_number}
Name: {self.__name}
Address: {self.__address}
Salary: {self.__salary}
Job Title: {self.__job_title}
        ''')

    def print_info_2(self):
        print(
            f'Employee number={self.employee_number} Name={self.__name} Address={self.__address} Salary={self.__salary} Job Title:={self.__job_title} ')

    def __del__(self):
        print(self.__name + ' has been deleted')


employee1 = Employee(
    1,
    'Mohammad Khalid',
    'Amman, Jordan',
    500,
    'Consultant'
)

employee1.print_info()
employee1.print_info_2()

employee2 = Employee(
    2,
    'Hala Rana',
    'Aqaba, Jordan',
    750,
    'Manager'
)


employee1.setAddress('USA')
print('Employee1 New Address : ' + employee1.getAddress())

del employee1
del employee2

