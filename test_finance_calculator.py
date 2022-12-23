import unittest
from io import StringIO
import finance_calculators as calc


class TestFinancecalculator(unittest.TestCase):

    def test_calculate_investment_simple_interest(self):
        '''
        Test the calculate_investment function with simple interest
        '''
        choice = 'simple'
        principle, interest, years = 10000, 5, 5
        res = calc.calculate_investment(choice, principle, interest, years)
        self.assertEqual(res, 'The total amount when simple interest is applied is R12500.0')

    def test_calculate_investment_compound_interest(self):
        '''
        Test the calculate_investment function with compound interest.
        '''
        choice = 'compound'
        principle, interest, years = 75500, 7.5, 10
        res = calc.calculate_investment(choice, principle, interest, years)
        self.assertEqual(res, 'The total amount when compound interest is applied is R155607.88')

    def test_calculate_bond(self):
        value, interest, months = 1200000, 0.075, 120
        res = calc.calculate_bond(value, interest, months)
        self.assertEqual(res, 'The monthly bond repayment will be R14244.21')


if __name__ == '__main__':
    unittest.main()

        
        