print("Lütfen yapmak istediğiniz işlemi seçiniz.")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminizi Yapınız : (1/2/3/4):")

sayi1 = float(input("İlk sayıyı giriniz : "))
sayi2 = float(input("İkinci sayıyı giriniz : "))

def topla(x,y):
    return x+y

def cikar(x,y):
    return x-y
    
def carp(x,y):
    return x*y
    
def bolme(x,y):
    return x/y
    
if secim == "1":
    print("Toplama işlemi sonucu : ",topla(sayi1,sayi2))
elif secim == "2":
    print("Çıkarma işlemi sonucu : ",cikar(sayi1,sayi2))
elif secim == "3":
    print("Çarpma işlemi sonucu : ",carp(sayi1,sayi2))
elif secim == "4":
    if sayi2 == 0 :
        print("Bir sayı sıfıra bölünmez")
    else:
        print("Bölme işlemi sonucu : ",bolme(sayi1,sayi2))
else:
    print("Geçersiz seçim")