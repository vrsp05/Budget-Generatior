"""
File name: budget_creator
Author: Victor Santana
Last update: 25/12/2023

BUDGET CREATOR PROGRAM
"""

# PROGRAM INTRODUCTION #
print("""
Hi and welcome to the budget creator. Please follow the instructions below to properly create a budget.
      
Budget generator steps:
      
1- Add the income or money balance that is desired to create a budget on.
2- Enter the result into the budget creator section.
3- Confirm the parameters.
4- Follow the budget created.""")

# VARIABLES #
# This variable is the input for the menu
user_menu = ""
# This variable is for placing the value of income
saved_balance = 0
# This is the input for income variable
income = True
# This variable is the title of the text file
title = ""
# This variable is for the thithing option
thithable_answer = ""

# PROGRAM STARTS HERE #
# This prints the menu of the program
print("""
Here is the menu:

1- Create or Add to the initial and thithing balance
2- See the initial balance
3- Create a budget
4- Write budget on a file
5- Close program
""")

user_menu = input("Please enter the number of the action desired (1-5): ")

while user_menu != "5":

    if user_menu == "1":

        try:

            income = float(input("\nWhat is the balance you want to add? "))

            saved_balance += income

            balance = saved_balance

            print(f"The amount of ${income} has been added succesfully.")

            thithing_answer = input("\nDo you pay thithing (YES or NO)? ")

            thithing_answer = thithing_answer.lower()

            while thithing_answer != "yes" and thithing_answer != "no":

                print("\nERROR: Invalid input. Please answer with YES or NO.")
                
                thithing_answer = input("\nDo you pay thithing (YES or NO)? ")

            if thithing_answer == "yes":
                
                thithable_amount = float(input(f"\nWhat is the tithable amount from your initial balance of ${balance}? "))
                    
                if thithable_amount < balance:

                    thithing_amount = thithable_amount * 0.10

                    print(f"You will pay ${thithing_amount} of thithing.")
                
                elif thithable_amount > balance:

                    print("\nThe thithable amount cannot be larger than the initial amount.")
            
            elif thithing_answer == "no":

                thithable_amount = 0

                thithing_amount = 0

                print(f"\nUnderstood! You will not pay thithing from your initial balance of ${balance}.")

        except ValueError:

            print("\nERROR: Invalid input. Please answer with numbers.")


    elif user_menu == "2":

        try:

            if thithable_amount > 0:

                print(f"""\nYour current balance is: ${balance}
Your current thithable amout is: ${thithable_amount}""")
            
            elif thithable_amount == 0:
                
                print(f"\nYour current balance is: ${balance}")

        except NameError:

            print("\nERROR: No existing balance. Please add a balance first.")
    
    elif user_menu == "3":

        #try:
            
            if thithing_amount > 0:

                # Thithing
                after_thithing = balance - thithing_amount
                print(f"""\nYour initial balance of ${balance} - ${thithing_amount:.2f} of thithing = ${after_thithing}""")
                # Fasting
                after_fasting = after_thithing - 15
                print(f"""Your balance after thithing of ${after_thithing} - $15.00 of fasting = ${after_fasting}""")
                # Food
                after_food = after_fasting - 75
                print(f"""Your balance after fasting of ${after_fasting} - $75.00 for food = ${after_food}""")
                # Gas
                after_gas = after_food - 25
                print(f"""Your balance after food of ${after_food} - $25.00 for gas = ${after_gas}""")
                # Savings
                after_savings = after_gas - 100
                print(f"""Your balance after gas of ${after_gas} - $100.00 for savings = ${after_savings}""")
                # Weekly dinning
                after_dinning = after_savings - 15
                print(f"""Your balance after savings of ${after_savings} - $15.00 for weekly dinning = ${after_dinning}""")
                # Barbershop
                after_barbershop = after_dinning - 20
                print(f"""Your balance after dinning of ${after_dinning} - $20.00 for barbershop = ${after_barbershop}""")
                # Personal items
                after_pitems = after_barbershop - 50
                print(f"""Your balance after barbershop of ${after_barbershop} - $50.00 for personal items = ${after_pitems}""")
                # Estimated remainder
                remaining_balance = after_pitems
                print(f"\nYou may have the estimated remaining balance of ${remaining_balance} by the end of the two weeks.")

            elif thithing_amount == 0:

                # Fasting
                after_fasting = balance - 15
                print(f"""\nYour initial balance of ${balance} - $15.00 of fasting = ${after_fasting}""")
                # Food
                after_food = after_fasting - 75
                print(f"""Your balance after fasting of ${after_fasting} - $75.00 for food = ${after_food}""")
                # Gas
                after_gas = after_food - 25
                print(f"""Your balance after food of ${after_food} - $25.00 for gas = ${after_gas}""")
                # Savings
                after_savings = after_gas - 100
                print(f"""Your balance after gas of ${after_gas} - $100.00 for savings = ${after_savings}""")
                # Weekly dinning
                after_dinning = after_savings - 15
                print(f"""Your balance after savings of ${after_savings} - $15.00 for weekly dinning = ${after_dinning}""")
                # Barbershop
                after_barbershop = after_dinning - 20
                print(f"""Your balance after dinning of ${after_dinning} - $20.00 for barbershop = ${after_barbershop}""")
                # Personal items
                after_pitems = after_barbershop - 50
                print(f"""Your balance after barbershop of ${after_barbershop} - $50.00 for personal items = ${after_pitems}""")
                # Estimated remainder
                remaining_balance = after_pitems
                print(f"\nYou may have the estimated remaining balance of ${remaining_balance} by the end of the two weeks.")

        #except NameError:

           # print("\nERROR: No existing balance. Please add a balance first.")
    
    elif user_menu == "4":

        try:
        
            with open("Bi-weekly Budget.txt", "w") as file:

                title = f"""Bi-weekly Budget:

Your initial balance of ${balance} - ${thithing_amount} of thithing = ${after_thithing}
Your balance after thithing of ${after_thithing} - $15.00 of fasting = ${after_fasting}
Your balance after fasting of ${after_fasting} - $75.00 for food = ${after_food}
Your balance after food of ${after_food} - $25.00 for gas = ${after_gas}
Your balance after gas of ${after_gas} - $100.00 for savings = ${after_savings}
Your balance after savings of ${after_savings} - $15.00 for weekly dinning = ${after_dinning}
Your balance after dinning of ${after_dinning} - $20.00 for barbershop = ${after_barbershop}
Your balance after barbershop of ${after_barbershop} - $50.00 for personal items = ${after_pitems}

You may have the estimated remaining balance of ${remaining_balance} by the end of the two weeks.

Thank you for using the budget creator!
"""
                file.write(title)

        except NameError:

            print("\nERROR: No existing balance. Please add a balance first.")

            with open("Bi-weekly Budget.txt", "w") as file:

                title_error = "\nERROR WHILE WRITTING FILE: No existing balance. Please add a balance first.\n"

                file.write(title_error)

        else:

            print("\nThe file has been created successfully.")

    else:

        print("\nERROR: Invalid input. Please try again.")
    
    user_menu = input("\nPlease enter the number of the new action desired (1-5): ")

print("\nYou have exit the programm successfully, have a nice day!\n")

"""
END OF PROGRAM
"""