"""Decisions and repetition: if, for, and while."""

amounts = [2200, 1500, 1400, 6200, 800]

for amount in amounts:
    if amount >= 5000:
        label = "large"
    elif amount >= 1500:
        label = "medium"
    else:
        label = "small"
    print(f"{amount}: {label}")

running = 0
index = 0
while running < 5000:
    running += amounts[index]
    index += 1
print(f"It took {index} sales to pass 5000 (running total {running}).")
