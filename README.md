# Capstone
Senior Capstone: Auto Python Grader

Steps:
  1. Take .py file (From local dir)
  2. Run doctest module (https://docs.python.org/3.5/library/doctest.html) to test if code works as expected
  3. Other criteria outlined by instructor:
    a. Evaluate variable names for length, complexity
    b. Rough check for any documentation
  4. Create grade and pass value (.xlsx file)

Needs third party module "openpyxl" for spreadsheet functionality

Known Bugs:
Only functions under perfect conditions (Could use input confirmation on directory input)
Cannot handle py files with a space in the name (Known issue with subprocess, can fix)
