'''@Author Rebecca Samuel
     ID No. : ATR/6554/11
     Section: 2 '''

#FCS Project I : Calculator

#First, we add a while loop to let the user use the calculator as long as they want to.
#We also have a variable(contin), and as long as the variable is equal to yes the calculator doesn't stop.

print()
print("Welcome!")

contin = "yes"
while contin.lower() == "yes":

    #The .lower() function helps the user enter in both uppercase and lowercase letters.
    
    #Then we give the user a menu of what type of calculations the calculator has.
    #We use \n to indicate each new line.

    print("Below are types of calculations available for this calculator:-\n"
    "\n"
    "Press 1 for basic arithmetic operations.\n" 
    "Press 2 for square root.\n"
    "Press 3 for trigonometric calculations.\n"
    "Press 4 for factorial.\n"
    "Press 5 for inverse trigonometric calculations.\n"
    "Press 6 for logaritmic calculations.\n"
    "Press 7 for hyperbolic trigonometric function.\n"
    "Press 8 for exponential function with base e.\n"
    "Press 9 to exit.\n")


    #We set a variable for the users choice of calculation.
    calculation_type = int(input("Choose one of the numbers shown above: "))
    print()

    #Importing the math module from the beginning helps so that we dont write it after each if statement.

    import math

    #Using if...elif...else statements we can write statements for each condition/choice of calculation.

    #1. Basic operations
       # The basic operation includes addition, multiplication, subtraction, power and more.

    if (calculation_type == 1):
        print("Choose one of the following basic operations: \n"
              "Press 1 for addition.\n"
              "Press 2 for subtraction.\n"
              "Press 3 for multiplication.\n"
              "Press 4 for division.\n"
              "Press 5 for power.\n"
              "Press 6 for the remainder of division.\n")
        
        operation = int(input("Enter one of the numbers shown above: "))
        print()

        num_1 = eval(input("Enter first number: "))
        num_2 = eval(input("Enter second number: "))
    
        #We can have nested if statements(If statements containing another if statements).

        if (operation == 1):
            print(num_1,"+",num_2,"=",num_1 + num_2)
        elif (operation == 2):
            print(num_1,"-",num_2,"=",num_1 - num_2)
        elif (operation == 3):
            print(num_1,"*",num_2,"=",num_1 * num_2)
        elif (operation == 4):
            if (num_2 != 0):
                print(num_1,"/",num_2,"=",num_1 / num_2)
            #If the user sets the denominator to zero,
            else:
                print("Cannot divide by zero.")
        elif (operation == 5):
            print(num_1,"^",num_2,"=",num_1 ** num_2)
        elif (operation == 6):
            if (num_2 != 0):
                print("Remainder of division when",num_1,"is divided by",num_2,"is",num_1 % num_2)
            else:
                print("Cannot divide by zero.")

        #If the user enters a number other than 1-6,
        else:
            print("Invalid input!")
                    
    #2. Square root function

     #The elif statement makes writing code easier.

    elif (calculation_type == 2):

        num = eval(input("Enter the number you want to find the square root of: "))
        if (num >= 0):
            ans = math.sqrt(num)
            print("The square root of",num,"equals",ans)
        else:
            print("The radicand cannot be negative.")

    #3. Trigonometric function

    elif (calculation_type == 3):

        #We give the user a format so that they don't get confused.
        print('''Please enter in this format,(Example): for the value of cos 60 degrees: Trig function: cos
                                                                      number in degrees: 60''')
        print()
        Trig = input("Enter the trig function you want to use, you can enter cos/sin/tan/csc/sec/cot: ")
        num = eval(input("Enter the number in degree measures: "))

        #Here using radians function we can get the trigonometric function of numbers in degree measures.

        if (Trig.lower() == "sin"):
            ans = math.sin(math.radians(num))
            print("sin",num,"=", ans)
        elif (Trig.lower() == "cos"):
            ans = math.cos(math.radians(num))
            print("cos",num,"=", ans)
        elif (Trig.lower() == "tan"):
            ans = math.tan(math.radians(num))
            print("tan",num,"=", ans)
        elif(Trig.lower() == "csc"):
            ans = 1/(math.sin(math.radians(num)))
            print("csc",num,"=", ans)
        elif(Trig.lower() == "sec"):
            ans = 1/(math.cos(math.radians(num)))
            print("sec",num,"=", ans)
        elif(Trig.lower() == "cot"):
            ans = 1/(math.tan(math.radians(num)))
            print("cot",num,"=", ans)  
        else:
            print("This Trig function is not available.")

    #4. Factorial

    elif (calculation_type == 4):
        num = eval(input("Enter a number you want to find the factorial of: "))
        ans = math.factorial(num)
        print("The Factorial of",num,"equals", ans)

    #5. Inverse Trigonometric function

    elif (calculation_type == 5):
    
        print('''Please enter in this format,(Example):for cos inverse of 0.5: Inverse trig function: cos-1
                                                                  number: 0.5''')
        print()

        Trig_inverse = input("Enter which trig inverse you want to use, you can enter cos-1/sin-1/tan-1: ")
        num = eval(input("Enter the number you want to find the trig inverse of: "))

        if (Trig_inverse.lower() == "cos-1"):
            #Restricting the domain for when the user enters a number outside of the domain.
            if -1 <= num <= 1: 
                ans = math.degrees(math.acos(num))
                print("cos inverse of",num,"equals",ans)
            else:
                print("Undefined. Outside the range of the number.")
                
        elif(Trig_inverse.lower() == "sin-1"):
            if -1 <= num <= 1:
                ans = math.degrees(math.asin(num))
                print("sin inverse of",num,"equals",ans)
            else:
                print("Undefined. Outside the range of the number.")

        elif(Trig_inverse.lower() == "tan-1"):
            ans = math.degrees(math.atan(num))
            print("tan inverse of",num,"equals",ans)

        else:
            print("This inverse Trig function isn't available.")

    #6. Logarithmic function

    elif (calculation_type == 6):

        print("Press 1 for logarithm with base e(natural logarithm).\n"
              "Press 2 for logarithm with any other base.\n")
        base = int(input("Enter your choice: "))

        if (base == 1):
            number = eval(input("Enter a number you want to find the natural logarithm of: "))
            if (number > 0):
                ans = math.log(number)
                print("Natural logarithm of", number, "is", ans)
            elif (number <= 0):
                print("Natural logarithm of a number less than or equal to zero is undefined.")
            else:
                print("Invalid input!")

        elif (base == 2):
            base_log = eval(input("Please enter a base to which the logarithm is computed: "))
            number = eval(input("Enter a number you want to find the logarithm of: "))
            if (number > 0): 
                ans = math.log(number, base_log)
                print("Logarithm base", base_log, "of", number, "is", ans)
            elif (number <= 0):
                print("Logarith of a number less than or equal to zero is undefined.")
            else:
                print("Invalid input!")

        else:
            print("Not available.")

    #7. Hyperbolic Trig function

    elif (calculation_type == 7):
        print('''Please enter in this format:(Example): for cosh 60, Enter hyperbolic trig: cosh 
                                                             Enter number: 60''')
        print()

        Hyperb_trig = input("Enter hyperbolic trig function you want to use, you can enter: cosh/sinh/tanh: ")
        number = eval(input("Enter a number you want to find the hyperbolic trig of: "))

        if (Hyperb_trig.lower() == "cosh"):
            ans = math.cosh(number)
            print("cosh",number,"=",ans)
        elif(Hyperb_trig.lower() == "sinh"):
             ans = math.sinh(number)
             print("sinh",number,"=",ans)
        elif(Hyperb_trig.lower() == "tanh"):
            ans = math.tanh(number)
            print("tanh",number,"=",ans)
        else:
            print("This hyperbolic trig function isn't available.")
             
        
    #8. Natural Exponential function

    elif (calculation_type == 8):
        number = input("Enter a number you would like to be the exponent of e: ")
        ans = math.exp(eval(number))
        print("e raised to", number, "equals", ans)
            
     
    #9. Exit (for the user to quit the program/calulator)
        #We use the function exit

    elif (calculation_type == 9):
        exit()


    #If user enters a number other than 1-9,

    else:
        print("Invalid input,please enter numbers 1-9.")

    #Defining the variable 'contin'
    print()
    contin = input("Would you like to continue? yes/no: ")
    print()

    # If user doesn't want to continue, we stop the loop/calculator from continuing, using the break function.

    if contin.lower() == "no":
        break

    

   
