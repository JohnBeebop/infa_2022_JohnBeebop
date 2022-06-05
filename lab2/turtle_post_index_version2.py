cifri = []   #цифры, считываемые из файла
x = 40  # ширина цифры, которую рисует черепаха
import turtle
turtle.shape("turtle")
turtle.width(3)
turtle.color("blue")
turtle.speed(5)
turtle.penup()
turtle.backward(x*6) #перед выполнением рисования цифр сдвигаем черепаху влево
turtle.pendown()
"""
Отрисовываем цифры. Начальная позиция черепахи - правый верхний угол цифры. 
Начальная позиция черепахи, смотрит направо, по оси х.
2**0.5*x основание равнобедренного прямоугольного треугольника 
"""
zero = [(90, x*2), (90, x), (90, x*2), (90, x)]
one = [(135, 2**0.5*x), (180, 2**0.5*x), (135, x*2), (180, x*2), (90, 0)]
two = [(180, x), (180, x), (90, x), (45, 2**0.5*x), (225, x), (180, x), (135, 2**0.5*x), (315, x), (90, 0)]
three = [(180, x), (180, x), (135, 2**0.5*x), (225, x), (135, 2**0.5*x), (180, 2**0.5*x), (225, x), (135, 2**0.5*x), (45, 0)]
four = [(90, x*2), (180, x), (270, x), (90, x), (180, x), (270, x), (270, x), (90, 0)]
five = [(180, x), (270, x), (270, x), (90, x), (90, x), (180, x), (270, x), (270, x), (90, x), (90, x)]
six = [(135, 2**0.5*x), (225, x), (90, x), (90, x), (90, x), (45, 2**0.5*x), (45, 0)]
seven = [(180, x), (180, x), (135, 2**0.5*x), (315, x), (180, x), (45, 2**0.5*x), (45, 0)]
eight = [(90, x*2), (90, x), (90, x), (90, x), (180, x), (90, x), (90, x)]
nine = [(90, x), (45, 2**0.5*x), (180, 2**0.5*x), (225, x), (90, x), (90, x)]

def drawing(c): #drawing post numberst
        for y in c:
            turtle.right(y[0])
            turtle.forward(y[1])
        turtle.penup()
        turtle.forward(x*2)
        turtle.pendown()

with open("index.txt") as file: #reading numbers from file and adding ti "cifri"
    for line in file:
        for i in line:
            cifri.append(i)
for i in cifri:
    if i == "1":
        drawing(one)
    elif i == "2":
        drawing(two)
    elif i == "3":
        drawing(three)
    elif i == "4":
        drawing(four)
    elif i == "5":
        drawing((five))
    elif i == "6":
        drawing(six)
    elif i == "7":
        drawing(seven)
    elif i == "8":
        drawing(eight)
    elif i == "9":
        drawing(nine)
    elif i == "0":
        drawing(zero)
input()