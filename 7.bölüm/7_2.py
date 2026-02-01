# 'name' parametresine varsayılan olarak 'user' değerini atadık.
# Eğer isim girilmezse otomatik olarak 'user' kullanacak.
def sayHello(name = 'user'):
    return 'Hello ' + name 
    # 'return' sonucu ekrana yazmaz, sonucu hafızada tutar ve geri gönderir.

msg = sayHello('Çınar') # msg değişkeni 'Hello Çınar' oldu.
msg = sayHello('Ada')   # msg değişkeni güncellendi ve 'Hello Ada' oldu.

print(msg) # En son değeri ekrana yazdırır.


# Toplama işlemi yapan basit bir fonksiyon örneği
def total(num1, num2):
    return num1 + num2
result = total(10, 20) # 10 + 20 = 30 olur, hafızaya alınır.
result = total(15, 20) # 15 + 20 = 35 olur, önceki değerin ÜZERİNE yazılır.

print(result) # En son hesaplanan değer ekrana yazılır.
def yasHesapla(dogumYili):
    return 2026 - dogumYili 
    # Not: Burada şimdiki yılı (2019) elle yazdık.

ageCinar = yasHesapla(2017) 
ageAda = yasHesapla(2010)   
ageSena = yasHesapla(1999)  

print(ageCinar, ageAda, ageSena)

# 2. Emeklilik hesaplayan ana fonksiyonumuz
def EmekliligeKacYilKaldi(dogumYili, isim):
    
    # Yukarıdaki fonksiyonu çağırıp yaşı öğreniyoruz
    yas = yasHesapla(dogumYili)
    
    # Emeklilik yaşı 65 olarak kabul edilmiş
    emeklilik = 65 - yas

    # Sonucu kontrol ediyoruz
    if emeklilik > 0:
        print(f'{isim}, emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print(f'{isim}, zaten emekli oldunuz.')

# --- Test Edelim ---
EmekliligeKacYilKaldi(1983, 'Ali')
EmekliligeKacYilKaldi(1950, 'Ahmet')