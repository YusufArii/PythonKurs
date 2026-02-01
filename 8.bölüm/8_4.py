# 1. PARENT CLASS (Ebeveyn Sınıf)
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print("Person nesnesi oluşturuldu.")

    def intro(self):
        print(f"Ben {self.name} {self.surname}")

# 2. CHILD CLASS (Çocuk Sınıf)
# Parantez içine miras alacağı sınıfı yazıyoruz: (Person)
class Student(Person):
    def __init__(self, name, surname, number):
        # super().__init__: Üst sınıfın (Person) kurucusunu çalıştırır.
        # name ve surname'i Person'a gönderir, number'ı kendisi alır.
        super().__init__(name, surname)
        self.number = number
        print("Student nesnesi oluşturuldu.")

    # OVERRIDING
    # Person'daki intro metodunu değiştiriyoruz.
    def intro(self):
        print(f"Ben {self.name}, Öğrenci Numaram: {self.number}")



p1 = Person("Ahmet", "Yılmaz")
p1.intro() 


print("-" * 10)

s1 = Student("Ali", "Kaya", 105)
s1.intro() 
