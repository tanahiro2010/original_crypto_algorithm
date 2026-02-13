def text_to_char_list(text) -> list:    
    """Convert a string of text into a list of its individual characters.

    Args:
        text (str): The input string.

    Returns:
        list: A list of characters in the string.
    """    
    return list(text)

def char_to_unicode(char) -> int:
    """Convert a single character to its Unicode code point.

    Args:
        char (str): A single character string.

    Returns:
        int: The Unicode code point of the character.

    Raises:
        ValueError: If the input is not a single character string.
    """
    if len(char) != 1:
        raise ValueError("Input must be a single character string.")
    return ord(char)

def unicode_to_char(code_point) -> str:
    """Convert a Unicode code point to its corresponding character.

    Args:
        code_point (int): The Unicode code point.

    Returns:
        str: The character corresponding to the Unicode code point.

    Raises:
        ValueError: If the input is not a valid Unicode code point.
    """
    if not (0 <= code_point <= 0x10FFFF):
        raise ValueError("Input must be a valid Unicode code point.")
    return chr(code_point)

def main():
    # Example usage
    text = "Hello, World! こんにちは"
    char_list = text_to_char_list(text)
    unicode_list: list[int] = [char_to_unicode(c) for c in char_list]
    print("Character List:", char_list)
    print("Unicode List:", unicode_list)
    decoded_chars: list[str] = [unicode_to_char(code) for code in unicode_list]
    print("Decoded Characters:", decoded_chars)
    return

if __name__ == "__main__":
    main()