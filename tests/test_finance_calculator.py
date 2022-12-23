import unittest
from io import StringIO
import finance_calculators as calc


class TestFinancecalculator(unittest.TestCase):

    def test_calculate_investment(self):
        '''Test whether user input is valid.
        display proper message if input is invalid.
        '''
        choice = 'simple'
        principle = 10000
        interest = 5
        years = 5
        res = calc.calculate_investment(choice, principle, interest, years)

        self.assertEqual(res, 'The total amount when simple interest is applied is R12500.0')


if __name__ == '__main__':
    unittest.main()

        
        