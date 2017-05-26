from peewee import *
import datetime
import sys
import os



db = SqliteDatabase('employees.db')

class Employee(Model):
    name = CharField(max_length=255)
    task_name = CharField(max_length=255)
    date_time = DateTimeField(default=datetime.datetime.now)
    minutes = IntegerField(default=0)
    notes = TextField()

    class Meta:
        database = db


# All records in descending order by date

employees = Employee.select().order_by(Employee.date_time.desc())


def c_s():
    """Clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


###############################################################################


def printer(results):
    """Print out search results."""
    for i in results:
        c_s()
        timestamp = i.date_time.strftime('%A %B %d, %Y %I:%M %p')
        print(timestamp)
        print('='*len(timestamp))
        print("Employee name: {}".format(i.name.title()))
        print("Task: {}".format(i.task_name))
        print("Time spent:{}".format(i.minutes))
        print("Notes: {}".format(i.notes))

        print("\nFor next entry, hit ENTER.")
        next_action = input("To return to main menu, press q and ENTER.\n> ")
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
        name = input("Please enter your name:\n> ").lower()
        c_s()
        task_name = input("Enter the task name:\n> ")
        c_s()
        minutes = input("Enter the time to complete task, in minutes:\n> ")
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
    searching = True
    while searching:
        c_s()
        print("Please select from one of the following search options:")
        choice = input("""
[a] Find by employee name
[b] Find by date
[c] Find by time spent
[d] Find by search term
> """).lower()
        if choice == 'a':
            name_search()
        elif choice == 'b':
            date_search()
        elif choice == 'c':
            time_search()
        elif choice == 'd':
            term_search()

###############################################################################

def name_search():
    """Search for records by name."""
    c_s()
    # Fetch all records and sort by date in descending order
    search = input("Please enter a search term:\n> ").lower()
    name_results = employees.where(Employee.name.contains(search))
    printer(name_results)

    # Get all the records
    # Filter for records with the matching names
    # Pass the matching records to printer()



###############################################################################
def date_search():
    c_s()
    search = input("Please enter a date")

###############################################################################
def time_search():
    pass


###############################################################################

def term_search():
    pass

###############################################################################


def main_menu():
    """Main program prompt"""
    choosing = True
    while choosing:
        c_s()
        choice = input("""
Welcome, wage slave! Keep reaching for that rainbow!

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



# entries = Employee.select()
# results = []
# for i in entries:
#     append 



###############################################################################
