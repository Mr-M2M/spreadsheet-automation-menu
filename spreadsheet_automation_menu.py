# Spreadsheet Automation Menu
# Author: Donavan McFadden
# This program shows a simple menu, gets the user's choice,
# confirms the choice, and prints the current date and time.

from datetime import datetime

# My student ID is stored as a string so any leading zeros are kept.
student_id = "donmcf8357"

# Title line (this is the first thing the program prints)
print(student_id + " Spreadsheet Automation Menu")

# Display the menu options
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into the variable called selected_option.
selected_option = input("Enter your selection (1, 2, or 3): ")

# Confirm the selection back to the user
print("Option " + selected_option + " has been selected")

# Show the current date and time
print("the time and date is", str(datetime.now()))
