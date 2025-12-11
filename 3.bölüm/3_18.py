ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    },
}

# Kullanıcıdan yeni eklenecek öğrencinin bilgilerini istiyoruz
ogr_no = input("Öğrenci No giriniz: ")
ogr_ad = input("Öğrenci Adı: ")
ogr_soyad = input("Öğrenci Soyadı: ")
ogr_tel = input("Öğrenci Telefon: ")

# Aldığımız bu bilgileri sözlüğe yeni bir kayıt olarak ekliyoruz

ogrenciler[ogr_no] = {
    'ad': ogr_ad,
    'soyad': ogr_soyad,
    'telefon': ogr_tel
}



# Bilgisini görmek istediğimiz numarayı soruyoruz
aranan_no = input("Aramak istediğiniz öğrenci no: ")

# Girilen numarayı sözlükte bulup bilgilerini alıyoruz
kayit = ogrenciler[aranan_no]

# Bilgileri güzel bir şekilde ekrana yazdırıyoruz
print(f"Aradığınız Öğrenci: {kayit['ad']} {kayit['soyad']}")
print(f"Telefon Numarası: {kayit['telefon']}")