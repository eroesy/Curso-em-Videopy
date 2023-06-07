import turtle

janela = turtle.Screen()

tartaruga = turtle.Turtle()

tartaruga.penup()
tartaruga.goto(0,0)
tartaruga.pendown()

tartaruga.write("Tossiu", font=("Arial", 18, "bold"))

tartaruga.penup()
tartaruga.forward(100)
tartaruga.pendown()

tartaruga.write("Passou!", font=("Arial", 18, "bold"))

janela.exitonclick()