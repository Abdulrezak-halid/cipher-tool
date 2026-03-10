"""
CLI Module — argparse-based Command-Line Interface
====================================================
Provides the traditional ``--algo / --mode / --text / --key`` interface
that can be used in scripts and one-liners.
"""

import argparse
import sys

from src.ciphers.caesar import caesar_encrypt, caesar_decrypt
from src.ciphers.vigenere import vigenere_encrypt, vigenere_decrypt
from src.ciphers.atbash import atbash_encrypt, atbash_decrypt
from src.ciphers.rot13 import rot13
from src.attacks.brute_force import print_brute_force_results
from src.utils import validate_caesar_key, validate_vigenere_key, print_result, print_error


# ── Argument Parser ───────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    """Create and return the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="cipher-tool",
        description=(
            "Classical Cryptography Tool — Encrypt, decrypt, and brute-force "
            "Caesar, Vigenère, Atbash, and ROT13 ciphers."
        ),
        epilog=(
            "Examples:\n"
            '  python main.py --algo caesar   --mode encrypt --text "HELLO" --key 3\n'
            '  python main.py --algo caesar   --mode brute   --text "KHOOR"\n'
            '  python main.py --algo vigenere --mode encrypt --text "HELLO" --key KEY\n'
            '  python main.py --algo atbash   --mode encrypt --text "HELLO"\n'
            '  python main.py --algo rot13    --mode encrypt --text "HELLO"\n'
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--algo",
        required=True,
        choices=["caesar", "vigenere", "atbash", "rot13"],
        help="Cipher algorithm to use.",
    )
    parser.add_argument(
        "--mode",
        required=True,
        choices=["encrypt", "decrypt", "brute"],
        help="Operation mode: encrypt, decrypt, or brute (Caesar only).",
    )
    parser.add_argument(
        "--text",
        required=True,
        help="Input plaintext or ciphertext.",
    )
    parser.add_argument(
        "--key",
        required=False,
        default=None,
        help=(
            "Cipher key — integer shift for Caesar, alphabetic keyword for "
            "Vigenère.  Not needed for Atbash, ROT13, or brute-force mode."
        ),
    )

    return parser


# ── Dispatch Handlers ─────────────────────────────────────────────────────

def handle_caesar(mode: str, text: str, key_str: str | None) -> None:
    """Route a Caesar cipher request."""
    if mode == "brute":
        print_brute_force_results(text)
        return

    if key_str is None:
        print_error("--key is required for Caesar encrypt/decrypt.")

    key = validate_caesar_key(key_str)

    if mode == "encrypt":
        print_result("Encrypted", caesar_encrypt(text, key))
    else:
        print_result("Decrypted", caesar_decrypt(text, key))


def handle_vigenere(mode: str, text: str, key_str: str | None) -> None:
    """Route a Vigenère cipher request."""
    if mode == "brute":
        print_error("Brute-force mode is not supported for the Vigenère cipher.")

    if key_str is None:
        print_error("--key is required for Vigenère encrypt/decrypt.")

    keyword = validate_vigenere_key(key_str)

    if mode == "encrypt":
        print_result("Encrypted", vigenere_encrypt(text, keyword))
    else:
        print_result("Decrypted", vigenere_decrypt(text, keyword))


def handle_atbash(mode: str, text: str) -> None:
    """Route an Atbash cipher request."""
    if mode == "brute":
        print_error("Brute-force mode is not applicable to Atbash (no key).")

    if mode == "encrypt":
        print_result("Encrypted", atbash_encrypt(text))
    else:
        print_result("Decrypted", atbash_decrypt(text))


def handle_rot13(mode: str, text: str) -> None:
    """Route a ROT13 request."""
    if mode == "brute":
        print_error("Brute-force mode is not applicable to ROT13 (fixed key).")

    # ROT13 encrypt == decrypt
    label = "Encrypted" if mode == "encrypt" else "Decrypted"
    print_result(label, rot13(text))


# ── Entry Point ───────────────────────────────────────────────────────────

def cli_main() -> None:
    """Parse CLI arguments and dispatch to the correct handler."""
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "caesar": lambda: handle_caesar(args.mode, args.text, args.key),
        "vigenere": lambda: handle_vigenere(args.mode, args.text, args.key),
        "atbash": lambda: handle_atbash(args.mode, args.text),
        "rot13": lambda: handle_rot13(args.mode, args.text),
    }

    handler = dispatch.get(args.algo)
    if handler:
        handler()
    else:
        print_error(f"Unknown algorithm '{args.algo}'.")
