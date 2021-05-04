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

if __name__ == '__main__':
    unittest.main()
