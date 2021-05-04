import unittest
from fizz_buzz.fizz_buzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    def test_fizz_for_number_3(self):
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.go(3), 'Fizz')

    def test_buzz_for_number_5(self):
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.go(5), 'Buzz')

    def test_buzz_for_multiples_of_5(self):
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.go(10), 'Buzz')

    def test_number_is_returned_for_non_multiples_of_3_or_5(self):
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.go(2), 2)

    def test_fizz_buzz_is_returned_for_15(self):
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.go(15), 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()
