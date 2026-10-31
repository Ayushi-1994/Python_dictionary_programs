words = ["cat", "dog", "apple", "ball"]

result = {}

for word in words:
    length = len(word)
    result.setdefault(length, []).append(word)

print(result)
