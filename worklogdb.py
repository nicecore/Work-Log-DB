"""

Work Log With Database

A Treehouse Tech Degree Project

===============================

Allows a user to enter work logs into a database
and search existing logs by employee name,
task name, date, or keyword.

By Adam D Cameron
May-June 2017

"""

import peewee
import datetime
import sys
import os
import unittest
import doctest



db = peewee.SqliteDatabase('employees.db')

class Employee(peewee.Model):
    """Database model

    """
    name = peewee.CharField(max_length=255)
    task_name = peewee.CharField(max_length=255)
    date_time = peewee.DateTimeField(default=datetime.datetime.now)
    minutes = peewee.IntegerField(default=0)
    notes = peewee.TextField()

    class Meta:
        database = db

    def __str__(self):
        return """Employee Name: {}
Task: {}
Minutes Spent: {}
Notes: {}
        """.format(self.name.title(), self.task_name, self.minutes, self.notes)


###############################################################################

def c_s():
    """Clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


###############################################################################


def printer(results):
    """Print out search results"""

    if results:
        for i in results:
            c_s()
            timestamp = i.date_time.strftime('%A %B %d, %Y %I:%M %p')
            print(timestamp)
            print('='*len(timestamp))
            print(i)
            print("\nFor next entry, hit ENTER.")
            next_action = input("To return to main menu, press q and ENTER.\n> ")
            if next_action == 'q':
                main_menu()
    else:
        input("There were no results! Press ENTER to return to the main menu...")
    main_menu()


    # Receive search results from various search functions
    # Format strings and print out results in a nice way
    # Ask user if they want to do another search, reroute back to search or main menu
    pass


###############################################################################

def add_entry():
    """Add a new entry to the work log."""
    still_entering = True
    while still_entering:
        c_s()
        name = input("Please enter your name:\n> ").lower().strip()
        c_s()
        task_name = input("Enter the task name:\n> ")
        c_s()
        minutes = int(input("Enter the time to complete task, in minutes:\n> "))
        c_s()
        print("Please enter any notes for this task and press ctrl+d when finished.")
        note = sys.stdin.read().strip()
        if note:
            if input(
"""\n\nDo you want to save this entry? Please enter Y for YES and N for NO.
If you select NO you will be returned to the main menu. 
""").lower() != 'n':
                Employee.create(
                    name=name, 
                    task_name=task_name, 
                    minutes=minutes, 
                    notes=note)
                if input("Create another entry? [Yn] ").lower() != 'n':
                    add_entry()
                else:
                    main_menu()

            else:
                main_menu()


###############################################################################

def search_menu():
    """Allow users to select a type of search."""
    employees = Employee.select().order_by(Employee.date_time.desc())
    searching = True
    while searching:
        c_s()
        print("Please select from one of the following search options:")
        choice = input("""
[a] Find by employee name
[b] Find by date
[c] Find by time spent
[d] Find by search term
[e] Display all entries
> """).lower()
        if choice == 'a':
            name_search()
        elif choice == 'b':
            date_search()
        elif choice == 'c':
            time_search()
        elif choice == 'd':
            term_search()
        elif choice == 'e':
            printer(employees)

###############################################################################

def display_names():
    employees = Employee.select().order_by(Employee.date_time.desc())
    c_s()
    names = []
    for employee in employees:
        if employee.name not in names:
            names.append(employee.name)
    print("Here are the employees with existing records:\n")
    for name in names:
        print(name.title())

###############################################################################

def name_search():
    """Search for records by name."""
    employees = Employee.select().order_by(Employee.date_time.desc())
    c_s()
    print("Here are the employees with existing records:\n")
    display_names()
    search = input("\nPlease enter a name from the list above:\n> ").lower()
    printer(name_query(search))

###############################################################################

def name_query(search):
    employees = Employee.select().order_by(Employee.date_time.desc())
    return employees.where(Employee.name.contains(search))

###############################################################################

def display_dates():
    employees = Employee.select().order_by(Employee.date_time.desc())
    dates = []
    for i in employees:
        date = i.date_time.strftime("%m/%d/%Y")
        if date not in dates:
            dates.append(date)
    return dates


###############################################################################

def date_search():
    c_s()
    print("There are entries available for the following dates:")
    for i in display_dates():
        print(i)
    try:
        search = input("\nPlease enter a date in MM/DD/YYYY format:\n> ")
    except EOFError:
        search = None
    if search not in display_dates():
        c_s()
        input("There aren't any posts for that date!"
            "Press ENTER to return to the main menu...")
    date_search = datetime.datetime.strptime(search, "%m/%d/%Y").date()
    printer(date_query(date_search))


###############################################################################

def date_query(search):
    employees = Employee.select().order_by(Employee.date_time.desc())
    return employees.where(Employee.date_time.contains(search))
    


###############################################################################
def time_search():
    c_s()
    employees = Employee.select().order_by(Employee.date_time.desc())
    search = input("Please enter a number of minutes:\n> ")
    printer(time_query(search))


###############################################################################

def time_query(search):
    c_s()
    employees = Employee.select().order_by(Employee.date_time.desc())
    return employees.where(Employee.minutes == search)


###############################################################################

def term_search():
    c_s()
    search = input("Please enter any word or phrase to search:\n> ")
    printer(term_db_query(search))

###############################################################################

def term_db_query(search):
    employees = Employee.select().order_by(Employee.date_time.desc())
    return employees.where(
        (Employee.task_name.contains(search)) |
        (Employee.task_name.contains(search.lower()) |
        (Employee.notes.contains(search)) |
        (Employee.notes.contains(search.lower()))
    ))


###############################################################################


def main_menu():
    """Main program prompt"""
    choosing = True
    while choosing:
        c_s()
        choice = input("""Welcome, wage slave! Keep reaching for that rainbow!

This work log has been provided by your benevolent masters.

Please input one of the options below and hit ENTER.

[a] Create new work log entry
[b] Search older work log entries

[q] Exit the work log and get back to work

> """).lower()
        if choice == 'a':
            add_entry()
        elif choice == 'b':
            search_menu()
        elif choice == 'q':
            c_s()
            quit()

###############################################################################



if __name__ == '__main__':
    db.connect()
    db.create_tables([Employee], safe=True)
    main_menu()



###############################################################################
