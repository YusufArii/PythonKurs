message= 'tony stark was able to build this in a cave with a box of scraps'

#message= message.upper() #tüm karakterleri büyük harf yapar
#message= message.lower() #tüm karakterleri küçük harf yapar
message= message.title() #her kelimenin ilk harfini büyük yapar
print(message)
#message= message.capitalize() sadece ilk harfi büyük yapar
# 
# message= message.strip() baştaki boşluk harfini siler
#message= message.split() kelimeleri ayırdı
#message= message.join(message) ayrılmış kelimeleri araya boşluk koyarak birleştirir.
index= message.find('Tony')
isFound= message.startswith('T')
print(isFound)
isEnds=message.endswith('s')
print(isEnds)
#message=message.replace('ç','c') karakterleri değiştirdik
#message = message.center(100) 100 karakterlik alana ortalar
# 
# 