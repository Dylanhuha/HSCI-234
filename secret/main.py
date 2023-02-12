import js
p5 = js.window

N = p5.random(4,8)
n = int(N)

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
 

def draw():
    p5.background(255)           # white background
    p5.push()  
    p5.translate(150, p5.mouseY)
    draw_head() 
    draw_nose(-10,15,p5.mouseX/20)
    draw_nose(10,15,p5.mouseX/20)
    draw_sharkteeth(n,p5.mouseY/30) #teeth bigger with mouse y
    draw_eye(-25, -15, 15 + p5.mouseX/20) 
    draw_eye(25, -15, 15 + p5.mouseX/20)   
    draw_spine(-10, 65)
    p5.pop()  

def draw_head():
    p5.rect(-50, -40, 100, 100)

def draw_nose(x, y, radius):
    p5.push()
    p5.noFill()
    p5.arc(-10, 15, 20, 20, p5.radians(100), p5.radians(310))
    p5.arc(10, 15, 20, 20, p5.radians(230), p5.radians(80))
    p5.fill(0)
    p5.ellipse(x, y, radius/4, radius/4)
    p5.pop()

def draw_sharkteeth(number,Size):
    p5.push()
    size = Size
    p5.translate(-number*(size/2), number*5)
    p5.fill(255)
    for i in range(0, number): 
        p5.triangle(0+i*size , -size, size/2+i*size, 0, size+i*size, -size)
        p5.triangle(0+i*size , size , size/2+i*size, 0, size+i*size, size)
    p5.pop()

        
def draw_eye(x, y, radius):
    p5.fill(255)
    p5.ellipse(x, y, radius, radius) 
    p5.fill(0)
    p5.ellipse(x, y, radius/4, radius/4)
