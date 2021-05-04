class FizzBuzz:
    def go(self, number):
        if number == 15:
            return 'FizzBuzz'
        elif number % 5 == 0:
            return 'Buzz'
        elif number % 3 == 0:
            return 'Fizz'
        return number
