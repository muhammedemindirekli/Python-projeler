import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.title("ŞANLI SANCAK") # başlık
w.setup(width=720,height=420) # pencere boyutu
w.bgcolor(red)

# ilk daire
t.up
t.goto(-100,100)#fare imleci lokasyonu
t.color("white")#beyaz renk
t.begin_fill()  #beyaz ile doldur
t.end_fill()

# hilal yapabilmek için ikinci daire
t.goto(-70,-80) #fare imleci lokasyonu
t.color("red")  #kırmızı renk
t.begin_fill()  #rengi doldur
t.circle(100) #çap
t.end_fill() #dolguyu bitir 

# yıldız için hazırlık
t.goto(0,35)
t.fillcolor("white")
t.begin_fill()

# yıldız içi tekrar eden üçgen çizimi
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()
t.goto(-130,-190)

w.exitonclick()