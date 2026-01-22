# --- 1. Break Komutu (Döngüyü Kırma) ---
name = 'Yusuf arı'

for letter in name:
    if letter == 'a':
        break # 'a' harfini gördüğü anda döngü tamamen biter.
    print(letter)

print('-' * 20)


# --- 2. Continue Komutu (Pas Geçme) ---

name = 'Yusuf arı'

for letter in name:
    if letter == 'ı':
        continue # 'ı' harfini görünce o turu atlar (yazdırmaz) ve devam eder.
    print(letter)

    x = 0

while x < 5:
    if x == 2:
        break # x değeri 2 olduğu an döngü "kırılır" ve biter.
    print(x)
    x += 1
    x = 0

while x < 5:
    if x == 2:
        break # x değeri 2 olduğu an döngü "kırılır" ve biter.
    print(x)
    x += 1