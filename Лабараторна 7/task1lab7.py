n = int(input("Введіть кількість слів: "))
words = []
for i in range(n):
    w = input("Слово: ").strip()
    if w not in words:
        words.append(w)
result = " ".join(words)
print(result)