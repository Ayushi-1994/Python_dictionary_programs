data = {"a": 10, "b": 50, "c": 20}

result = min(data, key=data.get)

print(result)
