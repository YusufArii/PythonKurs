# Tek satırda birden fazla değişken tanımlama
a, b, c = 5, 10, 20 

# Değerleri Takas Etme (Swapping)
a, b = b, a  # a'nın değeri b'ye, b'nin değeri a'ya geçer. (Geçici değişken kullanmaya gerek kalmaz)


a += 5  # a = a + 5 işleminin kısa yoludur. 
# Not: -= (çıkar), *= (çarp), /= (böl), //= (tam böl), %= (mod al), **= (üs al) şeklinde de kullanılır.

# Tuple (Demet) Paketleme
veriler = 1, 2, 3  # Parantez koymasan bile virgüller sayesinde bu bir 'tuple' olur.

# Unpacking (Paket Açma / Değerleri Dağıtma)
k, l, m = veriler # Tuple içindeki elemanlar sırasıyla k, l ve m'ye atanır.

# Genişletilmiş Paket Açma (Extended Unpacking) Notu:
# Eğer m'nin başına yıldız (*m) koysaydık ve liste daha uzun olsaydı;
# k ve l ilk iki değeri alır, geriye kalan tüm değerler m içinde bir liste olarak tutulurdu.