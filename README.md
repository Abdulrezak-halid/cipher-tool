# 🔐 Cipher Tool — Classical Cryptography Toolkit

A professional, modular command-line tool for exploring classical cryptography algorithms. Built for university cybersecurity courses, featuring both a **traditional CLI** and an **interactive terminal UI**.

Supports **Caesar**, **Vigenère**, **Atbash**, and **ROT13** ciphers, plus a **brute-force attack** module.

---

## Installation

**Prerequisites:** Python 3.10+ (no external dependencies).

```bash
git clone https://github.com/your-username/cipher-tool.git
cd cipher-tool
```

No `pip install` needed — uses only the Python standard library.

---

## Two Ways to Use

### 1. Interactive Terminal UI (recommended for learning)

Simply run without arguments:

```bash
python3 main.py
```

You'll see a colourful menu:

```
   ╔═══════════════════════════════════════════════════════════╗
   ║             🔐  CIPHER TOOL  v2.0  🔐                     ║
   ║          Classical Cryptography Toolkit                   ║
   ╚═══════════════════════════════════════════════════════════╝

  Choose an option:

    1)  Caesar Cipher
    2)  Vigenère Cipher
    3)  Atbash Cipher
    4)  ROT13 Cipher
    5)  Caesar Brute-Force Attack
    6)  Algorithm Examples & Explanations
    0)  Exit
```

Option **6** provides step-by-step visual explanations of each algorithm — perfect for understanding how they work.

### 2. Traditional CLI (for scripts & one-liners)

Pass arguments to use the standard CLI:

```bash
python3 main.py --algo <algorithm> --mode <mode> --text "<text>" [--key <key>]
```

| Argument | Required | Values | Description |
|----------|----------|--------|-------------|
| `--algo` | Yes | `caesar`, `vigenere`, `atbash`, `rot13` | Algorithm |
| `--mode` | Yes | `encrypt`, `decrypt`, `brute` | Operation mode |
| `--text` | Yes | Any string | Plaintext or ciphertext |
| `--key`  | No* | Integer (Caesar) / keyword (Vigenère) | Not needed for Atbash, ROT13, brute |

---

## CLI Examples

### Caesar Cipher

```bash
# Encrypt
python3 main.py --algo caesar --mode encrypt --text "HELLO" --key 3
#   Encrypted: KHOOR

# Decrypt
python3 main.py --algo caesar --mode decrypt --text "KHOOR" --key 3
#   Decrypted: HELLO

# Brute-force attack (try all 25 shifts)
python3 main.py --algo caesar --mode brute --text "KHOOR"
```

### Vigenère Cipher

```bash
# Encrypt
python3 main.py --algo vigenere --mode encrypt --text "HELLO" --key KEY
#   Encrypted: RIJVS

# Decrypt
python3 main.py --algo vigenere --mode decrypt --text "RIJVS" --key KEY
#   Decrypted: HELLO
```

### Atbash Cipher

```bash
# Encrypt (no key needed)
python3 main.py --algo atbash --mode encrypt --text "HELLO"
#   Encrypted: SVOOL

# Decrypt
python3 main.py --algo atbash --mode decrypt --text "SVOOL"
#   Decrypted: HELLO
```

### ROT13

```bash
# Encrypt (same as decrypt)
python3 main.py --algo rot13 --mode encrypt --text "HELLO"
#   Encrypted: URYYB

python3 main.py --algo rot13 --mode decrypt --text "URYYB"
#   Decrypted: HELLO
```

### Mixed-Case with Symbols

```bash
python3 main.py --algo caesar --mode encrypt --text "Hello, World! 123" --key 5
#   Encrypted: Mjqqt, Btwqi! 123
```

---

## Algorithm Examples Showcase

Run the examples script to see all algorithms in action:

```bash
python3 examples/examples.py
```

This prints a full demonstration of every cipher with multiple test cases — great for quick reference and presentations.

---

## Algorithm Explanations

### Caesar Cipher

A *monoalphabetic substitution cipher* where each letter is shifted by a fixed key.

```
E(x) = (x + k) mod 26       D(x) = (x − k) mod 26
```

| Plain | A | B | C | … | X | Y | Z |
|-------|---|---|---|---|---|---|---|
| Key=3 | D | E | F | … | A | B | C |

**Weakness:** Only 25 possible keys — trivially broken by brute force.

---

### Vigenère Cipher

A *polyalphabetic substitution cipher* that uses a repeating keyword to vary the shift.

```
Plaintext:  H   E   L   L   O
Keyword:    K   E   Y   K   E
Shift:      10  4   24  10  4
Ciphertext: R   I   J   V   S
```

```
E(i) = (P(i) + K(i)) mod 26       D(i) = (C(i) − K(i)) mod 26
```

**Strength:** Same letter maps to different ciphertext — resists simple frequency analysis.

---

### Atbash Cipher

A *mirror cipher* with no key — each letter maps to its reverse in the alphabet.

```
A ↔ Z,  B ↔ Y,  C ↔ X,  …,  M ↔ N
```

Encrypting twice returns the original text (its own inverse).

---

### ROT13

A Caesar cipher with a fixed shift of **13**.  Since 13 = 26/2, ROT13 is its own inverse.

```
HELLO → URYYB → HELLO
```

Originally used on Usenet to hide spoilers and puzzle answers.

---

## ⚠️ Error Handling

The tool validates all inputs with clear messages:

```bash
# Missing key
python3 main.py --algo caesar --mode encrypt --text "HELLO"
# → Error: --key is required for Caesar encrypt/decrypt.

# Invalid key type
python3 main.py --algo caesar --mode encrypt --text "HELLO" --key abc
# → Error: Caesar key must be an integer, got 'abc'.

# Brute force on Vigenère
python3 main.py --algo vigenere --mode brute --text "RIJVS"
# → Error: Brute-force mode is not supported for the Vigenère cipher.

# Non-alphabetic Vigenère key
python3 main.py --algo vigenere --mode encrypt --text "HELLO" --key 123
# → Error: Vigenère key must contain only letters, got '123'.
```

---

## License

Released for educational purposes. Free to use and modify for coursework and learning.
