#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 19:15:03 2019

@author: abdala

Title:
Project 3 Database

Description:
desktop interface to add employees information to the database (sqlite)
and view them on desktop window,
"""

import sqlite3
from tkinter import *
from tkinter import scrolledtext


# DATABASE
class Employee:
    def __init__(self):
        # CREATE DATABASE FILE AND CONNECT TO IT
        self.__conn = sqlite3.connect('OrgDB.db')
        self.__c = self.__conn.cursor()

        # CREATE EMPLOYEES TABLE
        query = """CREATE TABLE IF NOT EXISTS employees (
                        number int, name text, gender text,
                        nationality text, dob text, address text,
                        department text, salary real )
        """
        self.__c.execute(query)
        self.__conn.commit()

    def add_record(self, employee: {}):
        query = f""" INSERT INTO employees VALUES (
             {employee["number"]},
             '{employee["name"]}',
             '{employee["gender"]}',
             '{employee["nationality"]}',
             '{employee["dob"]}',
             '{employee["address"]}',
             '{employee["department"]}',
             {employee["salary"]}
        )"""
        self.__c.execute(query)
        self.__conn.commit()

    def get_record(self, columns='*', condition=""):
        query = f"SELECT {columns} from employees {condition}"
        records = self.__c.execute(query)
        return list(records)

    def delete_reocrd(self, employee_number):
        query = f"DELETE FROM employees WHERE number={employee_number}"
        self.__c.execute(query)
        self.__conn.commit()

    def update_record(self, new_values, employee_number):
        # TODO: NOT WORKING, FIX IT
        query = f"UPDATE employees SET {new_values} WHERE number={employee_number}"
        self.__c.execute(query)
        self.__conn.commit()

    def __del__(self):
        self.__conn.close()


# TODO: TEST - DELETE IT LATER
# employees = Employee()

# employees.add_record({
#     "number": 2,
#     "name": "Abdullah",
#     "gender": "male",
#     "nationality": "Jordanian",
#     "dob": "03-06-1993",
#     "address": "Amman, Jordan",
#     "department": "IT",
#     "salary": 9999500
# })

# employees.delete_reocrd(1)

# employees.update_record({"name": 'Abd', }) # TODO: NOT WORKING YET

# employees_list = list(employees.get_record())
# print(employees_list)


# DESKTOP WINDOWS
class Windows:
    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title('Main window')
        self.__main_window.geometry('200x200')

        Button(self.__main_window, text="Add New Employee", command=self.open_add_window).grid()
        Button(self.__main_window, text="View Employees", command=self.open_view_employees).grid()
        Button(self.__main_window, text="Delete Employee", command=self.open_delete_employee).grid()
        Button(self.__main_window, text="Update Employee", command=self.open_update_employee).grid()

        self.__main_window.mainloop()

    def open_add_window(self):
        add_window = Toplevel(self.__main_window)
        add_window.title('Add New Employee')
        add_window.geometry('700x500+500+100')
        Label(add_window, text="Add New Employee").grid()

        number = Label(add_window, text="Number").place(x=30, y=40)
        name = Label(add_window, text="Name").place(x=30, y=60)
        gender = Label(add_window, text="Gender").place(x=30, y=80)
        nationality = Label(add_window, text="Nationality").place(x=30, y=100)
        dob = Label(add_window, text="DOB").place(x=30, y=120)
        address = Label(add_window, text="Address").place(x=30, y=140)
        department = Label(add_window, text="Department").place(x=30, y=160)
        salary = Label(add_window, text="Salary").place(x=30, y=180)

        number_value = IntVar()
        name_value = StringVar()
        gender_value = StringVar()
        nationality_value = StringVar()
        dob_value = StringVar()
        address_value = StringVar()
        department_value = StringVar()
        salary_value = StringVar()

        Entry(add_window, textvariable=number_value).place(x=100, y=40)
        Entry(add_window, textvariable=name_value).place(x=100, y=60)
        Entry(add_window, textvariable=gender_value).place(x=100, y=80)
        Entry(add_window, textvariable=nationality_value).place(x=100, y=100)
        Entry(add_window, textvariable=dob_value).place(x=100, y=120)
        Entry(add_window, textvariable=address_value).place(x=100, y=140)
        Entry(add_window, textvariable=department_value).place(x=100, y=160)
        Entry(add_window, textvariable=salary_value).place(x=100, y=180)

        def save_employee():
            employees = Employee()
            employees.add_record({
                "number": number_value.get(),
                "name": name_value.get(),
                "gender": gender_value.get(),
                "nationality": nationality_value.get(),
                "dob": dob_value.get(),
                "address": address_value.get(),
                "department": department_value.get(),
                "salary": salary_value.get()
            })

        Button(add_window, text="Save Record", command=save_employee).place(x=30, y=200)

    def open_view_employees(self):
        view_employee_window = Toplevel(self.__main_window)
        view_employee_window.title('View Employees')
        view_employee_window.geometry('700x500+510+110')
        Label(view_employee_window, text="View Employee").grid()

        employees = Employee()
        records = employees.get_record()

        data = 'Number \t\t Name \t\t Gender \t\t Nationality \t\t DOB \t\t Address \t\t Department \t\t Salary \n'
        Label(view_employee_window, text=data).grid()

        for employee in records:
            record = f"{employee[0]} \t\t {employee[1]} \t\t {employee[2]} \t\t {employee[3]} \t\t " \
                     f"{employee[4]} \t\t {employee[5]} \t\t {employee[6]} \t\t {employee[7]} \n"
            Label(view_employee_window, text=record).grid()

        # txt = scrolledtext.ScrolledText(view_employee_window, text=data, width=40, height=10)
        # txt.grid(column=0, row=0)

    def open_delete_employee(self):
        delete_window = Toplevel(self.__main_window)
        delete_window.title('Delete Employee')
        delete_window.geometry('700x500+520+120')
        Label(delete_window, text="Delete Employee").grid()

        Label(delete_window, text="Employee Number").place(x=20, y=20)
        employee_number_value = IntVar()

        def del_employee():
            employees = Employee()
            employees.delete_reocrd(employee_number_value.get())

        Entry(delete_window, textvariable=employee_number_value).place(x=150, y=20)
        Button(delete_window, text="Delete", command=del_employee).place(x=20, y=40)

    def open_update_employee(self):
        update_window = Toplevel(self.__main_window)
        update_window.title('Update Employee')
        update_window.geometry('700x500+530+130')
        Label(update_window, text="Update Employee").grid()


windows = Windows()
