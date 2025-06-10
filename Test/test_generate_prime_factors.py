"""
test_generate_prime_factors.py -- Test cases for prime.py
"""

import pytest
import prime


def prime_number_validation(prime_number):
    """Assert prime factors of a prime is list containing itself"""
    assert prime.generate_prime_factors(prime_number) == [prime_number]


def any_number_validation(number, expected_list):
    """Assert prime factors of input matches list provided"""
    assert prime.generate_prime_factors(number) == expected_list


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
    any_number_validation(4, [2, 2])


def test_six_returns_list_with_two_three():
    """Assert prime factors of 6 is list containing 2,3"""
    any_number_validation(6, [2, 3])


def test_eight_returns_list_with_two_two_two():
    """Assert prime factors of 8 is list containing 2,2,2"""
    any_number_validation(8, [2, 2, 2])


def test_nine_returns_list_with_three_three():
    """Assert prime factors of 9 is list containing 3,3"""
    any_number_validation(9, [3, 3])


def test_prime_numbers():
    """Assert prime factors of a prime is list containing itself"""
    prime_number_validation(5)
    prime_number_validation(11)
    prime_number_validation(43)


def test_non_prime_numbers():
    """Assert factors of each number is list provided"""
    any_number_validation(10, [2, 5])
    any_number_validation(25, [5, 5])
    any_number_validation(18, [2, 3, 3])
    any_number_validation(1234, [2, 617])
    any_number_validation(9999, [3, 3, 11, 101])
