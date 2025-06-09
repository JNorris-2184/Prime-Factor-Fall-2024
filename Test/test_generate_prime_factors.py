"""
test_generate_prime_factors.py -- Test cases for prime.py
"""

import pytest
import prime


def test_invalid_datatype():
    """Assert non-integer raises a ValueError"""
    with pytest.raises(Exception):
        prime.generate_prime_factors('hello')


def test_one_returns_empty_list():
    """Assert prime factors of 1 is an empty list"""
    assert prime.generate_prime_factors(1) == []
