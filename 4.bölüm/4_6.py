
sayi = int(input('sayi girinşz'))

cevap = (0 < sayi) and (sayi< 100) # bir ise doğru 

cevap = (sayi >0) and (sayi % 2 == 0) # bir ise doğru

emai = "mail"
parola = "121"
ema = input("mail giriniz")
parol = input("parolayı giriniz")
cevap  = (emai == ema) and (parola == parol)

x,y,z = 1,2,3 #girilen sayılar

enbuyuksayiX = (x>y) and (x>z) 
enbuyuksayiY = (y>x) and (y>z) 
enbuyuksayiZz = (z>x) and (z>y) 


vize,final = 50,100 #girilen sayilar

orlama = ((vize*0.6)+(final*0.4))
cevap = ((orlama >50) and (final > 50)) or (final > 70)

ad,kilo,boy ="Admin", 100, 190 #girlen sayilar
formul = kilo/boy^2

zayif = (formul>= 0) and (formul>=18.4)
orta = (formul>= 18.5) and (formul>=24.9)
kilolu = (formul>= 25) and (formul>=29.9),
Obez = (formul>= 30) and (formul>=34.9)