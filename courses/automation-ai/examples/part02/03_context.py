"""A context window has a fixed size. When it is full, the oldest text falls out."""

WINDOW = 12  # words the model can "see" (real models count tokens, and hold far more)

conversation = [
    "My name is Daniela",
    "I work at Cafe Central",
    "Please summarise January sales",
    "Now compare with February",
]

kept: list[str] = []
size = 0
for message in reversed(conversation):
    length = len(message.split())
    if size + length > WINDOW:
        break
    kept.insert(0, message)
    size += length

print(f"Window size: {WINDOW} words")
print(f"Messages kept ({size} words):")
for message in kept:
    print(f"  {message}")
print(f"Forgotten: {len(conversation) - len(kept)} message(s)")
