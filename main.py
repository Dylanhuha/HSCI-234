import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)

    c = 150
    v = 20
    
    p5.strokeWeight(2)
    p5.fill(240,0,0)
    p5.ellipse(c, 280, 40, 40)#tail
    p5.noStroke()
    p5.fill(250,30,120)
    p5.ellipse(c, 190, 120, 160) #body

    p5.fill(240, 0, 0)
    p5.ellipse(c-v, 50, 30, 90)
    p5.ellipse(c+v, 50, 30, 90)#out ear
    p5.fill(250,30,120,240)
    p5.ellipse(c-v, 65, 20, 60)
    p5.ellipse(c+v, 65, 20, 60)#inner ear

    p5.fill(240, 0, 0)
    p5.ellipse(c, 100, 80, 80) #face

    v1 = 10
    l = 30
    y1 = 90
    
    p5.fill(250, 30, 120)
    p5.ellipse(c-v, y1, l, l)
    p5.ellipse(c+v, y1, l, l)
    p5.fill(100, 0, 0,200)
    p5.ellipse(c-v+v1/2, y1, l-v1, l-v1)
    p5.ellipse(c+v-v1/2, y1, l-v1, l-v1) #eyes

    p5.fill(250, 30, 120)
    p5.stroke(50,0,0)
    p5.ellipse(c, 100+v, v1, v1) #mouth

    p5.fill(240, 0, 0)
    p5.ellipse(c-v1, 120-v1, v, v)
    p5.ellipse(c+v1, 120-v1, v, v) #cheek

    p5.noStroke()
    p5.rect(115, 97, 70, v1)
    p5.stroke(50,0,0)  # cover box

    p5.fill(250, 30, 120)
    p5.ellipse(c, 100, v1, v1) #nose
    
    p5.noStroke()

    x1 = 60
    x2 = 120
    y2 = 260
    x3 = 180
    x4 = 240

    p5.fill(240, 0, 0)

    p5.rect(x2-v1, c, 20, 30)
    p5.ellipse(x2, x3, 20, 20)
    p5.rect(x3-v1, c, 20, 30)
    p5.ellipse(x3, x3, 20, 20)
   
    p5.fill(240,0,0) # fill things below with red
    p5.ellipse(x1, y2, 20, 20)
    p5.ellipse(x2, y2, 20, 20)
    p5.rect(x1, 250, 60, 20) #left foot

    for i in range(5):
        p5.stroke(i*50,0,0,i*50)
        p5.ellipse(x2, 240,60-i*15, 60-i*15)
    p5.noStroke()

    p5.fill(240,0,0) # fill things below with red
    p5.ellipse(x3, y2, 20, 20)
    p5.ellipse(x4, y2, 20, 20)
    p5.rect(x3, 250, 60, 20) #right foot
    
    for i in range(5):
        p5.stroke(i*50,0,0,i*50)
        p5.ellipse(x3, 240,60-i*15, 60-i*15)
    p5.noStroke()
