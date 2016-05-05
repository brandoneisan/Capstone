import os, datetime, subprocess
from openpyxl import Workbook

def varCheck(var):
	"""Test name length, complexity
	If length is greater/equal 9, check for _ or mixedCase
	If length is not at least 3, fail var (3 is the shortest var name that can still be descriptive ex:var, pass, check)
	Will return varPass; true or false
	One bad var will ruin grade"""
	varPass = True
	if len(var) < 3: #minimum required length
		varPass = False
	if len(var) >= 9: #Length where complexity should be required (Multiple words)
		if "_" in var: #Checks for underscores in variable name
			varPass = True
		elif not var.islower() and not var.isupper(): #Checks the variable name so that it is not fully lowercase or UPPERCASE, looking for mixedCase
			varPass = True
		else: #If it is long enough for complexity but has none, it fails
			varPass = False
	return varPass
	
workingPath = str(input("Enter the directory where the .py files are located. Use two slashes for separating(EX C:\\\\Users\\\\test): "))
os.chdir(workingPath) #Sets working directory
print ("Current working directory: " + os.getcwd())
workingDir = os.listdir(os.getcwd()) #List of files in working directory
excelFile = Workbook() #Creates grades spreadsheet
workSheet = excelFile.active
count = 1
todaysDate = str(datetime.date.today())
workSheet['A' + str(count)] = "Name"
workSheet['B' + str(count)] = "Grade"
for file in workingDir:
	grade = 0 #Initializing needed variables
	fileWorks = True
	output = None
	if file.endswith(".py"): #Only Python files
		count += 1
		fileObject = open(file)		
		page = fileObject.readlines() #List with each element being a line of text
		try:
			output = subprocess.check_output("python " + workingPath + "\\" + str(file)) #Runs file, catches output
		except subprocess.CalledProcessError: #Error is called when file has a syntax error through subprocess
			fileWorks = False
		if str(output) == "b\'\'" and fileWorks == True: #b'' is the default output if it works correctly, or doesnt compile due to spelling error, so it checks fileWorks
			fileWorks = True
			grade += 1
		else:
			fileWorks = False #file checking done, now to variables
		varTest = True #Checks current variable
		aVarFailed = False #Remembers if any variable fails
		for line in page:
			if ' = ' in line: #If a variable is initialized
				listOfLine = line.split(' = ', maxsplit=1) #Splits the line into two objects: variable name and definition
				var = listOfLine[0] #Sets var to the variable name
				var = var.strip() #Removes any whitespace from string(due to indents)
				varTest = varCheck(var)
				if varTest == False:
					aVarFailed = True #Marks a failing variable, so no point
		if aVarFailed == False:
			if fileWorks == True:
				grade += 1 #Only gives point if file also works
		workSheet['A' + str(count)] = file
		workSheet['B' + str(count)] = grade
excelFile.save("grades " + todaysDate + ".xlsx")
input("Process Complete. Press Enter to end")	
