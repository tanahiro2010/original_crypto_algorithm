from lib.algos import xor
from lib.char import text_to_char_list, char_to_unicode, unicode_to_char
from lib.radix import binary_to_decimal, decimal_to_binary
from lib.key import generate_key

def encode(text: str) -> str:
    text_chars = text_to_char_list(text)
    unicode_values = [char_to_unicode(c) for c in text_chars]
    binary_values = [decimal_to_binary(u) for u in unicode_values]
    key = generate_key(text)

    print(f"Text: {text}")
    print(f"Unicode Values: {unicode_values}")
    print(f"Binary Values: {binary_values}")
    print(f"Generated Key: {key}")
    return

def decode(encoded_text: str) -> str:

    return