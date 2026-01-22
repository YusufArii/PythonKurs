# range(başlangıç, bitiş, artış_miktarı)
# Mantık: 50'den başla, 100'e kadar git (100 dahil değil), 20'şer 20'şer artır.

# 1. Döngü ile yazdırma
for item in range(50, 100, 20):
    print(item)

# 2. Liste olarak yazdırma
print(list(range(5, 100, 10)))

# enumerate
#
#index = 0
#greeting = 'Hello There'

#for letter in greeting:
    # Hem sıra numarasını (index) hem de o sıradaki harfi yazdırıyoruz
   # print(f'index: {index} letter: {greeting[index]}')
 #   index += 1
#
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

# zip() iki listeyi aynı sıradaki elemanlarla birleştirir.
print(list(zip(list1, list2)))