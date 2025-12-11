#öğrendiklerimizle örnek yaptık
website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

print("1-", len(course))
print("2-", website[7:10])
print("3-", website[-3:])
print("4-", course[:15], course[-15:])
print("5-", course[::-1])

name = "Bora"
surname = "Yılmaz"
age = 32
job = "mühendis"

print("6-", f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")
print("7-", "Hello world".replace("w", "W"))
print("8-", "abc" * 3)