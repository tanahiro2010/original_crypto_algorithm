from lib.algos import xor
from lib.char import text_to_char_list, char_to_unicode, unicode_to_char
from lib.radix import binary_to_decimal, decimal_to_binary

def encode(text: str) -> str:
    text_chars = text_to_char_list(text)
    unicode_values = [char_to_unicode(c) for c in text_chars]
    binary_values = [decimal_to_binary(u) for u in unicode_values]

    
    
    key = 12345  # Example fixed key for XOR operation
    return

def decode(encoded_text: str) -> str:

    return