import js
p5 = js.window

class Sprite :
    def __init__(self, x = 150, y = 150):
        self.x = x  
        self.y = y

class Accumulate(Sprite):  # Spaceship is a child of Sprite
    def __init__(self):
        self.img = p5.loadImage('accumulate.png')
        self.x = 150
        self.y = 150
        self.width = self.img.width
        self.height = self.img.height
    
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img, 0, 0)
        p5.pop()

class Attack1(Accumulate):
    bitmap1  = [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 1, 1, 1, 1, 1, 1, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    ]

    def draw_bitmap(self, n):
        p5.fill(230,10,10)
        p5.noStroke()
        p5.push()
        p5.translate(-10*3, -10*3)  # center the 11x8 pixel bitmap
        # traverse 2D lists with i and j loops:
        for j in range(10):
            for i in range(10):
                if(n == 1):  # draw column j, row i of bitmap1
                    if(self.bitmap1[j][i] == 0):
                        p5.rect(i*6, j*6, 6, 6)
        p5.pop()

    def __init__(self, x = 150, y = 150):
        self.x = x  
        self.y = y
        self.width = 70
        self.height = 70

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        self.draw_bitmap(1)  
        p5.pop()

class Attack2(Accumulate):
    bitmap2  = [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
        [ 0, 0, 1, 1, 1, 1, 1, 1, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    ]

    def draw_bitmap(self, n):
        p5.fill(200,20,20)
        p5.noStroke()
        p5.push()
        p5.translate(-10*3, -10*3)  # center the 11x8 pixel bitmap
        # traverse 2D lists with i and j loops:
        for j in range(10):
            for i in range(10):
                if(n == 1):  # draw column j, row i of bitmap1
                    if(self.bitmap2[j][i] == 0):
                        p5.rect(i*6, j*6, 6, 6)
        p5.pop()

    def __init__(self, x = 150, y = 150):
        self.x = x  
        self.y = y
        self.width = 70
        self.height = 70

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        self.draw_bitmap(2)  
        p5.pop()

class Defense1(Accumulate):
    bitmap3  = [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0 ],
        [ 0, 0, 1, 1, 1, 1, 1, 1, 0, 0 ],
        [ 0, 0, 1, 1, 1, 1, 1, 1, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    ]

    def draw_bitmap(self, n):
        p5.fill(0,255,255)
        p5.noStroke()
        p5.push()
        p5.translate(-10*3, -10*3)  # center the 11x8 pixel bitmap
        # traverse 2D lists with i and j loops:
        for j in range(10):
            for i in range(10):
                if(n == 1):  # draw column j, row i of bitmap1
                    if(self.bitmap3[j][i] == 0):
                        p5.rect(i*6, j*6, 6, 6)
        p5.pop()

    def __init__(self, x = 150, y = 150):
        self.x = x  
        self.y = y
        self.width = 70
        self.height = 70

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        self.draw_bitmap(3)  
        p5.pop()

class Defense2(Accumulate):
    bitmap4  = [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0 ],
        [ 0, 0, 1, 1, 1, 1, 1, 1, 0, 0 ],
        [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
        [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
        [ 0, 0, 1, 1, 1, 1, 1, 1, 0, 0 ],
        [ 0, 0, 0, 1, 1, 1, 1, 0, 0, 0 ],
        [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    ]

    def draw_bitmap(self, n):
        p5.fill(0,0,255)
        p5.noStroke()
        p5.push()
        p5.translate(-10*3, -10*3)  # center the 11x8 pixel bitmap
        # traverse 2D lists with i and j loops:
        for j in range(10):
            for i in range(10):
                if(n == 1):  # draw column j, row i of bitmap1
                    if(self.bitmap4[j][i] == 0):
                        p5.rect(i*6, j*6, 6, 6)
        p5.pop()

    def __init__(self, x = 150, y = 150):
        self.x = x  
        self.y = y
        self.width = 70
        self.height = 70

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        self.draw_bitmap(4)  
        p5.pop()

def init_Sprite():
    global sprite_list
    sprite_list = []
    for i in range(2):
        sprite = Sprite(85 + i*130, 150)
        sprite_list.append(sprite)


class Player:
    Action = [
        accumulate,
        attack1,
        attack2,
        defense1,
        defense2
        ]




    def __init__(self, player_id):
        self.player_id = player_id
        self.accumulation = 0
        self.current_action = Player.Action["accumulate"]


    def update_action(self, action):
        self.current_action = action
        if action == Player.Action["accumulate"]:
            self.accumulation += 1
        elif action in (Player.Action["attack1"], Player.Action["defense1"]) and self.accumulation >= 1:
            self.accumulation -= 1
        elif action in (Player.Action["attack2"], Player.Action["defense2"]) and self.accumulation >= 2:
            self.accumulation -= 2




player1 = Player(1)
player2 = Player(2)




player1.update_action(Player.Action["attack1"])




def check_winner(player1, player2):
    if player1.current_action == Player.Action["attack1"] and player2.current_action == Player.Action["accumulate"]:
        return player1
    if player2.current_action == Player.Action["attack1"] and player1.current_action == Player.Action["accumulate"]:
        return player2
    if player1.current_action == Player.Action["attack2"] and player2.current_action == Player.Action["defense1"]:
        return player1
    if player2.current_action == Player.Action["attack2"] and player1.current_action == Player.Action["defense1"]:
        return player2
    return None


def get_action_from_input():
    if (p5.keyIsPressed == True):
        if (p5.keyCode ==='s') :
            player1.performAction('accumulate')
        else if (p5.keyCode == 'a') :
            player1.performAction('attack1')
        else if (p5.keyCode == 'q') :
            player1.performAction('attack2')
        else if (p5.keyCode == 'd') :
            player1.performAction('defense1')
        else if (p5.keyCode == 'e') :
            player1.performAction('defense2')
            
        if (p5.key === 'k') :
            player2.performAction('accumulate')
        else if (p5.key === 'j') :
            player2.performAction('attack1')
        else if (p5.key === 'u') :
            player2.performAction('attack2')
        else if (p5.key === 'l') :
            player2.performAction('defense1')
        else if (p5.key === 'o') :
            player2.performAction('defense2')
    

player1 = Player(1)
player2 = Player(2)


while True:
    action1_input = input("Player 1, choose an action (s: accumulate, a: attack1, q: attack2, d: defense1, e: defense2): ")
    action2_input = input("Player 2, choose an action (k: accumulate, j: attack1, u: attack2, l: defense1, o: defense2): ")


    player1_action = get_action_from_input(action1_input)
    player2_action = get_action_from_input(action2_input)


    if player1_action is not None and player2_action is not None:
        player1.update_action(player1_action)
        player2.update_action(player2_action)


        winner = check_winner(player1, player2)
        if winner is not None:
            print(f"Player {winner.player_id} wins!")
            break
    else:
        print("Invalid input, please try again.")




def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    p5.background(255)

    # Draw player 1's current action
    p5.push()
    p5.translate(50, 150)
    player1.current_action.draw()
    p5.pop()

    # Draw player 2's current action
    p5.push()
    p5.translate(250, 150)
    player2.current_action.draw()
    p5.pop()
    

def keyPressed(event):









def keyPressed(event):
    pass 




def keyReleased(event):
    pass




def mousePressed(event):
    pass




def mouseReleased(event):
    pass