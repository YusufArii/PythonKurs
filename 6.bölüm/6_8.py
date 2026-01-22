import random

sayi = random.randint(1, 100)
hak = 5 # Toplam hak sayısını 5 olarak sabitledik
sayac = 0 # Kaçıncı denemede olduğunu saymak için

while hak > 0:
    hak -= 1 # Her tahminde bir hak düşüyoruz
    sayac += 1
    tahmin = int(input('Tahmininiz: '))

    if sayi == tahmin:
        # Puan Hesabı: Her yanlış tahmin 20 puan götürür (100 / 5 = 20).
        # (sayac - 1) formülü sayesinde ilk tahminde bilirsen puan düşmez.
        puan = 100 - (20 * (sayac - 1))
        print(f'Tebrikler! {sayac}. defada bildiniz. Puanınız: {puan}')
        break
    elif sayi > tahmin:
        print('Yukarı')
    else:
        print('Aşağı')

    # Hak 0 olduğunda oyun biter ve puan 0 olarak ekrana yazılır
    if hak == 0:
        print(f'Hakkınız bitti. Tutulan sayı: {sayi}. Puanınız: 0')