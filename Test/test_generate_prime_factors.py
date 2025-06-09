"""
test_generate_prime_factors.py -- Test cases for prime.py
"""

import pytest
import prime


def prime_number_validation(prime_number):
    """Assert prime factors of a prime is list containing itself"""
    assert prime.generate_prime_factors(prime_number) == [prime_number]


def test_invalid_datatype():
    """Assert non-integer raises a ValueError"""
    with pytest.raises(Exception):
        prime.generate_prime_factors('hello')


def test_one_returns_empty_list():
    """Assert prime factors of 1 is an empty list"""
    assert prime.generate_prime_factors(1) == []


def test_two_returns_list_with_two():
    """Assert prime factors of 2 is list containing 2"""
    prime_number_validation(2)


def test_three_returns_list_with_three():
    """Assert prime factors of 3 is list containing 3"""
    prime_number_validation(3)


def test_four_returns_list_with_two_two():
    """Assert prime factors of 4 is list containing 2,2"""
    assert prime.generate_prime_factors(4) == [2, 2]


def test_six_returns_list_with_two_three():
    """Assert prime factors of 6 is list containing 2,3"""
    assert prime.generate_prime_factors(6) == [2, 3]
