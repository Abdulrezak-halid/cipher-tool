#!/usr/bin/env python3
"""
examples.py — Pre-built Algorithm Examples
============================================
Run this script to see every cipher in action with sample inputs and
detailed output.  Great for demos and quick reference.

Usage:
    python -m examples.examples
    # or from project root:
    python examples/examples.py
"""

import sys
import os

# Ensure the project root is on the path so src imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.ciphers.caesar import caesar_encrypt, caesar_decrypt
from src.ciphers.vigenere import vigenere_encrypt, vigenere_decrypt
from src.ciphers.atbash import atbash_encrypt, atbash_decrypt
from src.ciphers.rot13 import rot13
from src.attacks.brute_force import brute_force_caesar


# ── Helpers ───────────────────────────────────────────────────────────────

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def header(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {BOLD}{CYAN}{title}{RESET}")
    print(f"{'='*60}\n")


def show(label: str, value: str) -> None:
    print(f"  {YELLOW}{label:>14}{RESET}:  {value}")


# ── Examples ──────────────────────────────────────────────────────────────

def caesar_examples() -> None:
    header("CAESAR CIPHER EXAMPLES")

    for text, key in [("HELLO", 3), ("MERHABA", 5), ("Hello, World! 123", 7)]:
        enc = caesar_encrypt(text, key)
        dec = caesar_decrypt(enc, key)
        show("Plaintext", text)
        show(f"Key", str(key))
        show("Encrypted", enc)
        show("Decrypted", dec)
        print()


def vigenere_examples() -> None:
    header("VIGENÈRE CIPHER EXAMPLES")

    for text, kw in [("HELLO", "KEY"), ("ATTACKATDAWN", "LEMON"), ("Hello World", "SECRET")]:
        enc = vigenere_encrypt(text, kw)
        dec = vigenere_decrypt(enc, kw)
        show("Plaintext", text)
        show("Keyword", kw)
        show("Encrypted", enc)
        show("Decrypted", dec)
        print()


def atbash_examples() -> None:
    header("ATBASH CIPHER EXAMPLES")

    for text in ["HELLO", "ZYXWV", "Attack at Dawn!"]:
        enc = atbash_encrypt(text)
        dec = atbash_decrypt(enc)
        show("Plaintext", text)
        show("Encrypted", enc)
        show("Decrypted", dec)
        print()


def rot13_examples() -> None:
    header("ROT13 EXAMPLES")

    for text in ["HELLO", "URYYB", "The Quick Brown Fox"]:
        result = rot13(text)
        back = rot13(result)
        show("Input", text)
        show("ROT13", result)
        show("ROT13 x2", back)
        print()


def brute_force_example() -> None:
    header("CAESAR BRUTE-FORCE ATTACK")

    ciphertext = "KHOOR"
    print(f"  Ciphertext: {ciphertext}\n")
    results = brute_force_caesar(ciphertext)
    for shift, pt in results:
        marker = f"  {GREEN}← found!{RESET}" if pt == "HELLO" else ""
        print(f"    Shift {shift:>2}: {pt}{marker}")
    print()


# ── Main ──────────────────────────────────────────────────────────────────

def main() -> None:
    print(f"\n{BOLD}{CYAN}{'*'*60}")
    print(f"    CIPHER TOOL — ALGORITHM EXAMPLES SHOWCASE")
    print(f"{'*'*60}{RESET}")

    caesar_examples()
    vigenere_examples()
    atbash_examples()
    rot13_examples()
    brute_force_example()

    print(f"{DIM}  All examples completed successfully.{RESET}\n")


if __name__ == "__main__":
    main()
