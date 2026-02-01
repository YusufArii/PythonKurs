
list = [1, 2, 3]

list.append(4) # Listeye 4 ekler. (Liste [1, 2, 3, 4] olur)
list.pop()     # Listenin son elemanını (4'ü) siler.

print(type(list)) # Veri tipini yazar: <class 'list'>
print(list)       # Listeyi yazar: [1, 2, 3]


# --- 2. Bölüm: String (Metin) Metotları ---
myString = 'Hello'

# upper() metodu, metindeki tüm harfleri BÜYÜK harfe çevirir.
print(myString.upper())