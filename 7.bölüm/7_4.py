def yazdir(kelime, adet):
    # Belirtilen adet kadar döngü kuruyoruz
    for i in range(adet):
        print(kelime)

# Test edelim
yazdir('Merhaba', 3)

# *args kullanarak sınırsız parametre alıyoruz
def listeyeCevir(*args):
    liste = []
    # Gelen her parametreyi listeye ekliyoruz
    for arg in args:
        liste.append(arg)
    
    return liste

# Test edelim
sonuc = listeyeCevir(10, 20, 30, 'Merhaba', 'Python')
print(sonuc)

def asallariBul(sayi1, sayi2):
    # Sayı 1'den Sayı 2'ye kadar dönüyoruz
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1: # 1'den büyük sayılara bakılır
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break # Eğer bölünürse asal değildir, döngüyü kır
            else:
                # Hiçbir şeye bölünmediyse asaldır
                print(sayi)

# Test edelim (10 ile 30 arasındakiler)
asallariBul(10, 30)

def tamBolenleriBul(sayi):
    tamBolenler = []
    
    # 2'den başlayıp sayının kendisine kadar deniyoruz
    for i in range(2, sayi+1):
        if (sayi % i == 0):
            tamBolenler.append(i) # Tam bölüyorsa listeye ekle
            
    return tamBolenler

# Test edelim
print(tamBolenleriBul(20)) 
# Çıktı: [2, 4, 5, 10, 20] olur

