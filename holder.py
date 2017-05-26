def user_select():
    """Allow user to select their name."""
    users = Employee.select().order_by(Employee.name.desc())



def determine_user():
    """Determine whether active user is existing or new."""
    c_s()
    print(
"""Welcome, wage slave! Keep reaching for that rainbow!\n
            
This work log has been provided by your benevolent masters.\n
            
Please confirm your identity or select New User to open your account.

""")
    if input("Please enter N for new user and ENTER for existing user:\n> ").lower() == 'n':
        c_s()
        global active_user
        active_user = input("Please enter your name:\n> ")
        main_menu()
    else:
        print("Please enter the NUMBER corresponding with your name and hit ENTER")
        employees = Employee.select().order_by(Employee.name.desc())

        # The above var contains an iterable of ALL records - they are just SORTED by name. They don't actually contain just the name.
        # Below the records are looped through as an enumerate() object, with the start being 1 instead of 0.
        # This necessitates subtracting one from whatever choice the user enters to retrieve the proper name by index.
        holder = []
        for employee in enumerate(employees, start=1):
            # The index+1 is printed out, followed by the .name attribute of index 1 of each tuple, which is still the whole record itself.
            holder.append(employee)
            print("[{}] {}".format(employee[0], employee[1].name))
        choice = int(input("\n> "))
        global active_user
        active_user = holder[choice-1][1]
        main_menu()