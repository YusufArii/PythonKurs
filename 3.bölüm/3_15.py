
website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# baştaki ve sondaki boşlukları temizler
result1 = ' Hello World '.strip()

# kenarlardaki fazlalıkları (w, c, o, m ve nokta) siler
result2 = 'www.sadikturan.com'.strip('w.com')

# metindeki tüm harfleri küçültür
result3 = course.lower()

# içinde kaç tane 'a' harfi var onu sayar
result4 = website.count('a')

# www ile mi başlıyor, com ile mi bitiyor diye bakar (True/False)
isStarted = website.startswith('www')
isEnded = website.endswith('com')

# içinde .com var mı diye arar, varsa sırasını söyler
result6 = website.find('.com')

#  metindeki karakterlerin hepsi harf mi diye bakar (boşluk varsa false)
result7 = course.isalpha()

# 'Contents' yazısını 50 karakterin ortasına alıp kenarlara yıldız ekler
result8 = 'Contents'.center(50, '*')

# 'course' metnindeki bütün boşlukları bulup yerine tire (-) koyar
result9 = course.replace(' ', '-')

# 'Hello World' metnindeki 'World' kelimesini 'There' ile değiştirir
result10 = 'Hello World'.replace('World', 'There')

# 'course' metnini boşluklardan parçalayıp kelime kelime ayırır (liste yapar)
result11 = course.split(' ')


# Listeyi oluşturuyoruz
arabalar = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

# Kaç tane eleman var?
eleman_sayisi = len(arabalar)

# İlk ve son arabayı bulur
ilk = arabalar[0]
son = arabalar[-1]

# Mazda'yı bulup yerine Toyota yazar
arabalar[3] = 'Toyota'

# Listede Mercedes var mı diye bakar (True/False döner)
var_mi = 'Mercedes' in arabalar

# Sondan ikinci sıradaki ne?
sondan_ikinci = arabalar[-2]

# Baştan 3 tanesini alır
ilk_uc = arabalar[:3]

# Son iki arabayı silip yerlerine yenilerini koyar
arabalar[-2:] = ['Toyota', 'Renault']

# Listenin sonuna iki yeni araba ekler
arabalar = arabalar + ['Audi', 'Nissan']

# Listenin en sonundaki elemanı siler
arabalar.pop() 

# Listeyi tersten yazdırır
tersten = arabalar[::-1]


# 'Cenk' ismini listenin en sonuna ekler
names.append('Cenk') 

# 'Sena'yı listenin en başına ekler
names.insert(0, 'Sena') 

# 'Deniz' ismini listeden siler
names.remove('Deniz')

# 'Deniz' isminin listedeki sırası kaç?
# Not: Normalde 3. sıradaydı. Silme işleminden önceki sırasını bulalım:
deniz_index = names.index('Deniz')

# 'Ali' listenin içinde var mı?
ali_var_mi = 'Ali' in names

# Listenin elemanlarını ters çevirir
names.reverse() 

# Listeyi alfabetik olarak sıralar
names.sort()

# years listesini küçükten büyüğe sıralar
years.sort()

# String'i virgülden bölüp kelime kelime listeye çevirir
str_data = "Chevrolet,Dacia"
araba_listesi = str_data.split(',')

# years dizisinin en büyük ve en küçük elemanı
en_buyuk = max(years)
en_kucuk = min(years)

# years dizisinde kaç tane 1998 var
bin_dokuz_yuz_doksan_sekiz_sayisi = years.count(1998)

# years dizisinin tüm elemanlarını siler
years.clear() 


# 12- Öğrenci bilgilerini liste olarak oluşturuyoruz

ogrenciA = ['Yiğit Bilgi', 2010, [70, 60, 70]]
ogrenciB = ['Sena Turan', 1999, [80, 80, 70]]
ogrenciC = ['Ahmet Turan', 1998, [80, 70, 90]]

# Bütün öğrencileri tek bir ana listede topluyoruz
ogrenciler = [ogrenciA, ogrenciB, ogrenciC]

# 13- Listeyi ekrana yazdırıyoruz
print(ogrenciler)