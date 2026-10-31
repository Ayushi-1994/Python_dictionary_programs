data = {"a": 5, "b": 1, "c": 3}

print(data.items())
print(sorted(data.items(), key=lambda item: item[1]))

result = dict(sorted(data.items(), key=lambda item: item[1]))
print(result)
