# Capstone
Senior Capstone: Auto Python Grader

Steps:
  1. Take .py file (From local dir)
  2. Run doctest module (https://docs.python.org/3.5/library/doctest.html) to test if code works as expected
  3. Other criteria outlined by instructor:
    a. Evaluate variable names for length, complexity
  4. Create grade and pass value (.xlsx file)

Needs third party module "openpyxl" for spreadsheet functionality

Known Bugs:
Crashes when directory entered is not valid (Could use input confirmation on directory input)
Cannot handle py files with a space in the name (Known issue with subprocess, should be able to fix by replacing spaces in the string with '\s' before passing to subprocess)
Fails if existing grade sheet with same name is open/cannot be replaced (Could fix by adding time to xlsx name)
