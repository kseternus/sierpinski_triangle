import turtle

turtle.bgcolor('#000000')
colors = ['#ffffba', '#baffc9', '#bae1ff']
raphael = turtle.Turtle()
raphael.speed(0)
raphael.right(30)
raphael.pu()
raphael.ht()


def sierpinski_triangle(size, order):
    if order == 0:
        raphael.stamp()
    else:
        for i in range(0, 3):
            raphael.fillcolor(colors[i % 3])
            raphael.pencolor(colors[i % 3])
            raphael.forward(size)
            sierpinski_triangle(size/2, order-1)
            raphael.backward(size)
            raphael.left(120)


sierpinski_triangle(200, 5)     # use 100&4 or 200&5 or 300&6 above that will mess up triangles
turtle.done()
