"""
Vigenère Cipher Module
======================
Implements encryption and decryption using the Vigenère polyalphabetic cipher.

The Vigenère cipher applies a different Caesar shift to each letter in the
plaintext, cycling through shifts derived from a repeating keyword.
Non-alphabetic characters are preserved and do not consume keyword letters.
"""


def _extend_keyword(text: str, keyword: str) -> str:
    """Repeat the keyword to align with alphabetic positions in *text*.

    Non-alphabetic characters in *text* are skipped — the keyword only
    advances for letters.

    Args:
        text:    The plaintext / ciphertext.
        keyword: The keyword string (letters only).

    Returns:
        A string the same length as *text* where each position that
        corresponds to a letter holds the appropriate keyword character
        and every other position holds a null character.
    """
    extended: list[str] = []
    keyword_index = 0
    keyword_upper = keyword.upper()

    for char in text:
        if char.isalpha():
            extended.append(keyword_upper[keyword_index % len(keyword_upper)])
            keyword_index += 1
        else:
            extended.append('\x00')

    return "".join(extended)


def vigenere_encrypt(text: str, keyword: str) -> str:
    """Encrypt plaintext using the Vigenère cipher.

    Each alphabetic character is shifted by the corresponding keyword
    letter's position (A=0, B=1, …, Z=25).  Non-alphabetic characters
    are left unchanged and do not advance the keyword index.

    Args:
        text:    The plaintext string to encrypt.
        keyword: The keyword string (must contain only letters).

    Returns:
        The encrypted ciphertext string.

    Example:
        >>> vigenere_encrypt("HELLO", "KEY")
        'RIJVS'
    """
    extended_key = _extend_keyword(text, keyword)
    result: list[str] = []

    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(extended_key[i]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            encrypted = (ord(char) - base + shift) % 26 + base
            result.append(chr(encrypted))
        else:
            result.append(char)

    return "".join(result)


def vigenere_decrypt(text: str, keyword: str) -> str:
    """Decrypt ciphertext that was encrypted with the Vigenère cipher.

    Each alphabetic character is shifted *backward* by the corresponding
    keyword letter's position.

    Args:
        text:    The ciphertext string to decrypt.
        keyword: The keyword string used during encryption.

    Returns:
        The decrypted plaintext string.

    Example:
        >>> vigenere_decrypt("RIJVS", "KEY")
        'HELLO'
    """
    extended_key = _extend_keyword(text, keyword)
    result: list[str] = []

    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(extended_key[i]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            decrypted = (ord(char) - base - shift) % 26 + base
            result.append(chr(decrypted))
        else:
            result.append(char)

    return "".join(result)
