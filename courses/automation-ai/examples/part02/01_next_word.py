"""A toy language model: predict the next word by counting what followed before."""

from collections import Counter, defaultdict

text = (
    "the cafe sells coffee and the cafe sells cake and the cafe sells coffee "
    "and the shop sells coffee"
)
words = text.split()

followers: dict[str, Counter] = defaultdict(Counter)
for current, nxt in zip(words, words[1:]):
    followers[current][nxt] += 1

for word in ("the", "sells"):
    counts = followers[word]
    best, seen = counts.most_common(1)[0]
    print(f"After '{word}': {dict(counts)} -> predict '{best}' ({seen} of {sum(counts.values())})")
