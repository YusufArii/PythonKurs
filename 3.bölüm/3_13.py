# 1- Listeyi oluşturuyoruz
arabalar = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

# 2- Listede kaç tane araba var sayar
eleman_sayisi = len(arabalar)

# 3- İlk ve son arabayı bulur
ilk = arabalar[0]
son = arabalar[-1]

# 4- Mazda'yı bulup yerine Toyota yazar

arabalar[3] = 'Toyota' 

# 5- Listede Mercedes var mı diye bakar (True/False döner)
var_mi = 'Mercedes' in arabalar

# 6- Sondan ikinci sıradaki arabayı verir
sondan_ikinci = arabalar[-2]

# 7- Listenin başından 3 tanesini alır
ilk_uc = arabalar[:3]

# 8- Son iki arabayı silip yerlerine yenilerini koyar

arabalar[-2:] = ['Toyota', 'Renault']

# 9- Listenin sonuna iki yeni araba ekler
arabalar = arabalar + ['Audi', 'Nissan']

# 10- Listenin en sonundaki elemanı siler
arabalar.pop()

# 11- Listeyi tersten yazdırır
tersten = arabalar[::-1]

# 12- Öğrenci bilgilerini liste olarak oluşturuyoruz
studentA = ['Yiğit Bilgi', 2010, [70, 60, 70]]
studentB = ['Sena Turan', 1999, [80, 80, 70]]
studentC = ['Ahmet Turan', 1998, [80, 70, 90]]
students = [studentA, studentB, studentC]


print(f"Toplam Eleman: {eleman_sayisi}")
print(f"İlk: {ilk}, Son: {son}")
print(f"Mercedes Var mı?: {var_mi}")
print(f"Sondan İkinci: {sondan_ikinci}")
print(f"Listenin Son Hali: {arabalar}")
print(f"Tersten: {tersten}")
print(students)
print("Birinci Öğrenci:", students[0])
print("İkinci Öğrenci:", students[1])
print("Üçüncü Öğrenci:", students[2])