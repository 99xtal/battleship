"""Contains wrapper functions for os, sys functions which control console"""

import os
import sys


def clear_screen():
    """Clear all text from screen (os.system('cls') wrapper)"""
    os.system("cls" if os.name == "nt" else "clear")


def close_window():
    """Close terminal window (sys.exit() wrapper)"""
    sys.exit()


def set_window_size(cols: int, lines: int):
    """Set size of console window

    cols : int
        sets width of window based on number of character columns
    lines : int
        sets height of window based on number of text lines
    """
    os.system(f"mode con: cols={cols} lines={lines}")
