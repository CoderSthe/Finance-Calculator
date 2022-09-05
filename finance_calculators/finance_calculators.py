def calculate_investment():
    principle_amt = float(input("How much money will you be depositing: "))
    interest_rate = float(
        input("Please enter the interest rate (Only the number is necessary): ")
    )
    years = int(input("How many years will you be investing the amount: "))

    print("Please choose either 'simple' or 'compound' interest")
    print("simple           -   calculated on the principal amount invested annually")
    print("compound         -   calculated on the accumulated amount")
    interest = input("").lower()

    if (interest != "simple") and (interest != "compound"):
        print("You have entered an invalid option. Select 'simple' or 'compound'\n")
    else:
        if interest == "simple":
            print(
                "The total amount when simple interest is applied is R"
                f"{round(calculate_simple_interest(principle_amt, interest_rate, years), 2)}."
            )
        else:
            print(
                "The total amount when compound interest is applied is R"
                f"{round(calculate_compound_interest(principle_amt, interest_rate, years), 2)}."
            )


def calculate_bond():
    house_value = float(input("What is the present value of the house: "))
    interest_rate = (
        float(input("Please enter the interest rate (Only the number is necessary): "))
        / 100
    )
    months = int(input("How many months do you plan to take to repay the bond: "))

    total_amt = ((interest_rate / 12) * house_value) / (
        1 - (1 + (interest_rate / 12)) ** (-months)
    )
    print(f"The monthly bond repayment will be {round(total_amt, 2)}")


def calculate_simple_interest(principle, interest, num_years):
    total_amt = principle * (1 + (interest / 100) * num_years)
    return total_amt


def calculate_compound_interest(principle, interest, num_years):
    from math import pow

    total_amt = principle * pow(1 + (interest / 100), num_years)
    return total_amt
