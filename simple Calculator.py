value1 = 0  #Gives a value to value1
value2 = 0  #Gives a value to value2

def ask_for_values():   #Defines the function (ask_for_values)
    global value1   #Makes value1 global
    global value2   #Mkaes value2 global
    value1 = input("Enter first value")     #Asks for the user to enter the first value
    value2 = input("Enter Second value")    #Asks for the user to enter the second value

    if not value1.isnumeric():  #Checks if the first value is not numeric
        print("The first value is not an integer or float, Please enter again.")    #If so it will output:
        ask_for_values()    #Returns the argument for the function
    elif not value2.isnumeric():    #Checks if the second value is not numeric
        print("The second value is not an integer or float, Please enter again.")   #if so it will output:
        ask_for_values()    #Returns the argument for the function
    else:
        value1 = float(value1)  #ASssigns the first value into a float instead of a string
        value2 = float(value2)  #ASssigns the second value into a float instead of a string

ask_for_values() #Returns the argument for the function

decision = input("Enter between add, subtract, divide, multiply")   #Asks the user for what calculation it wants to complete

def addition(value1, value2):   #Defines the function (adition) with both values as its parameters
    result = value1 + value2    #Since its addition, this line adds both values together
    print(result)   #prints the result

def subtraction(value1, value2):    #Defines the function (subtraction) with both values as its parameters
    result = value1 - value2    #Subtracts the first value with the second
    print(result)   #prints result

def division(value1, value2):   #Defines the function (division) with both values as its parameters
    result = value1 / value2    #Divides the first value with the second
    print(result)   #prints result

def multiplication(value1, value2): #Defines the function (multiplication) with both values as its parameters
    result = value1 * value2    #Multiplies both values together
    print(result)   #print result

if decision == "add":   #If the user enters add it will:
    addition(value1,value2) #runs the function addition, this is the argument


elif decision == "subtract":    #If the user enters subtract it will:
    subtraction(value1,value2)  #runs the function addition, this is the argument

elif decision == "divide":  #If the user enters divide it will:
    if value2 == 0:
        print("Sorry your second value CANNOT be 0")
        ask_for_values()
    else:
        division(value1,value2) #runs the function addition, this is the argument

elif decision == "multiply":    #If the user enters multiply it will:
    multiplication(value1,value2)   #runs the function addition, this is the argument

else:
    print("Wrong Input")    #If the user doesnt enter any of the provided, it will print...
