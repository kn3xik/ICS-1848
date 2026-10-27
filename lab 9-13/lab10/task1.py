import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

keys = ["ось", "в", "сонечко", "квіти", "спів", "повітря"]

with open("site.txt", encoding="utf-8") as f:
    text = f.read().lower()

words = re.findall(r"\w+", text)

with open("fr.txt", "w", encoding="utf-8") as out:
    for key in keys:
        count = words.count(key.lower())
        out.write(f"{key}={count}\n")
        print(f"{key}={count}")