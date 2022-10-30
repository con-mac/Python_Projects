# Program: Diet planner using a central Class
# Author: Conor Macklin (B00794811)
# Version: 1.0.1

# This program will demonstrate the basics of Object-Orientated
# programming (OOP) and the benefits of using a central class to store
# and display records. Information will be written and read from a
# text file and sorted using list functions.


# Import all the data from the class file
from Diet_Class import *
# Call main menu
def main():
    menu()


def menu():
    print("\n******** Diet Plan Menu ********")
    print("\nEnter 1 to display all meal records")
    print("Enter 2 to dispaly total number of calories ")
    print("Enter 3 to find the average serving weight of all meals ")
    print("Enter 4 for Total amount of foot eaten today ")
    print("Enter 5 to Search for records based on saturated fat threshold")
    print("Enter 6 to add a new record")
    print("Enter 7 to Exit program ")

    userChoice = (input("Enter Menu option: "))
# If/if-else/else decision structures are used in the menu selection
# process.

    if userChoice == '1':
        displayRecords()

    elif userChoice == '2':
        displayTotal()

    elif userChoice == '3':
        findAverage()

    elif userChoice == '4':
        totalAmount()

    elif userChoice == '5':
        satFat()

    elif userChoice == '6':
        addNew()

    elif userChoice == '7':
        end()
# Incorrect input is then validated by the else statement
    else:
        print("ERROR: YOU HAVE MADE AN INCORRECT CHOICE PLEASE TRY AGAIN!")
        menu()


# Call option one: Display all records
def displayRecords():
# Empty ist is created and txt file is opened and read line-by-line.
    list = []
    infile = open("Diet.txt")
    fileContents = infile.readlines()


# Each line is read in as an object, calling the 'diet' class.
    for row in fileContents:
        row = row.strip('\n').split(', ')
        list.append(diet(row[0],row[1],row[2],row[3],row[4],row[5]))
        infile.close()

# for-loop to pass each object to the printdetails method.
    for index in list:
        i = index.record()
        print(i)
        index.printDetails()
# Call the go-again function.
    goAgain()


# Option 2 (Function): Calorie intake
def totalCals():
    list = []
    totalList = 0
    infile = open("Diet.txt")
    fileContents = infile.readlines()

# List read in ,stripped and split in 2D format and appended to
# empty list .
    for row in fileContents:
        row = row.strip('\n').split(', ')
        list.append(row)

# For-loop is used using the 'len' function to add items in list
    for item in range(len(list)):
        # Each item in list is totaled
        totalList += float(list[item][4])
    total = format(totalList/len([list]), '.2f')
    infile.close()
    return total

# Print option 2...
def displayTotal():
    print("\nThe total amount of calories of "
          "all the foods is : ",totalCals(),"kcal")
    goAgain()


# Option 3: Serving total uses similiar function as option 2,
# sorting 2d list followed by mathematical operation...
def average():
    list = []
    totalList = 0
    infile = open("Diet.txt")
    fileContents = infile.readlines()

    for row in fileContents:
        row = row.strip('\n').split(', ')
        list.append(row)


    for item in range(len(list)):
        totalList += float(list[item][3])
    total = format(totalList/len([list]), '.2f')
    average = format(float(total)/int(len(list)), '.2f')
    infile.close()
    return average

def findAverage():

    print("\nThe average serving in grammes is: ", average(),"g")
    goAgain()


# Option 4: Total serving also reads and sorts data in list format
# followed by for-loop to perform mathematical operation.
def totalToday():
    list = []
    totalList = 0
    infile = open("Diet.txt")
    fileContents = infile.readlines()

    for row in fileContents:
        row = row.strip('\n').split(', ')
        list.append(row)


    for item in range(len(list)):
        totalList += float(list[item][3])
    total = format(totalList/len([list]), '.2f')
    infile.close()
    return total

def totalAmount():
    print("\nThe total amount of servings in grammes"
          " taken today is", totalToday(),"g")
    goAgain()

# Option 5: Saturated fat threshold. This option requires data to be
# read in as objects again and to display all records under the desired
# saturated fat threshold.
def satFat():
    list = []
    infile = open("Diet.txt")
    fileContents = infile.readlines()

    for row in fileContents:
        row = row.strip('\n').split(', ')
        list.append(diet(row[0],row[1],row[2],row[3],row[4],row[5]))


    choice = input("\nEnter the maximum amount of saturated fat "
                   "threshold to display all records below chosen limit:")
    # For-loop is used to iterate through the 'sats' property of the
    # 'diet' class.
    for index in range(len(list)):
        if float(choice) >= float(list[index].sats):
            found = True
            # If true; call each record with printdetails method.
            if found:
                print(diet.record())
                indexValue = index
                list[indexValue].printDetails()
                infile.close()
            # Validate with else statement for records not found.
            else:
                print("NO records were found!")
    goAgain()

# Option 6: Add new record
def addNew():

    # Text file is read in as a list with the append suffix so that
    # data can be written to end of list.
    list = []
    infile = open("Diet.txt","a")

# While loop is used to enter the data
    userChoice = 'y'

    while userChoice == 'y':
        time = input("\nEnter the meal time: ")
        meal_type = input("Enter the meal type: ")
        des_of_m = input("Enter the description of meal: ")
        serv = input("Enter the serving weight (in grammes): ")
        cal = input("Enter the calories: ")
        sats = input("Enter the Saturated fat content (in grammes): ")

# New record are read and written as objects.
        list.append(diet(time, meal_type, des_of_m, serv, cal, sats))
        infile.write('\n' + time)
        infile.write(', ' + meal_type)
        infile.write(', ' + des_of_m)
        infile.write(', ' + serv)
        infile.write(', ' + cal)
        infile.write(', ' + sats)


        userChoice = input("Do you want to add another "
                           "meal record? ('y' for yes):")
# New records are printed as objects
    for index in list:
        print("\n")
        index.printDetails()

    infile.close()
    goAgain()

def goAgain():
    # an if-statement is used to prompt the user to go
    # again. Any key other than small-case 'y' will end the option and
    # return to menu.
    userChoice = input("\nDo you want to do chose again?"
                           " ('y' for yes): ")

    if userChoice == 'y':
        menu()
    else:
        end()


# End program function
def end():
    print("\nThe program has ended\n")

main()























