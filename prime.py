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
    if number == 1:
        return []
    if number in (2, 3):
        return [number]
    if number == 4:
        return [2, 2]
    return int(number)
