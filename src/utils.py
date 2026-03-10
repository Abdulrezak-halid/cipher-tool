"""
Utility Helpers
===============
Shared validation, formatting, and display functions used across the project.
"""

import sys

# ── ANSI colour codes (no external deps) ──────────────────────────────────

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"


# ── Validation helpers ────────────────────────────────────────────────────

def validate_caesar_key(key_str: str) -> int:
    """Parse and validate a Caesar cipher key.

    Args:
        key_str: The raw key string from user input.

    Returns:
        The validated integer key.

    Raises:
        SystemExit: If the key is not a valid integer.
    """
    try:
        return int(key_str)
    except (ValueError, TypeError):
        print(f"{RED}Error:{RESET} Caesar key must be an integer, got '{key_str}'.")
        sys.exit(1)


def validate_vigenere_key(key_str: str) -> str:
    """Validate a Vigenère cipher keyword.

    Args:
        key_str: The raw keyword string from user input.

    Returns:
        The validated keyword string.

    Raises:
        SystemExit: If the keyword contains non-alphabetic characters.
    """
    if not key_str or not key_str.isalpha():
        print(f"{RED}Error:{RESET} Vigenère key must contain only letters, got '{key_str}'.")
        sys.exit(1)
    return key_str


# ── Display helpers ───────────────────────────────────────────────────────

def print_result(label: str, text: str) -> None:
    """Display a labelled result in a consistent coloured format.

    Args:
        label: A short description (e.g. "Encrypted", "Decrypted").
        text:  The result string to display.
    """
    print(f"\n  {GREEN}{BOLD}{label}:{RESET} {text}\n")


def print_error(message: str) -> None:
    """Print an error message in red and exit.

    Args:
        message: The error description.
    """
    print(f"\n  {RED}{BOLD}Error:{RESET} {message}\n")
    sys.exit(1)


def print_banner() -> None:
    """Print the application banner / header."""
    banner = rf"""
{CYAN}{BOLD}
   ╔═══════════════════════════════════════════════════════════╗
   ║             🔐  CIPHER TOOL  v2.0  🔐                   ║
   ║         Classical Cryptography Toolkit                   ║
   ╚═══════════════════════════════════════════════════════════╝
{RESET}"""
    print(banner)


def print_separator(char: str = "─", width: int = 60) -> None:
    """Print a horizontal separator line.

    Args:
        char:  The character to repeat.
        width: How many times to repeat it.
    """
    print(f"  {DIM}{char * width}{RESET}")
