
# String, Integer gibi tiplerde verinin kendisi kopyalanır.
def changeName(n):
    n = 'ada' # Burada sadece fonksiyon içindeki 'n' değişir.

name = 'yiğit'

changeName(name)
print(name) 


# --- BÖLÜM 2: Referans Tip (Reference Types) ---
# Listeler hafızadaki adresi (pointer gibi) taşır.
def change(n):
    n[0] = 'istanbul' # Listenin orjinal adresi üzerindeki veriyi değiştirir.

sehirler = ['ankara', 'izmir']

change(sehirler)
print(sehirler) # (Görselin sonunda kesilmiş ama mantıken buraya print gelir)

# Parametre isminin başına '*' koyduğumuzda, gelen tüm değerler bir "Tuple" (demet) içinde toplanır.
def add(*params):
    print(params[0]) # Gelen listenin ilk elemanını ekrana yazar
    print(params[2])
    # sum() fonksiyonu, kendisine verilen listenin/tuple'ın içindeki sayıları toplar.
    return sum(params)

# 1. Kullanım: 2 tane sayı gönderiyoruz
print(add(10, 20,50))

# 2. Kullanım: 3 tane sayı gönderiyoruz
print(add(10, 20, 30))

# 3. Kullanım: İstediğimiz kadar sayı gönderebiliyoruz
print(add(10, 20, 30, 50, 60, 10, 20))

# Parametrenin başına iki yıldız (**) koyduğumuzda,
# Python gelen verileri bir Sözlük (Dictionary) içine atar.
def displayUser(**args):
    # args.items() fonksiyonu sözlüğün içindeki 'anahtar' ve 'değer' ikililerini tek tek gezmemizi sağlar.
    for key, value in args.items():
        print('{} is {}'.format(key, value))
    
    print('---') # Okuması kolay olsun diye ayraç ekledim

# 1. Kullanım: 3 bilgi gönderiyoruz
displayUser(name='Çınar', age=2, city='istanbul')

# 2. Kullanım: 4 bilgi gönderiyoruz (Ekstra 'phone' bilgisi var)
displayUser(name='Ada', age=12, city='kocaeli', phone='123132')

# 3. Kullanım: Yine farklı bilgiler
displayUser(name='Yiğit', age=14, city='ankara', phone='123132')