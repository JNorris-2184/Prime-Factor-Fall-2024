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
        while number % 2 == 0:
            prime_list.append(2)
            number /= 2
        if number % 3 == 0:
            prime_list.append(3)
        if number == 9:
            prime_list.append(3)
        return prime_list
    return int(number)
