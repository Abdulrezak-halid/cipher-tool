"""
Interactive Terminal UI
=======================
A rich, menu-driven terminal interface for exploring classical ciphers.
Uses only the Python standard library (ANSI escape codes for colour).

Launch with:  ``python main.py``  (no arguments)
"""

import os
import sys

from src.ciphers.caesar import caesar_encrypt, caesar_decrypt
from src.ciphers.vigenere import vigenere_encrypt, vigenere_decrypt
from src.ciphers.atbash import atbash_encrypt, atbash_decrypt
from src.ciphers.rot13 import rot13
from src.attacks.brute_force import brute_force_caesar
from src.utils import (
    RESET, BOLD, DIM, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE,
    validate_caesar_key, validate_vigenere_key,
)


# ── Helpers ───────────────────────────────────────────────────────────────

def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause() -> None:
    """Wait for the user to press Enter before continuing."""
    input(f"\n  {DIM}Press Enter to continue...{RESET}")


def read_input(prompt: str) -> str:
    """Read a non-empty line from the user.

    Args:
        prompt: The prompt string to display.

    Returns:
        The stripped user input.
    """
    while True:
        value = input(f"  {CYAN}{prompt}{RESET}").strip()
        if value:
            return value
        print(f"  {RED}Input cannot be empty. Try again.{RESET}")


def print_box(title: str, content: str, colour: str = GREEN) -> None:
    """Print *content* in a simple bordered box.

    Args:
        title:   Box header text.
        content: The main body text.
        colour:  ANSI colour code for the border.
    """
    width = max(len(title), len(content)) + 6
    border = "─" * width
    print(f"\n  {colour}┌{border}┐{RESET}")
    print(f"  {colour}│{RESET}  {BOLD}{title:<{width - 2}}{RESET}  {colour}│{RESET}")
    print(f"  {colour}├{border}┤{RESET}")
    print(f"  {colour}│{RESET}  {content:<{width - 2}}  {colour}│{RESET}")
    print(f"  {colour}└{border}┘{RESET}")


# ── Banner ────────────────────────────────────────────────────────────────

BANNER = rf"""
{CYAN}{BOLD}   ╔═══════════════════════════════════════════════════════════╗
   ║             🔐  CIPHER TOOL  v2.0  🔐                   ║
   ║         Classical Cryptography Toolkit                   ║
   ╚═══════════════════════════════════════════════════════════╝{RESET}
"""


# ── Main Menu ─────────────────────────────────────────────────────────────

MAIN_MENU = f"""
  {BOLD}{WHITE}Choose an option:{RESET}

    {YELLOW}1){RESET}  Caesar Cipher
    {YELLOW}2){RESET}  Vigenère Cipher
    {YELLOW}3){RESET}  Atbash Cipher
    {YELLOW}4){RESET}  ROT13 Cipher
    {YELLOW}5){RESET}  Caesar Brute-Force Attack
    {YELLOW}6){RESET}  Algorithm Examples & Explanations
    {YELLOW}0){RESET}  Exit
"""

MODE_MENU = f"""
  {BOLD}{WHITE}Choose mode:{RESET}

    {YELLOW}1){RESET}  Encrypt
    {YELLOW}2){RESET}  Decrypt
"""


# ── Caesar ────────────────────────────────────────────────────────────────

def ui_caesar() -> None:
    """Interactive Caesar cipher flow."""
    clear_screen()
    print(f"\n  {BOLD}{MAGENTA}━━━  Caesar Cipher  ━━━{RESET}\n")
    print(MODE_MENU)
    mode = read_input("Select (1/2): ")

    text = read_input("Enter text: ")
    key_str = read_input("Enter shift key (integer): ")

    try:
        key = int(key_str)
    except ValueError:
        print(f"  {RED}Invalid key — must be an integer.{RESET}")
        pause()
        return

    if mode == "1":
        result = caesar_encrypt(text, key)
        print_box("Caesar — Encrypted", result)
    elif mode == "2":
        result = caesar_decrypt(text, key)
        print_box("Caesar — Decrypted", result)
    else:
        print(f"  {RED}Invalid choice.{RESET}")

    pause()


# ── Vigenère ──────────────────────────────────────────────────────────────

def ui_vigenere() -> None:
    """Interactive Vigenère cipher flow."""
    clear_screen()
    print(f"\n  {BOLD}{MAGENTA}━━━  Vigenère Cipher  ━━━{RESET}\n")
    print(MODE_MENU)
    mode = read_input("Select (1/2): ")

    text = read_input("Enter text: ")
    keyword = read_input("Enter keyword (letters only): ")

    if not keyword.isalpha():
        print(f"  {RED}Keyword must contain only letters.{RESET}")
        pause()
        return

    if mode == "1":
        result = vigenere_encrypt(text, keyword)
        print_box("Vigenère — Encrypted", result)
    elif mode == "2":
        result = vigenere_decrypt(text, keyword)
        print_box("Vigenère — Decrypted", result)
    else:
        print(f"  {RED}Invalid choice.{RESET}")

    pause()


