from finance_calculators.finance_calculators import (
    calculate_investment,
    calculate_bond,
    calculate_compound_interest,
    calculate_simple_interest,
)

print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print(
    "investment           - to calculate the amount of interest you'll earn on interest"
)
print(
    "bond                 - to calculate the amount you'll have to pay on a home loan"
)
calc_choice = input("").lower()
if (calc_choice != "investment") and (calc_choice != "bond"):
    print(
        "You have entered an invalid option. Please choose either 'investment' or 'bond'\n"
    )
else:
    if calc_choice == "investment":
        calculate_investment()
    else:
        calculate_bond()
