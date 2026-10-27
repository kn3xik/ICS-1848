import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("one.txt", encoding="utf-8") as f:
    profit = json.load(f)        # {"фірма": прибуток}
with open("two.txt", encoding="utf-8") as f:
    staff = json.load(f)         # {"фірма": кількість співробітників}

print(f"{'Фірма':<15}{'Прибуток':>12}{'Співробітників':>16}")
best_name, best_value = None, -1
for name in profit:
    p, n = profit[name], staff[name]
    print(f"{name:<15}{p:>12}{n:>16}")
    if p / n > best_value:
        best_name, best_value = name, p / n

print(f"\nНайефективніше працює фірма {best_name} "
      f"(прибуток на 1 працівника: {best_value:.2f})")