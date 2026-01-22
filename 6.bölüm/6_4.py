sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# --- 1. While ile Listeyi Yazdırma ---
# Listenin başından (0. indeks) başlamak için sayac oluşturuyoruz.
i = 0 

# i sayısı, listenin eleman sayısından küçük olduğu sürece döngü döner.
while i < len(sayilar):
    print(sayilar[i])
    i += 1 # Sonsuz döngü olmaması için i'yi 1 artırıyoruz.

print('-' * 20)


# --- 2. Başlangıç ve Bitiş Arasındaki Tek Sayılar ---
baslangic = int(input('Başlangıç değeri: '))
bitis = int(input('Bitiş değeri: '))

i = baslangic

while i < bitis:
    i += 1
    # Eğer sayının 2'ye bölümünden kalan 1 ise tektir.
    if i % 2 == 1:
        print(i)

print('-' * 20)


# --- 3. 100'den 1'e Geriye Doğru Yazdırma ---
i = 100

while i > 0:
    print(i)
    i -= 1 # Geriye saydığımız için azaltıyoruz.

print('-' * 20)


# --- 4. Kullanıcıdan 5 Sayı Alıp Sıralama ---
yeni_liste = [] # Sayıları koyacağımız boş bir kutu
i = 0

while i < 5:
    sayi = int(input('Bir sayı giriniz: '))
    yeni_liste.append(sayi) # Girilen sayıyı listeye ekle
    i += 1

yeni_liste.sort() # Listeyi küçükten büyüğe sıralar
print(yeni_liste)

print('-' * 20)


# --- 5. Ürün Bilgisi (Dictionary) Saklama ve Listeleme ---
urunler = [] # Ürünleri tutacak boş liste

adet = int(input('Kaç ürün eklemek istiyorsunuz?: '))
i = 0

# Kullanıcının istediği adet kadar döngü çalışır
while i < adet:
    ad = input('Ürün adı: ')
    fiyat = input('Ürün fiyatı: ')
    
    # Bilgileri sözlük (dictionary) olarak paketliyoruz
    urun_bilgisi = {'ad': ad, 'fiyat': fiyat}
    
    # Paketi listeye ekliyoruz
    urunler.append(urun_bilgisi)
    
    i += 1

# Kayıt işlemi bitti, şimdi while ile ekrana yazdıralım
a = 0
while a < len(urunler):
    print(f"Ürün: {urunler[a]['ad']} - Fiyat: {urunler[a]['fiyat']}")
    a += 1