import math


def select_calculator() -> str:
    """
    accepts input from user and returns the string.
    """
    return input("").lower()


def display_main_menu() -> None:
    """
    displays main menu option for user
    """
    print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
    print(
        "investment           - to calculate the amount of interest you'll earn on interest"
    )
    print(
        "bond                 - to calculate the amount you'll have to pay on a home loan"
    )


def display_interest_menu() -> None:
    """
    displays the menu option for the available interest choices
    """
    print("Please choose either 'simple' or 'compound' interest")
    print("simple           -   calculated on the principal amount invested annually")
    print("compound         -   calculated on the accumulated amount")


def calculate_investment(choice, principle_amt, interest_rate, years) -> str:
    """
    calculates the total investment amount based on selected interest choice
    """
    if choice == "simple":
        total_amt = principle_amt * round((1 + (interest_rate / 100) * years), 2)
        msg = f"The total amount when simple interest is applied is R{total_amt}"

    # if user selected 'compound' interest:
    if choice == "compound":
        total_amt = round(principle_amt * math.pow(1 + (interest_rate / 100), years), 2)
        msg = f"The total amount when compound interest is applied is R{total_amt}"

    return msg


def select_interest() -> str:
    """
    prompts for user input to select interest choice
    """
    return input("").lower()


def calculate_bond(house_value, interest_rate, months) -> str:
    """
    calculates total bond repayment amount
    """
    total_amt = round(
        ((interest_rate / 12) * house_value)
        / (1 - (1 + (interest_rate / 12)) ** (-months)),
        2,
    )
    return f"The monthly bond repayment will be R{total_amt}"


def get_investment_info() -> tuple:
    '''
    prompts user for input needed for total investment calculation
    '''
    principle_amt = float(input("How much money will you be depositing: "))
    interest_rate = float(
        input("Please enter the interest rate (Only the number is necessary):")
    )
    years = int(input("How many years will you be investing the amount: "))

    return principle_amt, interest_rate, years


def get_bond_info() -> tuple:
    """
    prompts user for input needed for bond repayment calculation
    """
    house_value = float(input("What is the present value of the house: "))
    interest_rate = (
        float(input("Please enter the interest rate (Only the number is necessary):"))
        / 100
    )
    months = int(input("How many months do you plan to take to repay the bond: "))

    return house_value, interest_rate, months


if __name__ == "__main__":
    display_main_menu()

    calculator = select_calculator()
    while "investment" != calculator != "bond":  # user has selected invalid option
        print("You have entered an invalid option.")
        display_main_menu()
        calculator = select_calculator()

    if calculator == "investment":
        display_interest_menu()
        interest_choice = select_interest()
        while (
            "simple" != interest_choice != "compound"
        ):  # user has selected invalid option
            print("You have entered an invalid option.")
            display_interest_menu()
            interest_choice = select_interest()
        principle, interest, years = get_investment_info()
        total = calculate_investment(interest_choice, principle, interest, years)

    if calculator == "bond":
        value, interest, months = get_bond_info()
        total = calculate_bond(value, interest, months)

    print(total)
