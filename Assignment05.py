# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KLMartinez,11/19/21,Added code
# KLMartinez,11/21/21,Edited and completed code
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # Data storage file (note: changed variable name from objFile)
objFile = None  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")  # Open file in read mode
for row in objFile:
    lstRow = row.split(",")  # Row of data from the file, split on the comma
    dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}  # Populate a dictionary row using the list row contents
    lstTable.append(dicRow)  # Append row to the table in memory
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == "1"):
        print("Your current to-do list (task, priority):")
        for dicRow in lstTable:
            print(dicRow['task'], dicRow['priority'], sep=', ')
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == "2"):
        print("Enter the task and priority (Low, Medium, High):")
        task = input("To-do task: ")  # User enters a task
        priority = input("Priority (Low, Medium, High): ")  # User enters a priority
        dicRow = {"task": task, "priority": priority}  # Populate a dictionary row using the inputs
        lstTable.append(dicRow)  # Append row to the table in memory
        print("\nTask added.")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == "3"):
        print("Your current to-do list (task, priority):")
        for dicRow in lstTable:
            print(dicRow["task"], dicRow["priority"], sep=', ')
        delTask = input("Which task from the list above would you like to delete?: ")
        for dicRow in lstTable:  # Search table by row for the task to delete
            if delTask.lower() in dicRow["task"].lower():
                lstTable.remove(dicRow)  # Delete the indicated row
        print(delTask.title() + " has been removed from the list.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == "4"):
        objFile = open(strFile, "w")  # Open txt file in write mode (write over existing contents)
        for dicRow in lstTable:  # For each dictionary row, write the values (comma separated)
            objFile.write(dicRow["task"] + ',' + dicRow["priority"] + "\n")
        objFile.close()
        print("To-do list saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == "5"):
        print("Exiting program.")
        break  # and Exit the program
