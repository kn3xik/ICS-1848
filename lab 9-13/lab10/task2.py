import os
import shutil

# работать в папке, где лежит сам скрипт
os.chdir(os.path.dirname(os.path.abspath(__file__)))

dest = r"D:\SIGNAL"
os.makedirs(dest, exist_ok=True)

count = 0
for name in os.listdir("."):
    if os.path.isfile(name) and name.lower().endswith(".whl"):
        shutil.copy(name, os.path.join(dest, name))
        print("Скопійовано:", name)
        count += 1
print("Всього скопійовано файлів:", count)