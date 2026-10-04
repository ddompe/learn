"""Absolute and relative paths on Windows and on macOS/Linux."""

from pathlib import PurePosixPath, PureWindowsPath

windows = PureWindowsPath(r"C:\Users\Daniela\Documents\cafe-central\cafe_central_sales.csv")
mac = PurePosixPath("/Users/daniela/Documents/cafe-central/cafe_central_sales.csv")

print("Windows absolute:", windows)
print("Windows is absolute:", windows.is_absolute())
print("Windows folder:", windows.parent)
print("macOS file name:", mac.name)
print("macOS extension:", mac.suffix)
print("macOS is absolute:", mac.is_absolute())

relative = PurePosixPath("cafe-central/cafe_central_sales.csv")
print("Relative path is absolute:", relative.is_absolute())
print("Relative path parts:", relative.parts)
