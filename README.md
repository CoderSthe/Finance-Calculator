# Finance Calculators

This is a program that allows the user to access two different financial calculators:
1. an investment calculator
2. a home loan repayment calculator.

### INTEREST FORMULA
1. Simple Interest:
A = P(1 + r * t)

2. Compound Interest:
A = P * math.pow((1+r),t)
where:
- A = total amount
- P = Principle amount
- r = interest / 100
- t = number of years for investment

### BOND REPAYMENT FORMULA
X = (i * P)/(1 - (1 + i)**(-n))
where:
- X = Monthly repayment amount
- i = monthly interest rate / 12
- P = Present value of house
- n = number of months over which the bond will be repaid
