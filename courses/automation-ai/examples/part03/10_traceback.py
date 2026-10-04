"""Cause an error on purpose and show how a traceback points to where it happened."""

import traceback
from pathlib import Path


def read_sales(name):
    return Path(name).read_text(encoding="utf-8")


def main():
    return read_sales("no_such_file.csv")


try:
    main()
except FileNotFoundError as error:
    print(f"Error type: {type(error).__name__}")
    print("Call chain in this file, oldest first:")
    for frame in traceback.extract_tb(error.__traceback__):
        if frame.filename == __file__:
            print(f"  line {frame.lineno}: in {frame.name}")
