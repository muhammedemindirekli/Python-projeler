from random import randint 
rand = randint(1,11)
sayac = 0


while True:
    sayac += 1
    sayi = int(input("1 ile 10 arasında bir değer giriniz (0 çıkış) :"))

    if(sayi == 0):
        print("oyunu kapattınız")
        break
    elif sayi < rand:
        print("Daha yüksek bir sayı giriniz !!")
        continue
    elif sayi > rand:
        print("Daha düşük bir sayı giriniz !!")
        continue
    else:
        print("Rastgele seçilen sayı{}!".format(rand))
        print("{}tahminde bulundunuz".format(sayac))

    
