class Araba:
    # __init__: Constructor (Yapıcı Metot). 
    # Nesne ilk oluşturulduğunda otomatik çalışır ve ayarları yapar.
    def __init__(self, marka, model, renk):
        self.marka = marka  # Gelen bilgiyi nesnenin hafızasına (self) kaydet
        self.model = model
        self.renk = renk
        self.hiz = 0        # Her araba 0 hızla başlar (Varsayılan değer)

    # Bir Metot (Yetenek) tanımlayalım
    def calistir(self):
        print(f"{self.marka} {self.model} çalıştırıldı.")

    def hizlan(self):
        self.hiz += 10
        print(f"Hız arttı: {self.hiz} km/s")

# --- KULLANIM (Nesne Üretme) ---

# Kalıptan 1. arabayı üretiyoruz
araba1 = Araba('BMW', 'i5', 'Kırmızı')

# Kalıptan 2. arabayı üretiyoruz
araba2 = Araba('Mercedes', 'E200', 'Siyah')

# Arabaların özelliklerini kullanalım
araba1.calistir()  #BMW i5 çalıştırıldı.
araba1.hizlan()    # Hız arttı: 10 km/s

print(araba2.renk) # Siyah