# --- 12. While Döngüsü (1-100'e kadar yazdırma) ---
# Başlangıç değeri veriyoruz
x = 0

# x, 100'den küçük olduğu sürece döngü çalışır
while x < 100:
    print(x)
    x = x + 1 # x'i her seferinde 1 arttırıyoruz (yoksa sonsuz döngü olur)

print('bitti...')
print('-' * 20)


# --- 13. While Döngüsü (Boş Bırakılamayan Alan) ---
name = '' # Boş string Python'da "False" (yanlış) kabul edilir.

# "name" değişkeni boş olduğu sürece (not name) sormaya devam et
while not name:
    name = input('isminizi giriniz: ')

# Kullanıcı bir şey yazıp enter'a bastığında döngü biter ve burası çalışır
print(f'Merhaba, {name}')