import unittest
from fizz_buzz.fizz_buzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_fizz_for_number_3(self):
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.go(3), 'Fizz')

if __name__ == '__main__':
    unittest.main()
