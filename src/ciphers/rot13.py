"""
ROT13 Cipher Module
===================
ROT13 ("rotate by 13 places") is a special case of the Caesar cipher with a
fixed shift of 13.  Because 13 is exactly half of 26, applying ROT13 twice
returns the original text — encryption and decryption are the same function.

Non-alphabetic characters are preserved.
"""

from src.ciphers.caesar import caesar_encrypt


def rot13(text: str) -> str:
    """Apply ROT13 to *text* (encrypt **or** decrypt).

    Args:
        text: The input string.

    Returns:
        The ROT13-transformed string.

    Example:
        >>> rot13("HELLO")
        'URYYB'
        >>> rot13("URYYB")
        'HELLO'
    """
    return caesar_encrypt(text, 13)
