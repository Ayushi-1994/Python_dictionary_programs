sentence = "python is easy python is powerful"

freq = {}

for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)
