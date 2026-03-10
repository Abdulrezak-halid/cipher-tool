#!/usr/bin/env python3
"""
main.py — Cipher Tool Entry Point
===================================
Launches either the **interactive UI** or the **argparse CLI** depending
on whether command-line arguments are provided.

Usage:
    python main.py                     →  Interactive menu UI
    python main.py --algo caesar ...   →  Traditional CLI mode
"""

import sys


def main() -> None:
    """Detect the execution mode and dispatch accordingly.

    - If no arguments (or only ``--help``): launch the interactive UI.
    - If arguments are supplied: use the argparse-based CLI.
    """
    # If the user passed any --flags, use CLI mode
    if len(sys.argv) > 1:
        from src.cli import cli_main
        cli_main()
    else:
        from src.ui import ui_main
        ui_main()


if __name__ == "__main__":
    main()
