#girilen 2 sayıdan hangisi büyüktür

a = int(input('a: '))
b = int(input('b:'))

cevap = (a > b)

print(f'a:{a} b:{b} büyüktür: {cevap}')

#kullanıcıdan 2 vize %60 ve final %40 notunu alığ ortalma hesaplayınız
#eğer ortlama 50 ve üstündeyse geçti değise kaldı

vize1 = float(input('1. vize : '))
vize2 = float(input('2. vize:'))
final = float(input('final : '))

ortalma = ((vize1 + vize2) * 0.6) + (final * 0.4)

print(f'not ortalamsız : {ortalma} ve dersten geçme durumunuz: {ortalma>=50}')

#girilen  bir sayını tek mi çift mi olduğunu yazdırın

sayi = int(input('sayi:'))

tekcift = (sayi% 2 == 0)

print(f'girilen sayi cift  {tekcift}')

sayi = int(input('sayi:'))
poziitfmidir = (sayi> 0)

print(f'girilen sayi prizif olma durumu :: {poziitfmidir}')

email = 'emaşkada'

sifre = 'abafaf'

girrilenmail = input('mailiniz: ')
girilensifre = input('parola: ')

ismial = (email == girrilenmail)
issifre = (sifre == girilensifre)

print(f'email bilgisini doğruluk durumu : {ismial} \ngirilen sifre doğruluk durumu {issifre} ')