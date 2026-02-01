class Yazilimci:
    # Yapıcı Metot (__init__)
    # Nesne oluşurken verileri (attributes) set eder.
    def __init__(self, ad, soyad, maas, diller):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.diller = diller # Liste olarak alacağız
    
    # --- METOTLAR (YETENEKLER) ---

    # 1. Bilgi Gösteren Metot
    def bilgileriGoster(self):
        print(f"""
        Yazılımcı Bilgileri:
        Ad: {self.ad}
        Soyad: {self.soyad}
        Maaş: {self.maas} TL
        Bildiği Diller: {self.diller}
        """)

    # 2. Yeni Dil Öğrenen Metot
    def dilOgren(self, yeni_dil):
        print(f"{self.ad}, {yeni_dil} dilini öğreniyor...")
        self.diller.append(yeni_dil)
    
    # 3. Zam İsteyen Metot
    def zamYap(self, zam_miktari):
        print(f"{self.ad} zam aldı.")
        self.maas += zam_miktari

# --- NESNELERİ OLUŞTURALIM VE KULLANALIM ---

# Bir yazılımcı (nesne) üretiyoruz
yazilimci1 = Yazilimci("Ahmet", "YILMAZ", 30000, ["Python", "C++"])

# Metotları Çağıralım
yazilimci1.bilgileriGoster() 


yazilimci1.dilOgren("Java") 


yazilimci1.zamYap(5000)

# Son durum
yazilimci1.bilgileriGoster()