"""
Caesar Brute-Force Attack Module
=================================
Tries every possible Caesar shift (1–25) against a given ciphertext and
displays each result so the user can visually identify the correct plaintext.
"""

from src.ciphers.caesar import caesar_decrypt


def brute_force_caesar(ciphertext: str) -> list[tuple[int, str]]:
    """Try all 25 meaningful Caesar shifts and return the results.

    Shift 0 is excluded because it reproduces the ciphertext unchanged.

    Args:
        ciphertext: The encrypted string to attack.

    Returns:
        A list of ``(shift, decrypted_text)`` tuples for shifts 1–25.
    """
    results: list[tuple[int, str]] = []

    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        results.append((shift, decrypted))

    return results


def print_brute_force_results(ciphertext: str) -> None:
    """Run the brute-force attack and pretty-print every candidate.

    Args:
        ciphertext: The encrypted string to attack.
    """
    results = brute_force_caesar(ciphertext)

    print(f"\n{'='*60}")
    print("  Caesar Brute-Force Attack")
    print(f"  Ciphertext: {ciphertext}")
    print(f"{'='*60}\n")

    for shift, plaintext in results:
        print(f"  Shift {shift:>2}: {plaintext}")

    print(f"\n{'='*60}")
    print("  Review the results above to identify meaningful plaintext.")
    print(f"{'='*60}\n")
