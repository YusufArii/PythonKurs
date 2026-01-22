# --- BÖLÜM 1: 0-100 Arası Kontrol ---
# Kullanıcıdan sayı alıp float'a çeviriyoruz
girilen_sayi = float(input('1. Sayı (0-100 kontrolü): '))
# Sayı 0'dan büyük VE 100'den küçük/eşit mi?
sonuc = (girilen_sayi > 0) and (girilen_sayi <= 100)
print(f'Sayı 0-100 arasında mı?: {sonuc}')
print('-' * 30) # Araya çizgi çektik


# --- BÖLÜM 2: Pozitif ve Çift Sayı Kontrolü ---
tam_sayi = int(input('2. Sayı (Pozitif/Çift kontrolü): '))
# Sayı pozitif mi VE 2'ye bölümünden kalan 0 mı?
cift_pozitif = (tam_sayi > 0) and (tam_sayi % 2 == 0)
print(f'Sayı pozitif ve çift mi?: {cift_pozitif}')
print('-' * 30)


# --- BÖLÜM 3: Giriş (Login) Kontrolü ---
gercek_mail = 'deneme@gmail.com'
gercek_sifre = '123'

kullanici_mail = input('Mail giriniz: ')
kullanici_sifre = input('Şifre giriniz: ')

# Hem mail hem şifre doğru mu?
giris_basarili = (kullanici_mail == gercek_mail) and (kullanici_sifre == gercek_sifre)
print(f'Giriş başarılı mı?: {giris_basarili}')
print('-' * 30)


# --- BÖLÜM 4: Büyüklük Karşılaştırma ---
s1 = int(input('a sayısı: '))
s2 = int(input('b sayısı: '))
s3 = int(input('c sayısı: '))

# Her sayının en büyük olma durumunu tek tek kontrol ediyoruz
a_buyuk = (s1 > s2) and (s1 > s3)
b_buyuk = (s2 > s1) and (s2 > s3)
c_buyuk = (s3 > s1) and (s3 > s2)

print(f'a en büyük mü?: {a_buyuk}')
print(f'b en büyük mü?: {b_buyuk}')
print(f'c en büyük mü?: {c_buyuk}')
print('-' * 30)


# --- BÖLÜM 5: Not Hesaplama ---
v1 = float(input('Vize 1: '))
v2 = float(input('Vize 2: '))
fnl = float(input('Final: '))

# Ortalama hesabı: Vizelerin ortalamasının %60'ı + Finalin %40'ı
ort = ((v1 + v2) / 2) * 0.6 + (fnl * 0.4)

# Geçme şartı: (Ortalama 50 üstü ve final 50 üstü) VEYA (Final 70 üstü)
gecme = (ort >= 50 and fnl >= 50) or (fnl >= 70)
print(f'Ortalama: {ort} - Geçti mi?: {gecme}')
print('-' * 30)


# --- BÖLÜM 6: Kilo İndeksi (VKİ) Hesaplama ---
ad = input('Adınız: ')
kilo = float(input('Kilo: '))
boy = float(input('Boy (m): '))

vki = kilo / (boy ** 2)

# Hangi aralıkta olduğunu kontrol et
zayif = (vki >= 0) and (vki <= 18.4)
normal = (vki > 18.4) and (vki <= 24.9)
kilolu = (vki > 24.9) and (vki <= 29.9)
obez = (vki > 29.9) and (vki <= 34.9)

print(f'{ad} indeksin: {vki}')
print(f'Zayıf mı?: {zayif}')
print(f'Normal mi?: {normal}')
print(f'Kilolu mu?: {kilolu}')
print(f'Obez mi?: {obez}')
print('-' * 30)


# --- BÖLÜM 7: For Döngüsü (Sayılar) ---
sayilar = [1, 2, 3, 4, 5]

# Listenin içindeki her bir eleman için döngü çalışır
for sayi in sayilar:
    print('Hello') # 5 eleman olduğu için 5 kere Hello yazar
print('-' * 30)


# --- BÖLÜM 8: For Döngüsü (İsimler) ---
isimler = ['çınar', 'sadık', 'sena']

for isim in isimler:
    print(f'My name is {isim}') # Sırayla isimleri yazar
print('-' * 30)


# --- BÖLÜM 9: For Döngüsü (Tuple Listesi) ---
# Liste içinde ikili gruplar (demetler) var
sayi_ciftleri = [(1,2), (1,3), (3,5), (5,7)]

# Her turda a ve b değişkenlerine sıradaki ikiliyi atar
for a, b in sayi_ciftleri:
    print(a, b)
print('-' * 30)


# --- BÖLÜM 10: For Döngüsü (Sözlük - Dictionary) ---
sozluk = {'k1': 1, 'k2': 2, 'k3': 3}

# Sözlüklerde döngü varsayılan olarak anahtarları (keys) getirir
for eleman in sozluk:
    print(eleman) # k1, k2, k3 yazar