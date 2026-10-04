"""Decimal units (KB) versus binary units (KiB), and why a 1 TB disk shows less."""

KB = 1000
KIB = 1024

disk_bytes = 1 * KB**4  # a "1 TB" disk, as the maker counts it
disk_in_gib = disk_bytes / KIB**3  # what the operating system reports

print(f"1 KB  = {KB} bytes")
print(f"1 KiB = {KIB} bytes")
print(f"A 1 TB disk holds {disk_bytes} bytes")
print(f"The operating system shows it as {disk_in_gib:.0f} GiB")
