"""
Caesar Cipher Module
====================
Implements encryption and decryption using the Caesar (shift) cipher.

The Caesar cipher shifts each letter in the plaintext by a fixed number
of positions in the alphabet. Non-alphabetic characters are preserved.
"""


def caesar_encrypt(text: str, key: int) -> str:
    """Encrypt plaintext using the Caesar cipher.

    Each alphabetic character is shifted forward by ``key`` positions.
    Non-alphabetic characters (digits, symbols, spaces) are unchanged.

    Args:
        text: The plaintext string to encrypt.
        key:  The integer shift value (0–25 meaningful range).

    Returns:
        The encrypted ciphertext string.

    Example:
        >>> caesar_encrypt("HELLO", 3)
        'KHOOR'
    """
    result: list[str] = []
    shift = key % 26

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)

    return "".join(result)


def caesar_decrypt(text: str, key: int) -> str:
    """Decrypt ciphertext that was encrypted with the Caesar cipher.

    Decryption is simply encryption with the negated key.

    Args:
        text: The ciphertext string to decrypt.
        key:  The integer shift value used during encryption.

    Returns:
        The decrypted plaintext string.

    Example:
        >>> caesar_decrypt("KHOOR", 3)
        'HELLO'
    """
    return caesar_encrypt(text, -key)
