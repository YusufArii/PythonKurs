website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- Baştaki ve sondaki boşlukları temizler
result1 = ' Hello World '.strip()

# 2- Kenarlardaki w, c, o, m harflerini ve noktaları siler, ortası kalır
result2 = 'www.sadikturan.com'.strip('w.com')

# 3- Bütün harfleri küçültür
result3 = course.lower()

# 4- İçinde kaç tane 'a' harfi var onu sayar
result4 = website.count('a')

# 5- www ile mi başlıyor, com ile mi bitiyor kontrolü
isStarted = website.startswith('www')
isEnded = website.endswith('com')

# 6- İçinde .com var mı diye bakar, varsa sırasını verir
result6 = website.find('.com')

# 7- Hepsi harf mi diye bakar (boşluk varsa kabul etmez)
result7 = course.isalpha()
# Rakam var mı kontrolü
result7_digit = course.isdigit()

# 8- Yazıyı 50 karakterlik yerin tam ortasına koyup sağa sola yıldız ekler
result8 = 'Contents'.center(50, '*')

# 9- Cümledeki bütün boşlukları bulup yerine tire (-) koyar
result9 = course.replace(' ', '-')

# 10- 'World' kelimesini 'There' ile değiştirir
result10 = 'Hello World'.replace('World', 'There')

# 11- Cümleyi boşluklardan parçalayıp kelime kelime ayırır (liste yapar)
result11 = course.split(' ')


print(result1)
print(result2)
print(result3)
print(result4)
print(isStarted, isEnded)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)