# ── Atbash ────────────────────────────────────────────────────────────────

def ui_atbash() -> None:
    """Interactive Atbash cipher flow."""
    clear_screen()
    print(f"\n  {BOLD}{MAGENTA}━━━  Atbash Cipher  ━━━{RESET}\n")
    print(MODE_MENU)
    mode = read_input("Select (1/2): ")

    text = read_input("Enter text: ")

    if mode == "1":
        result = atbash_encrypt(text)
        print_box("Atbash — Encrypted", result)
    elif mode == "2":
        result = atbash_decrypt(text)
        print_box("Atbash — Decrypted", result)
    else:
        print(f"  {RED}Invalid choice.{RESET}")

    pause()


# ── ROT13 ─────────────────────────────────────────────────────────────────

def ui_rot13() -> None:
    """Interactive ROT13 flow."""
    clear_screen()
    print(f"\n  {BOLD}{MAGENTA}━━━  ROT13 Cipher  ━━━{RESET}\n")
    print(f"  {DIM}(ROT13 is its own inverse — encrypt = decrypt){RESET}\n")

    text = read_input("Enter text: ")
    result = rot13(text)
    print_box("ROT13 — Result", result)
    pause()


# ── Brute Force ───────────────────────────────────────────────────────────

def ui_brute_force() -> None:
    """Interactive Caesar brute-force flow."""
    clear_screen()
    print(f"\n  {BOLD}{MAGENTA}━━━  Caesar Brute-Force Attack  ━━━{RESET}\n")

    ciphertext = read_input("Enter ciphertext: ")
    results = brute_force_caesar(ciphertext)

    print(f"\n  {BOLD}{'='*55}{RESET}")
    print(f"  {BOLD}  Ciphertext: {ciphertext}{RESET}")
    print(f"  {BOLD}{'='*55}{RESET}\n")

    for shift, plaintext in results:
        print(f"    {YELLOW}Shift {shift:>2}:{RESET}  {plaintext}")

    print(f"\n  {BOLD}{'='*55}{RESET}")
    print(f"  {GREEN}Review the results above to find meaningful text.{RESET}")
    print(f"  {BOLD}{'='*55}{RESET}")
    pause()


# ── Algorithm Examples & Explanations ─────────────────────────────────────

def ui_examples() -> None:
    """Show live algorithm examples with step-by-step explanations."""
    clear_screen()
    print(f"\n  {BOLD}{MAGENTA}━━━  📚 Algorithm Examples & Explanations  ━━━{RESET}\n")

    examples_menu = f"""
  {BOLD}{WHITE}Choose an algorithm to explore:{RESET}

    {YELLOW}1){RESET}  Caesar Cipher — step-by-step
    {YELLOW}2){RESET}  Vigenère Cipher — step-by-step
    {YELLOW}3){RESET}  Atbash Cipher — step-by-step
    {YELLOW}4){RESET}  ROT13 — step-by-step
    {YELLOW}5){RESET}  🔄 Run all examples
    {YELLOW}0){RESET}  Back to main menu
"""
    print(examples_menu)
    choice = read_input("Select: ")

    if choice == "1":
        _example_caesar()
    elif choice == "2":
        _example_vigenere()
    elif choice == "3":
        _example_atbash()
    elif choice == "4":
        _example_rot13()
    elif choice == "5":
        _example_caesar()
        _example_vigenere()
        _example_atbash()
        _example_rot13()
    elif choice == "0":
        return
    else:
        print(f"  {RED}Invalid choice.{RESET}")

    pause()


def _example_caesar() -> None:
    """Print a detailed Caesar cipher example."""
    text = "HELLO"
    key = 3
    encrypted = caesar_encrypt(text, key)
    decrypted = caesar_decrypt(encrypted, key)

    print(f"""
  {CYAN}{BOLD}┌────────────────────────────────────────────────────┐
  │              CAESAR CIPHER  (Shift Cipher)         │
  └────────────────────────────────────────────────────┘{RESET}

  {BOLD}How it works:{RESET}
    Each letter is shifted forward by a fixed number (the key).
    Formula:  E(x) = (x + k) mod 26

  {BOLD}Example — Key = {key}:{RESET}

    Alphabet:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    Shifted +3: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

  {BOLD}Step-by-step:{RESET}
    H (pos  7) + 3 = K (pos 10)
    E (pos  4) + 3 = H (pos  7)
    L (pos 11) + 3 = O (pos 14)
    L (pos 11) + 3 = O (pos 14)
    O (pos 14) + 3 = R (pos 17)

  {GREEN}Plaintext  →  {text}
  Ciphertext →  {encrypted}
  Decrypt    →  {decrypted}{RESET}
""")


