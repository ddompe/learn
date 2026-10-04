"""Text is stored as bytes. Reading with the wrong encoding garbles accents."""

word = "Categoría"

utf8_bytes = word.encode("utf-8")
print("UTF-8 bytes:", utf8_bytes)

wrong = utf8_bytes.decode("latin-1")
print("Read as Latin-1:", wrong)

repaired = wrong.encode("latin-1").decode("utf-8")
print("Repaired:", repaired)
