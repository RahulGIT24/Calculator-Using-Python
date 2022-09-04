
#! Made by Rahul
#! Location Mars
#! Date-2-12-2021
#! Project Name Calculator

try:
    while (True):
        
        print('''
            1.Simple calculator
            2.Scientific calculator
            3.Exit calculator''')
        choice=int(input("Enter your choice: "))
        if (choice==1):
            num1=int(input("Enter first number\n"))
            num2=input("Enter the mathematical operation\n")
            num3=int(input("Enter second number\n"))

            if __name__=="__main__":
                def calcu(num1,num2,num3):
                    if '*' in num2:
                        return (f'The multiply of two numbers is {num1*num3}')
                    elif '+' in num2:
                        return (f'The addition of two numbers is {num1+num3}')
                    elif '-' in num2:
                        return (f'The subtraction of two numbers is {num1-num3}')
                    elif '/' in num2:
                        return (f'The divide of two numbers is {num1/num3}')
                    else:
                        print("Invalid command")
                print(calcu(num1,num2,num3))

                f=open("calculator_history.txt",'r')
                f.read()
                with open("calculator_history.txt","a") as f:
                    f.writelines(f"\n{num1} {num2} {num3}")
                f=open("calculator_history.txt",'r')
                f.read()
                f.close()

        elif (choice==2):
            import math
            print("*** Scientific Calculator enabled succesfully ******")
            description=('''Note* This scientific calculator takes only one number and may not be valid for all commands.''')
            print(description)
            s=int(input("Enter the number\n"))
            c=input("Enter the operation: ")
            def scientificCalcu(s):
                if ('sin' == c):
                    return(f"The sin of {s} is {math.sin(s)}")
                elif ('tan' == c):
                    return(f"The tan of {s} is {math.tan(s)}")
                elif ('square' == c):
                    return(f"The square of {s} is {s*s}")
                elif ('cube' == c):
                    return(f"The cube of {s} is {s*s*s}")
                elif ('square root' == c):
                    return(f"The square root of {s} is {math.sqrt(s)}")
                elif ('gamma' == c):
                    return(f"The gamma of {s} is {math.gamma(s)}")
                elif ('hyperbolic tangent' == c):
                    return(f"The hyperbolic tangent of {s} is {math.tanh(s)}")
                elif ('pi' == c):
                    return(f"The the ratio of circumference of a circle to it's diameter {s} is {math.pi(s)}")
                elif ('cos' == c):
                    return(f"The cosine of {s} is {math.cos(s)}")
                elif ('ceil' == c):
                    return(f"The ceil of {s} is {math.ceil(s)}")
                # elif ('degrees' or 'degree' == c):
                #     return(f"The degrees of {s} is {math.degrees(s)}")
                else:
                    return("Operation not available")
            print(scientificCalcu(s))

            f=open("calculator_history.txt",'r')
            f.read()
            with open("calculator_history.txt","a") as f:
                f.writelines(f"\n{c} of {s}")
            f=open("calculator_history.txt",'r')
            f.read()
            f.close()

        elif (choice==3):
            print("**** Thanks for using this calculator ****")
            exit()
        else:
            print("Enter a valid choice!")
except Exception:
    print("Please enter a valid value or operarion!")
