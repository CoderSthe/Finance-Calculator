import math

print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment           - to calculate the amount of interest you'll earn on interest")
print("bond                 - to calculate the amount you'll have to pay on a home loan")

calc_choice = input("").lower()

if (calc_choice != "investment") and (calc_choice != "bond"):
    print("You have entered an invalid option. Please choose either 'investment' or 'bond'\n")

else:

    if calc_choice == "investment":
        principle_amt = float(input("How much money will you be depositing: "))
        interest_rate = float(input("Please enter the interest rate (Only the number is necessary): "))
        years = int(input("How many years will you be investing the amount: "))


        print("Please choose either 'simple' or 'compound' interest")
        print("simple           -   calculated on the principal amount invested annually")
        print("compound         -   calculated on the accumulated amount")
        interest = input("").lower()

        if (interest != "simple") and (interest != "compound"):
            print("You have entered an invalid option. Select 'simple' or 'compound'\n")

        else:
            if interest == "simple:":
                total_amt = principle_amt * (1 + (interest_rate / 100) * years)

                print(f"The total amount when simple interest is applied is R{round(total_amt, 2)}\n")

            else:
                total_amt = principle_amt * math.pow(1 + (interest_rate / 100), years)

                print(f"The total amount when compound interest is applied is R {round(total_amt, 2)}\n")
    
    else:
        house_value = float(input("What is the present value of the house: "))
        interest_rate = float(input("Please enter the interest rate (Only the number is necessary): "))/100
        months = int(input("How many months do you plan to take to repay the bond: "))

        total_amt = ((interest_rate / 12) * house_value) / (1 - (1 + (interest_rate / 12)) ** (-months))

        print(f"The monthly bond repayment will be {round(total_amt, 2)}")
