# Bankamatik Uygulaması

SadıkHesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        print('paranızı alabilirsiniz.')
    else:
        # Görselde şurada 'help' yazılmış, doğrusu 'hesap' olmalıydı:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            # Kullanıcıya soru sorup cevabı değişkene atıyoruz
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')
            
            if ekHesapKullanimi == 'e':
                print('Paranızı alabilirsiniz. (Ek hesap kullanıldı)')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda bakiye yetersiz.")
        else:
            print('Üzgünüz, bakiye yetersiz.')

# Fonksiyonu çağırıyoruz.
paraCek(SadıkHesap, 4000)

