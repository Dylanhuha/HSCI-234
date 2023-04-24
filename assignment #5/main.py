import js
p5 = js.window
program_state = 'state 1'
image1 = p5.loadImage('image1.png')
image2 = p5.loadImage('image2.png')
image3 = p5.loadImage('image3.png')

def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')
    p5.imageMode(p5.CENTER)
    
def draw():
    global image1 image2 image3
    p5.background(255)           
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    global image1,image2,image3
    if (program_state == "state1"):
        p5.image(image1, 0 ,0)
    if (millis() - program_timer > 2000):
        program_state = "state2"
    else if (program_state == "state2"):
        p5.image(image2, 0 ,0)
    else if (program_state == "state3"):
        p5.image(image3, 0 ,0)

def keyPressed(event):
    global program_state
    if(program_state == "state2"):
        program_state = "state3"
    elif(program_state == "state3"):
        program_state = "state2"
    elif(program_state == "state2"):
        program_state = "state3"

def keyReleased(event):
    print('keyReleased.. ' + str(p5.key))
    if (key == "1"):
        program_state = "state1"
        program_timer = millis()
    else if (key == "2"):
        program_state = "state2"
    else if (key == "3"):
        program_state = "state3"

def mousePressed(event):
    print('mousePressed..')

def mouseReleased(event):
    print('mouseReleased..')