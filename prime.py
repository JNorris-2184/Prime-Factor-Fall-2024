"""
prime.py -- Application to generate all prime factors for a given number
"""


def generate_prime_factors(number):
    """Return prime factors
    Args:
    number (int): any number greater than 0
    Returns:
    list: prime factors of number
    """
    if int(number):
        prime_list = []
        i = 2
        factored_number = number
        while i <= number - 1:
            if factored_number % i == 0:
                while factored_number % i == 0:
                    prime_list.append(i)
                    factored_number /= i
            i += 1
        if len(prime_list) == 0:
            if number != 1:
                prime_list = [number]
        return prime_list
    return int(number)
