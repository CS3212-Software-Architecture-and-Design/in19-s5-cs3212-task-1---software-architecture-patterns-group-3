import numbers


class Server:

    def add_two_numbers(self, num1, num2):
        if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):
            return num1 + num2
        else:
            raise Exception()

    def find_maximum_element(self, numbers: list):
        return max(numbers)
