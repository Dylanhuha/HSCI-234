import js

p5 = js.window

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.circle((0, 0), 50)
        p5.pop()
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

player1 = Player(150, 150)
player2 = Player(200, 200)
player1.x += 2


def key_pressed():
    if (p5.keyCode == p5.RIGHT_ARROW):
        player2.x += 2
    elif (p5.keyCode == p5.LEFT_ARROW):
        player2.x -= 2
    elif (p5.keyCode == p5.DOWN_ARROW):
        player2.y += 2
    elif (p5.keyCode == p5.UP_ARROW):
        player2.y -= 2


def check_collision(player1, player2):
    if player1 and player2:
        dist = p5.dist((player1.x, player1.y), (player2.x, player2.y))
        if dist < 10:
            player1.x = 150
            player1.y = 150
            player2.x = 200
            player2.y = 200
    
def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')

def draw():
    p5.background(255)           
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    player1.draw()
    player2.draw()
    player2.move(0, 0)
    check_collision(player1, player2)
    p5.loop()

def keyPressed(event):
    print('keyPressed.. ' + str(p5.key))

def keyReleased(event):
    print('keyReleased.. ' + str(p5.key))

def mousePressed(event):
    print('mousePressed..')

def mouseReleased(event):
    print('mouseReleased..')
