# 1. Kullanıcıdan bir sayı istiyoruz ve matematik işlemi yapabilmek için 'float'a (kesirli sayıya) çeviriyoruz.
sayi = float(input('Bir sayı giriniz: '))

# 2. Sayının 0 ile 100 arasında olup olmadığını kontrol ediyoruz.
# Mantık: Sayı 0'dan büyük OLMALI "ve" (and) sayı 100'den küçük veya eşit OLMALI.
durum = (sayi > 0) and (sayi <= 100)

# 3. Çıkan sonucu (True veya False) ekrana yazdırıyoruz.
print(f'Sayı 0-100 arasında mı?: {durum}')
# 1. Kullanıcıdan bir sayı istiyoruz ve matematiksel işlem için tamsayıya (int) çeviriyoruz.
girilen_deger = int(input('Bir sayı giriniz: '))

# 2. İki şartın AYNI ANDA sağlanıp sağlanmadığını kontrol ediyoruz:
#    Şart A: Sayı 0'dan büyük mü? (Pozitif mi?)
#    Şart B: Sayının 2'ye bölümünden kalan 0 mı? (Çift mi?)
cevap = (girilen_deger > 0) and (girilen_deger % 2 == 0)

# 3. Sonucu (True veya False olarak) ekrana yazdırıyoruz.
print(f'Girilen sayı pozitif ve çift mi?: {cevap}')

# 1. Öncelikle sistemde kayıtlı olan DOĞRU bilgileri tanımlıyoruz.
kayitli_email = 'deneme@gmail.com'
kayitli_sifre = '123456'

# 2. Kullanıcıdan kendi bilgilerini girmesini istiyoruz.
girilen_email = input('E-posta adresinizi giriniz: ')
girilen_sifre = input('Şifrenizi giriniz: ')

# 3. Kullanıcının girdiği bilgiler ile kayıtlı bilgileri karşılaştırıyoruz.
#    Mantık: (Email eşleşiyor mu?) VE (Şifre eşleşiyor mu?)
#    Her ikisi de doğruysa sonuç True, en az biri yanlışsa False çıkar.
giris_durumu = (girilen_email == kayitli_email) and (girilen_sifre == kayitli_sifre)

# 4. Sonucu ekrana yazdırıyoruz.
print(f'Giriş başarılı mı?: {giris_durumu}')

# 1. Kullanıcıdan kıyaslamak için 3 farklı sayı istiyoruz.
s1 = int(input('Birinci sayı: '))
s2 = int(input('İkinci sayı: '))
s3 = int(input('Üçüncü sayı: '))

# 2. Birinci sayının (s1) EN BÜYÜK olma durumu:
#    Mantık: s1, s2'den büyük olmalı VE s1, s3'ten büyük olmalı.
sonuc_1 = (s1 > s2) and (s1 > s3)
print(f'Birinci sayı en büyük mü?: {sonuc_1}')

# 3. İkinci sayının (s2) EN BÜYÜK olma durumu:
#    Mantık: s2 hem s1'den hem de s3'ten büyük mü?
sonuc_2 = (s2 > s1) and (s2 > s3)
print(f'İkinci sayı en büyük mü?: {sonuc_2}')

# 4. Üçüncü sayının (s3) EN BÜYÜK olma durumu:
sonuc_3 = (s3 > s1) and (s3 > s2)
print(f'Üçüncü sayı en büyük mü?: {sonuc_3}')

# 1. Kullanıcıdan notları ondalıklı sayı (float) olabilecek şekilde istiyoruz.
vize1 = float(input('1. Vize notunuz: '))
vize2 = float(input('2. Vize notunuz: '))
final_notu = float(input('Final notunuz: '))

# 2. Ortalama Hesaplama: 
#    Önce iki vizenin ortalamasını alıp %60'ını (0.6) buluyoruz.
#    Sonra finalin %40'ını (0.4) bulup topluyoruz.
#    Parantez kullanımı işlem önceliği için çok önemlidir!
ders_ortalamasi = ((vize1 + vize2) / 2) * 0.6 + (final_notu * 0.4)

# 3. Geçme Durumu Kontrolü (İki ihtimal var):
#    İhtimal A: Ortalama 50'yi geçmeli VE Final en az 50 olmalı.
#    İhtimal B: Final 70 veya üstü ise ortalamaya bakmaksızın geçer.
#    Mantık: (Şart A) VEYA (Şart B)
gecme_durumu = (ders_ortalamasi >= 50 and final_notu >= 50) or (final_notu >= 70)

# 4. Sonucu ekrana yazdırıyoruz.
print(f'Ortalama: {ders_ortalamasi} - Dersten geçme durumu: {gecme_durumu}')

# 1. Kullanıcıdan gerekli bilgileri alıyoruz.
#    Boyu "metre" cinsinden (örn: 1.78) ondalıklı (float) olarak istiyoruz.
isim = input('Adınız: ')
kilo = float(input('Kilonuz (kg): '))
boy = float(input('Boyunuz (m): '))

# 2. Vücut Kitle İndeksi Hesaplama Formülü: Kilo / (Boy'un Karesi)
vki_indeksi = kilo / (boy ** 2)

# 3. Hesaplanan değerin hangi aralıkta olduğunu kontrol ediyoruz.
#    Her bir kategori için "Alt Sınır" VE "Üst Sınır" şartı koyuyoruz.

durum_zayif = (vki_indeksi >= 0) and (vki_indeksi <= 18.4)
durum_normal = (vki_indeksi > 18.4) and (vki_indeksi <= 24.9)
durum_kilolu = (vki_indeksi > 24.9) and (vki_indeksi <= 29.9)
durum_obez = (vki_indeksi > 29.9) and (vki_indeksi <= 34.9)

# 4. Sonuçları ekrana yazdırıyoruz.
#    Program çalıştığında sadece kullanıcının girdiği gruba ait satırda "True" yazar.

print(f'{isim} - Kilo İndeksiniz: {vki_indeksi} -> Zayıf mı?: {durum_zayif}')
print(f'{isim} - Kilo İndeksiniz: {vki_indeksi} -> Normal mi?: {durum_normal}')
print(f'{isim} - Kilo İndeksiniz: {vki_indeksi} -> Fazla Kilolu mu?: {durum_kilolu}')
print(f'{isim} - Kilo İndeksiniz: {vki_indeksi} -> Obez mi?: {durum_obez}')

