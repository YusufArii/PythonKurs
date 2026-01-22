# 1. Sayıyı alıyoruz
sayi = int(input('Bir sayı giriniz: '))

asal_mi = True
bolen_sayi = 0  # Suçluyu (böleni) yakalayıp buraya kaydedeceğiz

# 2. 1 sayısı için özel durum
if sayi == 1:
    asal_mi = False

# 3. Kontrol döngüsü
for i in range(2, sayi):
    if (sayi % i == 0):
        asal_mi = False
        bolen_sayi = i # İşte sayıyı bölen suçlu bu! Hafızaya atıyoruz.
        break 

# 4. Sonucu yazdırma kısmı
if asal_mi:
    print(f'{sayi} sayısı ASALDIR.')
else:
    # Eğer bir bölen bulunduysa (yani 0'dan büyükse) sebebini de yazdır
    if bolen_sayi > 0:
        print(f'{sayi} sayısı ASAL DEĞİLDİR. Çünkü {bolen_sayi} sayısına tam bölünüyor.')
    else:
        # Sayı 1 ise böleni yoktur ama asal da değildir
        print(f'{sayi} sayısı ASAL DEĞİLDİR.')