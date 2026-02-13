"""
lib.radix の Docstring
This module provides functions for encoding and decoding text.
"""

def binary_to_decimal(binary_str: str) -> int:
    """Convert a binary string (base-2) to a decimal integer (base-10).

    Args:
        binary_str (str): The binary string to convert.

    Returns:
        int: The decimal integer representation of the binary string.

    Raises:
        ValueError: If the input string is not a valid binary string.
    """
    try:
        return int(binary_str, 2)
    except ValueError:
        raise ValueError("Input must be a valid binary string.")


def decimal_to_binary(decimal_int: int) -> str:
    """Convert a decimal integer (base-10) to a binary string (base-2).

    Args:
        decimal_int (int): The decimal integer to convert.

    Returns:
        str: The binary string representation of the decimal integer.
    """
    if decimal_int < 0:
        raise ValueError("Input must be a non-negative integer.")
    return bin(decimal_int)[2:]  # Remove the '0b' prefix


# Backwards-compatible aliases (deprecated)
def two_radix_to_ten_radix(binary_str: str) -> int:
    import warnings
    warnings.warn('two_radix_to_ten_radix is deprecated; use binary_to_decimal', DeprecationWarning)
    return binary_to_decimal(binary_str)


def ten_radix_to_two_radix(decimal_int: int) -> str:
    import warnings
    warnings.warn('ten_radix_to_two_radix is deprecated; use decimal_to_binary', DeprecationWarning)
    return decimal_to_binary(decimal_int)
