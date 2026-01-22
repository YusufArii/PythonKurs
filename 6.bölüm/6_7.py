# YÖNTEM 1: Klasik Yol (Döngü ve append kullanarak)
numbers = [] # Önce boş bir liste oluştururuz
for x in range(10):
    numbers.append(x) # Her sayıyı tek tek listenin içine atarız

print(numbers)


# YÖNTEM 2: Pratik Yol (List Comprehension)
# Yukarıdaki 3 satırlık işlemin aynısını tek satırda yapar.
# Mantığı: "range(10) içindeki her x değeri için, listeye bir x ekle"
numbers = [x for x in range(10)]

print(numbers)
# YÖNTEM 1: Klasik Döngü ile Yazdırma
# 0'dan 10'a kadar olan sayıların karesini tek tek ekrana yazar.
for x in range(10):
    print(x**2)


# YÖNTEM 2: List Comprehension (Liste Üreteci)
# 0'dan 10'a kadar olan sayıların karelerinden oluşan bir liste yaratır.
numbers = [x**2 for x in range(10)]

print(numbers)
# YÖNTEM 1: Klasik Döngü (Long Way)
myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter) # Her harfi listeye ekler

print(myList)


# YÖNTEM 2: List Comprehension (Kısa Yol)
# String içindeki her harfi alır ve tek satırda listeye çevirir.
#myList = [letter for letter in myString]

#print(myList)
# --- BÖLÜM 1: List Comprehension içinde If-Else ---
# 1'den 10'a kadar sayıları kontrol et.
# Eğer sayı çiftse (x%2==0) kendisini al, değilse yerine 'TEK' yaz.

results = [x if x%2==0 else 'TEK' for x in range(1, 10)]
print(results)


# --- BÖLÜM 2: İç İçe Döngüler (Nested Loops) ---
result = []

for x in range(3):      # x: 0, 1, 2
    for y in range(3):  # y: 0, 1, 2
        result.append((x,y)) # x ve y ikilisini listeye ekle

print(result)