import math


def select_calculator() -> str:
    '''
    accepts input from user and returns the string.
    '''
    calc_choice = input("").lower()

    return calc_choice

def display_message() -> None:
    '''
    displays main menu option for user
    '''
    print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
    print("investment           - to calculate the amount of interest you'll earn on interest")
    print("bond                 - to calculate the amount you'll have to pay on a home loan")

def calculate_investment():
    principle_amt = float(input("How much money will you be depositing: "))
    interest_rate = float(input("Please enter the interest rate (Only the number is necessary):"))
    years = int(input("How many years will you be investing the amount: "))

    print("Please choose either 'simple' or 'compound' interest")
    print("simple           -   calculated on the principal amount invested annually")
    print("compound         -   calculated on the accumulated amount")
    interest = input("").lower()

    # if the user has selected anything other than 'simple' or 'compound':
    while (interest != "simple") and (interest != "compound"):
        print("You have entered an invalid option. Select 'simple' or 'compound'\n")
        print("simple           -   calculated on the principal amount invested annually")
        print("compound         -   calculated on the accumulated amount")
        interest = input("").lower()

    if interest == "simple:":
        total_amt = principle_amt * (1 + (interest_rate / 100) * years)

        print(f"The total amount when simple interest is applied is R{round(total_amt, 2)}")

    # if user selected 'compound' interest:
    else:
        total_amt = principle_amt * math.pow(1 + (interest_rate / 100), years)

        print(f"The total amount when compound interest is applied is R {round(total_amt, 2)}")

def calculate_bond():
    house_value = float(input("What is the present value of the house: "))
    interest_rate = float(input("Please enter the interest rate (Only the number is necessary):"))/100
    months = int(input("How many months do you plan to take to repay the bond: "))

    total_amt = ((interest_rate / 12) * house_value) / (1 - (1 + (interest_rate / 12)) **(-months))

    print(f"The monthly bond repayment will be {round(total_amt, 2)}")

def calculate_total_amt():
    pass


if __name__ == '__main__':
    display_message()
    calculator = select_calculator()
    while (calculator != "investment") and (calculator != "bond"):
        print("You have entered an invalid option.")
        display_message()
        calculator = select_calculator()
    
    if calculator == 'investment':
        calculate_investment()
    elif calculator == 'bond':
        calculate_bond()