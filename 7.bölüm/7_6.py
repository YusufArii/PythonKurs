# global scope
x = 'global x'

def function():
    # local scope
    # x = 'local x'
    print(x)

function()
print(x)

#############################
# global
name = 'Çınar'

def changeName(new_name):
    # local
    # Burada 'name' adında YENİ bir yerel değişken oluşur.
    # Dışarıdaki 'name' değişkeni ile sadece isim benzerliği vardır, bağları yoktur.
    name = new_name 
    print(name)

changeName('Ada')
print(name)

#############################
name = 'global string'

def greeting():
    name = 'Çınar'

    def hello():
        # Bu fonksiyon çalıştığında 'name' değişkenini arar.
        # Önce kendi içine bakar -> Yok.
        # Sonra kapsayıcı (enclosing) fonksiyona bakar -> Evet, orada 'Çınar' var.
        print('hello ' + name)

    hello()

greeting()

x = 50

def test():
    # 'global' komutu ile Python'a diyoruz ki:
    # "İçeride yeni bir 'x' üretme, en tepedeki 'x'i kullan ve onu değiştir."
    global x 
    
    print(f'x : {x}') # Globaldeki değeri okur (50)

    x = 100 # Globaldeki asıl kutunun içini değiştirir
    print(f'changed x to {x}')

# Fonksiyonu çağırıyoruz
test()

# Fonksiyon bittikten sonra dışarıdaki x'i kontrol ediyoruz
print(x)

