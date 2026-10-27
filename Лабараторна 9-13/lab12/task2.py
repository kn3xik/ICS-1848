import random

Масті = ["♠", "♥", "♦", "♣"]
Цифри = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
Колода = [r + s for s in Масті for r in Цифри]


def take_cards(Колода, count):
    hand = random.sample(Колода, count)
    for card in hand:
        Колода.remove(card)
    return hand


n = int(input("Кількість гравців: "))
if n * 6 > len(Колода):
    print(f"У колоді лише {len(Колода)} карт, максимум гравців: {len(Колода) // 6}")
else:
    for i in range(1, n + 1):
        print(f"Гравець {i}:", " ".join(take_cards(Колода, 6)))
