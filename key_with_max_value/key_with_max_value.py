data = {"a": 10, "b": 50, "c": 20}
result = max(data, key=data.get)
print(result)

# Easier version
# max_key = None
# max_value = float("-inf")

# for k, v in data.items():
#     if v > max_value:
#         max_value = v
#         max_key = k

# print(max_key)
