"""
Atbash Cipher Module
====================
Implements the Atbash cipher — a monoalphabetic substitution cipher that
maps each letter to its reverse in the alphabet.

    A ↔ Z,  B ↔ Y,  C ↔ X,  …,  M ↔ N

The Atbash cipher is its own inverse: encrypting twice returns the
original plaintext, so encrypt and decrypt are the same operation.
Non-alphabetic characters are preserved.
"""


def _atbash_transform(text: str) -> str:
    """Apply the Atbash substitution to *text*.

    Each letter is replaced by its mirror in the alphabet:
    ``A`` ↔ ``Z``, ``B`` ↔ ``Y``, etc.
    Case is preserved.  Non-letter characters pass through unchanged.

    Args:
        text: The input string.

    Returns:
        The transformed string.
    """
    result: list[str] = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Mirror: position 0 → 25, position 1 → 24, …
            mirrored = base + (25 - (ord(char) - base))
            result.append(chr(mirrored))
        else:
            result.append(char)

    return "".join(result)


def atbash_encrypt(text: str) -> str:
    """Encrypt plaintext using the Atbash cipher.

    Args:
        text: The plaintext string.

    Returns:
        The encrypted ciphertext.

    Example:
        >>> atbash_encrypt("HELLO")
        'SVOOL'
    """
    return _atbash_transform(text)


def atbash_decrypt(text: str) -> str:
    """Decrypt Atbash ciphertext (same operation as encryption).

    Args:
        text: The ciphertext string.

    Returns:
        The decrypted plaintext.

    Example:
        >>> atbash_decrypt("SVOOL")
        'HELLO'
    """
    return _atbash_transform(text)
