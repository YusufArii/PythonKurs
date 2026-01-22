a, b, c = 2, 5, 10

degerler = 1, 5, 10, 6

# Kullanıcıdan aldığınız 2 sayının çarpımı ile a, b, c toplamının farkı nedir?

giris1 = input('sayi girin: ')
giris2 = input('ikinci sayi giriniz: ')

sonuc = int(giris1) * int(giris2) - (a + b + c)


# b'nin a'ya kalansız bölümünü hesaplayınız

sonuc = b // a


# a + b + c'nin mod 3'ü nedir?

sonuc = (a + b + c) % 3


# b'nin a kuvvetini hesaplayınız

sonuc = b ** a


# a, *b, c = degerler işlemine göre c'nin küpü kaçtır?

a, *b, c = degerler
sonuc = c ** 3


# a, *b, c = degerler işlemine göre b'nin (listenin) değerleri toplamı kaçtır?

sonuc = b[0] + b[1]

print(sonuc)