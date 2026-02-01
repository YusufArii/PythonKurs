# def square(num): return num ** 2  

numbers = [1, 3, 5, 9]

# LAMBDA KULLANIMI:
# "lambda num: num ** 2" demek; "bana bir numara ver, sana karesini geri vereyim" diyen isimsiz bir fonksiyondur.
# map fonksiyonu bu isimsiz fonksiyonu alır ve listeye uygular.
result = list(map(lambda num: num ** 2, numbers))

# Döngü ile yazdırma kısmı (Not: Görselde burada hala 'square' yazıyor ama doğrusu lambda olmalıydı)
for item in map(lambda num: num ** 2, numbers):
    print(item)

print(result)

# Çift sayıları kontrol eden fonksiyon
# Eğer sayı 2'ye tam bölünüyorsa (kalan 0 ise) True döndürür.
def check_even(num): return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6] # (Örnek anlaşılsın diye listeyi güncelledim)

# FILTER KULLANIMI:
# numbers listesindeki her sayıyı check_even fonksiyonuna gönderir.
# Sadece "True" cevabı alanları  yeni listeye ekler.
result = list(filter(check_even, numbers))

print(result)