def _example_vigenere() -> None:
    """Print a detailed Vigenère cipher example."""
    text = "HELLO"
    keyword = "KEY"
    encrypted = vigenere_encrypt(text, keyword)
    decrypted = vigenere_decrypt(encrypted, keyword)

    print(f"""
  {CYAN}{BOLD}┌────────────────────────────────────────────────────┐
  │           VIGENÈRE CIPHER  (Polyalphabetic)        │
  └────────────────────────────────────────────────────┘{RESET}

  {BOLD}How it works:{RESET}
    Uses a repeating keyword to vary the shift for each letter.
    Formula:  E(i) = (P(i) + K(i)) mod 26

  {BOLD}Example — Keyword = "{keyword}":{RESET}

    Plaintext:  H   E   L   L   O
    Keyword:    K   E   Y   K   E
    Shift:      10  4   24  10  4

  {BOLD}Step-by-step:{RESET}
    H (7)  + K (10) = R (17)
    E (4)  + E (4)  = I (8)
    L (11) + Y (24) = J (9)     ← wraps around!
    L (11) + K (10) = V (21)
    O (14) + E (4)  = S (18)

  {GREEN}Plaintext  →  {text}
  Ciphertext →  {encrypted}
  Decrypt    →  {decrypted}{RESET}
""")


def _example_atbash() -> None:
    """Print a detailed Atbash cipher example."""
    text = "HELLO"
    encrypted = atbash_encrypt(text)
    decrypted = atbash_decrypt(encrypted)

    print(f"""
  {CYAN}{BOLD}┌────────────────────────────────────────────────────┐
  │           ATBASH CIPHER  (Mirror Cipher)           │
  └────────────────────────────────────────────────────┘{RESET}

  {BOLD}How it works:{RESET}
    Each letter is replaced by its mirror in the alphabet.
    A↔Z, B↔Y, C↔X, D↔W, …, M↔N
    No key needed — the mapping is fixed.

  {BOLD}Mapping:{RESET}
    Plain:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    Cipher:  Z Y X W V U T S R Q P O N M L K J I H G F E D C B A

  {BOLD}Step-by-step:{RESET}
    H (pos  7)  → S (pos 18)    mirror: 25 - 7  = 18
    E (pos  4)  → V (pos 21)    mirror: 25 - 4  = 21
    L (pos 11)  → O (pos 14)    mirror: 25 - 11 = 14
    L (pos 11)  → O (pos 14)    mirror: 25 - 11 = 14
    O (pos 14)  → L (pos 11)    mirror: 25 - 14 = 11

  {GREEN}Plaintext  →  {text}
  Ciphertext →  {encrypted}
  Decrypt    →  {decrypted}{RESET}

  {DIM}Note: Atbash is its own inverse — encrypting twice returns the original.{RESET}
""")


def _example_rot13() -> None:
    """Print a detailed ROT13 example."""
    text = "HELLO"
    result = rot13(text)
    back = rot13(result)

    print(f"""
  {CYAN}{BOLD}┌────────────────────────────────────────────────────┐
  │           ROT13  (Caesar with key=13)              │
  └────────────────────────────────────────────────────┘{RESET}

  {BOLD}How it works:{RESET}
    ROT13 is a special Caesar cipher with a fixed shift of 13.
    Since 13 is half of 26, applying ROT13 twice returns the original.

  {BOLD}Step-by-step:{RESET}
    H (pos  7)  + 13 = U (pos 20)
    E (pos  4)  + 13 = R (pos 17)
    L (pos 11)  + 13 = Y (pos 24)
    L (pos 11)  + 13 = Y (pos 24)
    O (pos 14)  + 13 = B (pos  1)    ← wraps around!

  {GREEN}Original   →  {text}
  ROT13      →  {result}
  ROT13 x2   →  {back}   (back to original!){RESET}

  {DIM}Fun fact: ROT13 was commonly used on Usenet to hide spoilers.{RESET}
""")


# ── Main Loop ─────────────────────────────────────────────────────────────

def ui_main() -> None:
    """Launch the interactive terminal UI main loop."""
    while True:
        clear_screen()
        print(BANNER)
        print(MAIN_MENU)

        choice = read_input("Select: ")

        if choice == "1":
            ui_caesar()
        elif choice == "2":
            ui_vigenere()
        elif choice == "3":
            ui_atbash()
        elif choice == "4":
            ui_rot13()
        elif choice == "5":
            ui_brute_force()
        elif choice == "6":
            ui_examples()
        elif choice == "0":
            print(f"\n  {GREEN}Goodbye! 👋{RESET}\n")
            sys.exit(0)
        else:
            print(f"  {RED}Invalid option — please pick 0-6.{RESET}")
            pause()
