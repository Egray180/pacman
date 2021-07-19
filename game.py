#'create a game' project. This code is for a pacman-based game with many added elements. 
#Written by Ethan Gray.

import simplegui
import random
import math
#images
player_image = simplegui.load_image("https://storage.googleapis.com/codeavengers.appspot.com/cloud/lesson-plans/intro-to-coding/pacman-spritesheet.png")
skin_1 = simplegui.load_image("https://i.imgur.com/0u2Tf1E.png")
skin_2 = simplegui.load_image("https://i.imgur.com/VqeB0hM.png")
skin_3 = simplegui.load_image("https://i.imgur.com/vzhl6pB.png")
skin_4 = simplegui.load_image("https://i.imgur.com/4NernNg.png")
scared_ghost = simplegui.load_image("https://www.seekpng.com/png/full/32-326846_scaredghost-pacman-8-bit-gif.png")
pacman1 = simplegui.load_image("https://i.imgur.com/VPkdWyE.png?2")
pacman2 = simplegui.load_image("https://storage.googleapis.com/codeavengers.appspot.com/cloud/lesson-plans/intro-to-coding/pacman-spritesheet.png")
pacman3 = simplegui.load_image("https://i.imgur.com/rsGQVHv.png?2")
pacman4 = simplegui.load_image("https://i.imgur.com/jonTYbt.png")
pacman5 = simplegui.load_image("https://i.imgur.com/4yxn0Pf.png?1")
pacman6 = simplegui.load_image("https://i.imgur.com/XkMykL1.png")
pacman7 = simplegui.load_image("https://i.imgur.com/7pkdRlo.png?1")
pacman8 = simplegui.load_image("https://i.imgur.com/rTAGr8l.png")
start_button = simplegui.load_image("https://i.imgur.com/scoNLYU.png?1")
play_again_button = simplegui.load_image("https://i.imgur.com/3ojlECc.png")
easy_button = simplegui.load_image("https://i.imgur.com/PKpNrTo.png")
hard_button = simplegui.load_image("https://i.imgur.com/ZUBmBtp.png")
info_button = simplegui.load_image("https://i.imgur.com/6u48Rjw.png")
back_button = simplegui.load_image("https://i.imgur.com/0Q3kjYh.png")
arrows = simplegui.load_image("https://i.imgur.com/fvxEyAE.png?1")
menu = simplegui.load_image("https://i.ya-webdesign.com/images/how-to-make-a-png-background-transparent-5.png")
black_screen = simplegui.load_image("https://i.ytimg.com/vi/XIMLoLxmTDw/hqdefault.jpg")
number_image = simplegui.load_image("https://i.imgur.com/WAPqGJ6.png")
T_key = simplegui.load_image("https://i.imgur.com/XbiKYiX.png")
pacman_overlay = simplegui.load_image("https://i.imgur.com/fRuMl6q.png")
#dimensions and sizes 
START_BUTTON_IMG_WIDTH = 1080
START_BUTTON_IMG_HEIGHT = 1080
START_BUTTON_WIDTH = 300
START_BUTTON_HEIGHT = 300
PLAY_AGAIN_IMG_WIDTH = 1080
PLAY_AGAIN_IMG_HEIGHT = 1080
PLAY_AGAIN_BUTTON_WIDTH = 300
PLAY_AGAIN_BUTTON_HEIGHT = 300
DIFFICULTY_IMG_WIDTH = 1080
DIFFICULTY_IMG_HEIGHT = 1080
DIFFICULTY_BUTTON_WIDTH = 200
DIFFICULTY_BUTTON_HEIGHT = 200
INFO_BACK_IMG_WIDTH = 1080
INFO_BACK_IMG_HEIGHT = 1080
INFO_BACK_BUTTON_WIDTH = 200
INFO_BACK_BUTTON_HEIGHT = 200
ARROW_IMAGE_WIDTH = 6480/6
ARROW_IMAGE_HEIGHT = 6480/6
ARROW_IMAGE_SIZE = (500,500)
NUMBER_SIZE = (24, 40)
NUMBER_COLS = 5
NUMBER_ROWS = 2
NUMBER_IMG_WIDTH = 24
NUMBER_IMG_HEIGHT = 40
#sounds 
intro = simplegui.load_sound('https://vgmdownloads.com/soundtracks/mario-kart-ds/xkrwqfpx/048%20-%20Boss%20Battle%20%28Final%20Lap%29.mp3')
chomp = simplegui.load_sound("https://vgmdownloads.com/soundtracks/pac-man-game-sound-effects/knwtmadt/Chomp.mp3")
powerup = simplegui.load_sound("https://vgmdownloads.com/soundtracks/pac-man-game-sound-effects/rlgcahmx/Cutscene.mp3")
ghost_die = simplegui.load_sound("https://vgmdownloads.com/soundtracks/pac-man-game-sound-effects/zaehkcsz/Ghost.mp3")
player_die = simplegui.load_sound("https://vgmdownloads.com/soundtracks/pac-man-game-sound-effects/yfkgsbwu/Death.mp3")
menu_theme = simplegui.load_sound("https://vgmdownloads.com/soundtracks/mario-kart-ds/jpktnhnj/065%20-%20Rainbow%20Road.mp3")
#size of player image file
player_img_width = 573/5
player_img_height = 105
#size of player/ghost on canvas
PLAYER_SIZE = (50,50)
GHOST_SIZE = (50,50)
#canvas size
WIDTH = 1000
HEIGHT = 750
background_pos = [WIDTH/2,HEIGHT/2]
player_speed = 1.4
ghost_speed = 1.5
player = []
ghosts = []
poof = []
#use to change pacman property 
#game_mode 1 harder 
game_mode = 0
#max number of ghosts 
max_ghost = 2
#global variable to toggle between modes 
mode = 1
#when -1 makes ghost's movement opposite during powerup to run away 
ghost_run = 1
#for pacman animation 
x_pre = 1
y_pre = 0
mod = 5
#global variable to keep track of time
clock = 0
#list with all times stored in it
score = []
#for menu 
info_screen = False
game_start = False
game_over = False

#for ghost's eyes to point in direction they are going
GHOST_COLS = {'right':0,
              'left':1,
              'up':2,
              'down':3}

#starts new game
def new_game():
    global pacman
    global length
    global game_start
    global game_over
    global clock
    global powerups
    global player_img_width
    global player_img_height
    global x_pre
    global y_pre
    pacman = Character(player_image, player_img_width, player_img_height, [WIDTH/2,540], [0,0])
    player.append(pacman)
    length = Timer()
    clock = 0
    ghosts.clear()
    powerups = [Ability([505,295]), Ability([50,50]), Ability([50,700]), Ability([950,700]), Ability([950,50])]
    x_pre = 1
    y_pre = 0
    player_img_width = 573/5
    player_img_height = 105
    game_start = True
    game_over = False
    ones.pos = (635,710)
    tens.pos = (610,710)
    hundreds.pos = (585,710)
    thousands.pos = (565,710)
    intro.rewind()
    intro.set_volume(1.0)
    intro.play()

#like a stopwatch to keep track of time survived    
def timer_handler():
    global clock
    if game_start and not game_over:
        clock += 0.1

#for collision detection     
def distance(pos1, pos2):
    a = pos2[1] - pos1[1]
    b = pos2[0] - pos1[0]
    d = math.sqrt(a**2 + b**2)
    return d

#for AI to move towards player
def location_x(pos1, pos2):
    if pos1[0] - pos2[0] < 0:
        return True 
    else:
        return False

def location_y(pos1, pos2):
    if pos1[1] - pos2[1] > 0:
        return True
    else:
        return False

#for AI to cover greater distance first when in hard mode     
def distance_x(pos1, pos2):
    x_dist = pos1[0] - pos2[0]
    return x_dist

def distance_y(pos1, pos2):
    y_dist = pos1[1] - pos2[1]
    return y_dist

#random ghost trait gen 
def random_stats():
    
    num = random.randrange(0,4)
    if num == 0:
        SKIN = skin_1
        GHOST_IMG_WIDTH = 1080
        GHOST_IMG_HEIGHT = 1080
    elif num == 1:
        SKIN = skin_2
        GHOST_IMG_WIDTH = 1080
        GHOST_IMG_HEIGHT = 1080
    elif num == 2:
        SKIN = skin_3
        GHOST_IMG_WIDTH = 1080
        GHOST_IMG_HEIGHT = 1080
    else:
        SKIN = skin_4
        GHOST_IMG_WIDTH = 1080
        GHOST_IMG_HEIGHT = 1080
    return SKIN, GHOST_IMG_WIDTH, GHOST_IMG_HEIGHT

#class to draw each digit of the time when requested or when game is over
class Number:
    def __init__(self, position, image):
        self.pos = position
        self.image = image
        self.state = 0
        self.time = 1000

    def draw(self, canvas):
        if game_start and not game_over:
            if self.time < 1000:
                col = int(self.state)%NUMBER_COLS
                row = int(self.state)//NUMBER_COLS
                center_x = NUMBER_IMG_WIDTH/2+ col*NUMBER_IMG_WIDTH
                center_y = NUMBER_IMG_HEIGHT/2 +row*NUMBER_IMG_HEIGHT
                canvas.draw_image(self.image, 
                                (center_x, center_y), 
                                (NUMBER_IMG_WIDTH, NUMBER_IMG_HEIGHT), 
                                self.pos, 
                                (NUMBER_SIZE))
        elif game_over:
            col = int(self.state)%NUMBER_COLS
            row = int(self.state)//NUMBER_COLS
            center_x = NUMBER_IMG_WIDTH/2+ col*NUMBER_IMG_WIDTH
            center_y = NUMBER_IMG_HEIGHT/2 +row*NUMBER_IMG_HEIGHT
            canvas.draw_image(self.image, 
                              (center_x, center_y), 
                              (NUMBER_IMG_WIDTH, NUMBER_IMG_HEIGHT), 
                              self.pos, 
                              (NUMBER_SIZE))                            
            
    def update(self): 
        if game_start and not game_over:
            self.time += 1
        
        #keeps in-game time updated 
        ones.state = (((clock%1000)%100))%10
        tens.state = (((clock%1000)%100)-ones.state)//10
        hundreds.state = ((clock%1000)-(clock%1000)%100)//100
        thousands.state = (clock-clock%1000)//1000

class Character:
    def __init__(self, image, image_width, image_height, position, velocity):
        self.image = image
        self.image_width = image_width
        self.image_height = image_height
        self.pos = position
        self.vel = velocity
        self.animated = True 
        self.time = 0
        
    def draw(self, canvas):        
        x_mod = (self.time//10)%mod*player_img_width
        y_mod = (self.time//10)%mod*player_img_height
        canvas.draw_image(self.image, 
                        (player_img_width/2 + x_mod*x_pre, player_img_height/2 + y_mod*y_pre),
                        (player_img_width, player_img_height),
                        self.pos,
                        PLAYER_SIZE)
    
    #fnx to check time when T is pressed 
    def check_time(self):
        ones.time = 0
        tens.time = 0
        hundreds.time = 0
        thousands.time = 0
            
    def update(self):
        global mod
        next_pos = [self.pos[0] + self.vel[0], 
                    self.pos[1] + self.vel[1]]
        
        wall_collision = False
        
        #checks for collision using next_pos
        for wall in MAP:
            if wall.collide(next_pos):
                wall_collision = True
        
        for wall in BORDERS:
            if wall.collide(next_pos):
                wall_collision = True
                
        for wall in CENTER_BOX:
            if wall.collide(next_pos):
                wall_collision = True
        
        #updates position
        if not wall_collision:        
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]
        
        if self.animated:
            self.time += 1
        
        #plays chomp sound
        if game_start and not game_over and mode == 1:
            chomp.play()
        
        #stops chomp sound when powerup is collected
        if mode == 0 or game_over:
            chomp.pause()   
        
        #the two player animations have different # of rows/columns 
        if mode == 1:
            mod = 5
    
        if mode == 0:
            mod = 3
    
    #returns whether or not there is a collsion
    def has_collided(self, other_obj):
        dist = distance(self.pos, other_obj.pos)
        return dist <= 50
    
class Ghost:
    def __init__(self, image, image_width, image_height, position, velocity):
        self.image = image
        self.image_width = image_width
        self.image_height = image_height
        self.og_image = image
        self.og_image_width = image_width
        self.og_image_height = image_height
        self.pos = position
        self.vel = velocity
        self.direction = 'up'
        
    def draw_ghost(self, canvas):
        if mode == 1:
            canvas.draw_image(self.image,
                            (self.image_width/2 + GHOST_COLS[self.direction]*self.image_width, self.image_height/2),
                            (self.image_width, self.image_height),
                            self.pos,
                            GHOST_SIZE)
        else:
            canvas.draw_image(self.image,
                            (self.image_width/2, self.image_height/2),
                            (self.image_width, self.image_height),
                            self.pos,
                            GHOST_SIZE)            
        
    def update(self):
        #updates position
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        #updates direction for animation
        if self.vel[1] > 0:
            self.direction = 'down'
        elif self.vel[1] < 0:
            self.direction = 'up'
        elif self.vel[0] > 0:
            self.direction = 'right'
        else:
            self.direction = 'left'
        
        next_pos = [self.pos[0] + self.vel[0], 
                    self.pos[1] + self.vel[1]]
        
        wall_collision = False
        
        in_wall = False
        
        #checks for collsion using next_pos
        for wall in MAP:
            if wall.collide(next_pos):
                wall_collision = True
            if wall.in_wall(next_pos):
                in_wall = True
        
        for wall in BORDERS:
            if wall.collide(next_pos):
                wall_collision = True
                
        for wall in CENTER_BOX:
            if wall.collide(next_pos):
                wall_collision = True
            if wall.in_wall(next_pos):
                in_wall = True
        
        #uses GHOST_TURN_POINTS_VERT and GHOST_TURN_POINTS_HORZ to update direction where there are no walls
        if self.vel[0] != 0:        
            for wall in GHOST_TURN_POINTS_VERT:
                if wall.in_wall(next_pos):
                    if game_mode == 1:
                        if math.fabs(distance_y(self.pos, pacman.pos)) - math.fabs(distance_x(self.pos, pacman.pos)) > 0:
                            if location_y(self.pos, pacman.pos):
                                self.vel[0] = 0
                                self.vel[1] = -ghost_speed * ghost_run
                            else:
                                self.vel[0] = 0
                                self.vel[1] = ghost_speed * ghost_run
                        else:
                            continue
                    else:
                        change = random.randrange(0,2)
                        if change == 0:
                            if location_y(self.pos, pacman.pos):
                                self.vel[0] = 0
                                self.vel[1] = -ghost_speed * ghost_run
                            else:
                                self.vel[0] = 0
                                self.vel[1] = ghost_speed * ghost_run
                        else:
                            continue
                        
        if self.vel[0] == 0:
            for wall in GHOST_TURN_POINTS_HORZ:
                if wall.in_wall(next_pos):
                    if game_mode ==1:
                        if math.fabs(distance_x(self.pos, pacman.pos)) - math.fabs(distance_y(self.pos, pacman.pos)) > 0:
                            if location_x(self.pos, pacman.pos):
                                self.vel[0] = ghost_speed * ghost_run
                                self.vel[1] = 0
                            else:
                                self.vel[0] = -ghost_speed * ghost_run
                                self.vel[1] = 0
                        else:
                            continue 
                    else:
                        change = random.randrange(0,2)
                        if change == 0:
                            if location_x(self.pos, pacman.pos):
                                self.vel[0] = ghost_speed * ghost_run
                                self.vel[1] = 0
                            else:
                                self.vel[0] = -ghost_speed * ghost_run
                                self.vel[1] = 0
                        else:
                            continue
        
        #changes direction when there is wall collision 
        if wall_collision:
            change = random.randrange(0,5)
            if change == 0:
                if self.vel[0] != 0:
                    self.vel[0] *= -1
                else:
                    self.vel[1] *= -1
            else:
                if self.vel[0] !=0:
                    if location_y(self.pos, pacman.pos):
                        self.vel[0] = 0
                        self.vel[1] = -ghost_speed * ghost_run
                    else:
                        self.vel[0] = 0
                        self.vel[1] = ghost_speed * ghost_run
                else:
                    if location_x(self.pos, pacman.pos):
                        self.vel[0] = ghost_speed * ghost_run
                        self.vel[1] = 0
                    else:
                        self.vel[0] = -ghost_speed * ghost_run
                        self.vel[1] = 0
        
        #when AI 'warp' through walls makes them look like they are glitching (feature)
        skin, width, height = random_stats()
        
        if in_wall:
            self.image_width = width
            self.image_height = height
            self.image = skin
        
        #after powerup is collected and used makes sure that AI images return to what they spawned with
        if mode == 1:
            if not in_wall: 
                self.image_width = self.og_image_width
                self.image_height = self.og_image_height
                self.image = self.og_image
                
        #changes AI image during powerup 
        else:    
            if not in_wall:
                self.image_width = 515
                self.image_height = 514
                self.image = scared_ghost

#powerup class
class Ability:
    def __init__(self, position):
        self.pos = position
        
    def draw(self, canvas):
        canvas.draw_circle([self.pos[0], self.pos[1]], 20, 1, 'yellow', 'yellow')
    
    #changes everything when powerup is collected 
    def powerup(self):
        global mode
        global ghost_run
        global player_speed
        global player_img_width
        global player_img_height
        if mode == 0:
            length.time = 0
            powerup.rewind()
            powerup.play()            
        else:
            length.time = 0
            powerup.play()            
            length.active = True    
            player_speed = 1.7
            if pacman.vel[0] > 0:
                pacman.image = pacman1
                player_img_width = 5058/3
                player_img_height = 1569
                pacman.vel[0] = player_speed
            elif pacman.vel[0] < 0:
                pacman.image = pacman3
                player_img_width = 5058/3
                player_img_height = 1569
                pacman.vel[0] = -player_speed
            elif pacman.vel[1] > 0:
                pacman.image = pacman7
                player_img_width = 1569
                player_img_height = 5058/3
                pacman.vel[1] = player_speed
            elif pacman.vel[1] < 0:
                pacman.image = pacman5
                player_img_width = 1569
                player_img_height = 5058/3
                pacman.vel[1] = -player_speed            
            for ghost in ghosts:
                ghost.vel[0] *= -1
                ghost.vel[1] *= -1
            mode = 0
            ghost_run *= -1
            pacman.time = 0
            poof.append(Poof())

#small animation around player when powerup is collected            
class Poof:
    def __init__(self):
        self.image = simplegui.load_image("https://i.imgur.com/jb0ViVs.png")
        self.pos = pacman.pos 
        self.time = 0
    
    def draw(self, canvas):
        x_mod = (self.time//10)%5*160/5
        canvas.draw_image(self.image, 
                          (160/10 + x_mod, 16), 
                          (160/5, 32), 
                          self.pos, 
                          (100,100))
        
    def update(self):
        global poof
        self.time += 1
        
        if self.time > 50:
            poof.clear()

#keeps track of time since powerup was 
#collected and returns everything to normal when time is up
class Timer:
    def __init__(self):
        self.active = False
        self.time = 0
    
    def update(self):
        global mode
        global ghost_run
        global player_speed
        global player_img_width
        global player_img_height
        global x_pre
        global y_pre
        
        if self.active:
            self.time += 1 
        
        if self.time > 725:
            self.active = False
            self.time = 0
            intro.play()
            player_speed = 1.4
            if pacman.vel[0] > 0:
                pacman.image = pacman2
                player_img_width = 573/5
                player_img_height = 105
                pacman.vel[0] = player_speed
                x_pre = 1
                y_pre = 0
            elif pacman.vel[0] < 0:
                pacman.image = pacman4
                player_img_width = 573/5
                player_img_height = 105
                pacman.vel[0] = -player_speed
                x_pre = 1
                y_pre = 0
            elif pacman.vel[1] > 0:
                pacman.image = pacman8
                player_img_width = 105
                player_img_height = 573/5
                pacman.vel[1] = player_speed
                x_pre = 0
                y_pre = 1
            elif pacman.vel[1] < 0:
                pacman.image = pacman6
                player_img_width = 105
                player_img_height = 573/5
                pacman.vel[1] = -player_speed
                x_pre = 0
                y_pre = 1
            else:
                if pacman.image == pacman1:
                    pacman.image = pacman2
                    player_img_width = 573/5
                    player_img_height = 105
                    x_pre = 1
                    y_pre = 0
                elif pacman.image == pacman3:
                    pacman.image = pacman4
                    player_img_width = 573/5
                    player_img_height = 105
                    x_pre = 1
                    y_pre = 0
                elif pacman.image == pacman5:
                    pacman.image = pacman8
                    player_img_width = 105
                    player_img_height = 573/5
                    x_pre = 0
                    y_pre = 1
                elif pacman.image == pacman7:
                    pacman.image = pacman6
                    player_img_width = 105
                    player_img_height = 573/5
                    x_pre = 0
                    y_pre = 1               
            for ghost in ghosts:
                ghost.vel[0] *= -1
                ghost.vel[1] *= -1
            mode = 1
            ghost_run *= -1
            pacman.time = 0
                                                
class Wall:
    def __init__(self, position, width, height, colour):
        self.pos = position 
        self.width = width
        self.height = height
        self.colour = colour 
        
    def draw(self, canvas):
        canvas.draw_polygon(([self.pos[0]-self.width/2,self.pos[1]-self.height/2], 
                             [self.pos[0]+self.width/2,self.pos[1]-self.height/2], 
                             [self.pos[0]+self.width/2,self.pos[1]+self.height/2], 
                             [self.pos[0]-self.width/2,self.pos[1]+self.height/2]), 
                            1, self.colour, self.colour)
    
    #detects obj collision with walls 
    def collide(self, pos):
        left = self.pos[0] - self.width/2
        right = self.pos[0] + self.width/2
        top = self.pos[1] - self.height/2
        bottom = self.pos[1] + self.height/2
        in_x = pos[0] >= left-25 and pos[0] <= right+25
        in_y = pos[1] >= top-25 and pos[1] <= bottom+25
        return in_x and in_y
    
    #detects when ghost is in wall
    def in_wall(self, pos):
        left = self.pos[0] - self.width/2
        right = self.pos[0] + self.width/2
        top = self.pos[1] - self.height/2
        bottom = self.pos[1] + self.height/2
        in_x = pos[0] >= left and pos[0] <= right
        in_y = pos[1] >= top and pos[1] <= bottom
        return in_x and in_y
        
class Start_Button:
    def __init__(self, image, position, width, height):
        self.image = image
        self.pos = position
        self.width = width
        self.height = height
    
    def draw(self, canvas):
        canvas.draw_image(self.image,
                          (START_BUTTON_IMG_WIDTH/2, START_BUTTON_IMG_HEIGHT/2), 
                          (START_BUTTON_IMG_WIDTH, START_BUTTON_IMG_HEIGHT),
                          self.pos,
                          (self.width, self.height))
    
    #detects when start button is selected 
    def is_selected(self, click_pos):
        left = self.pos[0] - self.width/2
        right = self.pos[0] + self.width/2
        top = self.pos[1] - self.height/5
        bottom = self.pos[1] + self.height/5
        in_x = click_pos[0] >= left and click_pos[0] <= right
        in_y = click_pos[1] >= top and click_pos[1] <= bottom
        return in_x and in_y

class Playagain_Button:
    def __init__(self, image, position, width, height):
        self.image = image
        self.pos = position
        self.width = width
        self.height = height
    
    def draw(self, canvas):
        canvas.draw_image(self.image,
                          (PLAY_AGAIN_IMG_WIDTH/2, PLAY_AGAIN_IMG_HEIGHT/2), 
                          (PLAY_AGAIN_IMG_WIDTH, PLAY_AGAIN_IMG_HEIGHT),
                          self.pos,
                          (self.width, self.height))
    
    def is_selected(self, click_pos):
        left = self.pos[0] - self.width/2
        right = self.pos[0] + self.width/2
        top = self.pos[1] - self.height/3
        bottom = self.pos[1] + self.height/3
        in_x = click_pos[0] >= left and click_pos[0] <= right
        in_y = click_pos[1] >= top and click_pos[1] <= bottom
        return in_x and in_y
    
class Difficulty_Button:
    def __init__(self, image, position, width, height):
        self.image = image
        self.pos = position
        self.width = width
        self.height = height
    
    def draw(self, canvas):
        canvas.draw_image(self.image,
                          (DIFFICULTY_IMG_WIDTH/2, DIFFICULTY_IMG_HEIGHT/2), 
                          (DIFFICULTY_IMG_WIDTH, DIFFICULTY_IMG_HEIGHT),
                          self.pos,
                          (self.width, self.height))
    
    def is_selected(self, click_pos):
        left = self.pos[0] - self.width/3
        right = self.pos[0] + self.width/3
        top = self.pos[1] - self.height/4
        bottom = self.pos[1] + self.height/4
        in_x = click_pos[0] >= left and click_pos[0] <= right
        in_y = click_pos[1] >= top and click_pos[1] <= bottom
        return in_x and in_y 

class Info_Back_Button:
    def __init__(self, image, position, width, height):
        self.image = image
        self.pos = position
        self.width = width
        self.height = height
    
    def draw(self, canvas):
        canvas.draw_image(self.image,
                          (INFO_BACK_IMG_WIDTH/2, INFO_BACK_IMG_HEIGHT/2), 
                          (INFO_BACK_IMG_WIDTH, INFO_BACK_IMG_HEIGHT),
                          self.pos,
                          (self.width, self.height))
    
    def is_selected(self, click_pos):
        left = self.pos[0] - self.width/2
        right = self.pos[0] + self.width/2
        top = self.pos[1] - self.height/3
        bottom = self.pos[1] + self.height/3
        in_x = click_pos[0] >= left and click_pos[0] <= right
        in_y = click_pos[1] >= top and click_pos[1] <= bottom
        return in_x and in_y    
    
class Arrows:
    def __init__(self, image, position):
        self.image = image
        self.pos = position
        self.time = 0 
    #draws arrow animation on menu screen    
    def draw(self, canvas):
        x_mod = (self.time//10)%6*ARROW_IMAGE_WIDTH
        y_mod = (self.time//60)%6*ARROW_IMAGE_HEIGHT
        canvas.draw_image(self.image, 
                          (ARROW_IMAGE_WIDTH/2 + x_mod, ARROW_IMAGE_HEIGHT/2 + y_mod),
                          (ARROW_IMAGE_WIDTH, ARROW_IMAGE_HEIGHT),
                          self.pos,
                          ARROW_IMAGE_SIZE)
    
    #updates time for arrow animation 
    def update(self):
        if not game_start:
            self.time += 1
        
#handler to draw on canvas 
def draw(canvas):
    global player
    global pacman
    global game_over    
    
    #makes background music volume quieter after intro
    if clock >  2.6:
        intro.set_volume(0.1)           
    
    #draws map
    for border in BORDERS:	
        border.draw(canvas)   
    
    if game_start:
        length.update()
    
    for wall in CENTER_BOX:
        wall.draw(canvas)
        
    for wall in MAP:
        wall.draw(canvas)
    
    #draws powerups
    for powerup in powerups:
        powerup.draw(canvas) 
    
    #draws player after intro music
    if clock > 2.8:
        for p in player:
            p.draw(canvas)
            p.update()
    
    #draws AI
    for ghost in ghosts:
        ghost.draw_ghost(canvas)
        ghost.update()
    
    #draws powerup 'poof' animation 
    for p in poof:
        p.draw(canvas)
        p.update()
    
    #draws angry pacman in the background during powerup 
    if mode == 0:
        x_mod = (pacman.time//10)%mod*5058/3
        canvas.draw_image(pacman_overlay, 
                        (5058/6 + x_mod, 1569/2),
                        (5058/3, 1569),
                        (500,375),
                        (1000,750))
    
    #sets up menu/info screen 
    if not game_start:
        menu_theme.play()
        canvas.draw_image(menu,
                         background_pos,
                        (WIDTH,HEIGHT),
                        background_pos,
                        (WIDTH,HEIGHT))
        start_button.draw(canvas)
        easy_button.draw(canvas)
        hard_button.draw(canvas)
        canvas.draw_text("Move Left", (375, 650), 20, 'white', 'monospace')
        canvas.draw_text("Move Right", (700, 650), 20, 'white', 'monospace')
        canvas.draw_text("Move Up", (550, 323), 20, 'white', 'monospace')
        canvas.draw_text("Move Down", (550, 685), 20, 'white', 'monospace')
        #shades which difficulty button is selected 
        if game_mode == 0:
            canvas.draw_image(menu,
                              background_pos,
                              (WIDTH,HEIGHT),
                              (200,200),
                              (140,100))
        else:
            canvas.draw_image(menu,
                              background_pos,
                              (WIDTH,HEIGHT),
                              (200,400),
                              (140,100))
        arrow.update()
        arrow.draw(canvas)
        canvas.draw_image(T_key,
                          (540,540),
                          (1080,1080),
                          (850,260),
                          (200,200))
        canvas.draw_text("Check Time", (795, 350), 20, 'white', 'monospace')
        info_button.draw(canvas)
        if info_screen:
            canvas.draw_image(black_screen,
                            (480/2,360/2),
                            (480,360),
                            (500,375),
                            (WIDTH,HEIGHT))            
            back_button.draw(canvas)
            canvas.draw_circle((100,100), 50, 1, 'yellow', 'yellow')
            canvas.draw_text("POWERUP", (175, 110), 30, 'white', 'monospace')
            canvas.draw_image(skin_1,
                              (1080/2,1080/2),
                              (1080,1080),
                              (100,275),
                              (100,100))
            canvas.draw_text("GHOST", (175,275), 30, 'white', 'monospace')
            canvas.draw_image(scared_ghost,
                              (515/2,514/2),
                              (515,514),
                              (100,450),
                              (100,100))
            canvas.draw_text("SCARED GHOST", (175,460), 30, 'white', 'monospace')
            canvas.draw_text("HOW TO PLAY:", (500,500), 50, 'white', 'monospace')
            canvas.draw_text("Survive for as long as you can." , 
                             (400,550), 30, 'white', 'monospace')
            canvas.draw_text("If you get too close to a ghost,", (400,580), 30, 'white', 'monospace')
            canvas.draw_text("you will die. After collecting a", (400,610), 30, 'white', 'monospace')
            canvas.draw_text("powerup, you can kill the ghosts.", (400,640), 30, 'white', 'monospace')
            canvas.draw_text("In easy mode, the max # of ghosts", (400,670), 30, 'white', 'monospace')
            canvas.draw_text("is 2 and they have smaller brains.", (400,700), 30, 'white', 'monospace')
            canvas.draw_text("In hard mode... good luck.", (400,730), 30, 'white', 'monospace')
            canvas.draw_image(player_image,
                              (573/10,105/2),
                              (573/5,105),
                              (400,100),
                              (100,100))
            canvas.draw_text("YOU", (460,110), 30, 'white', 'monospace')
            canvas.draw_image(pacman1,
                              (5058/6,1569/2),
                              (5058/3,1569),
                              (400,275),
                              (100,100))
            canvas.draw_text("ANGRY YOU", (470,285), 30, 'white', 'monospace')
            canvas.draw_text("PRODUCER:", (20,600), 30, 'white', 'monospace')
            canvas.draw_text("Ethan Gray", (20,630), 30, 'white', 'monospace')
            canvas.draw_text("ANGRY PACMAN ART:", (20,700), 30, 'white', 'monospace')
            canvas.draw_text("Jaden Lee", (20,730), 30, 'white', 'monospace')
    
    #sets up game_over screen                          
    if game_over:
        canvas.draw_image(menu,
                         background_pos,
                        (WIDTH,HEIGHT),
                        background_pos,
                        (WIDTH,HEIGHT))        
        play_again_button.draw(canvas)
        easy_button.draw(canvas)
        hard_button.draw(canvas)
        if game_mode == 0:
            canvas.draw_image(menu,
                              background_pos,
                              (WIDTH,HEIGHT),
                              (200,200),
                              (140,100))
        else:
            canvas.draw_image(menu,
                              background_pos,
                              (WIDTH,HEIGHT),
                              (200,400),
                              (140,100))
        canvas.draw_text("Best Time:", (400,400), 60, "white", "monospace")
        canvas.draw_text("Your Time:", (400,500), 60, "white", "monospace")
        ones.pos = (825,485)
        tens.pos = (800,485)
        hundreds.pos = (775,485)
        thousands.pos = (750,485)
        score.append(clock)
        #checks score list for best time and draws it on game_over screen
        best_score = max(score)
        best_ones.state = (((best_score%1000)%100))%10
        best_tens.state = (((best_score%1000)%100)-ones.state)//10
        best_hundreds.state = ((best_score%1000)-(best_score%1000)%100)//100
        best_thousands.state = (best_score-best_score%1000)//1000
        for b in best_time:
            b.draw(canvas)
                
    #draws time 
    for t in time:
        t.draw(canvas)
        t.update()        
    
    #starts AI spawning when player spawns
    if game_start and clock > 2.8:
        if len(ghosts) < max_ghost:
            if random.randrange(1500) == 0:
                GHOST_IMAGE, GHOST_IMG_WIDTH, GHOST_IMG_HEIGHT = random_stats()
                new_ghost = Ghost(GHOST_IMAGE, GHOST_IMG_WIDTH, GHOST_IMG_HEIGHT, [WIDTH/2,450], [0,-ghost_speed])
                ghosts.append(new_ghost)
    
    #activates powerups when they are hit
    if game_start:
        if len(powerups) >= 1:
            for powerup in powerups:
                if pacman.has_collided(powerup):
                    powerup.powerup()                                
                    powerups.remove(powerup)
    
    #checks for player/ghost death and ends game
    if game_start:            
        if len(ghosts) >= 1:
            for ghost in ghosts:
                if pacman.has_collided(ghost):
                    if mode == 0:
                        ghosts.remove(ghost)
                        ghost_die.play()
                    else:
                        player = []
                        if not game_over:
                            player_die.play()
                        game_over = True
                if ghost.pos[0] < 0 or ghost.pos[0] > 1000 or ghost.pos[1] < 0 or ghost.pos[1] > 750:
                    ghosts.remove(ghost)

#button selection 
def mouse_handler(mouse_position):
    global game_start
    global game_mode
    global max_ghost
    global info_screen
    if not game_start and not info_screen:
        if start_button.is_selected(mouse_position):
            new_game()
            menu_theme.pause()
        if easy_button.is_selected(mouse_position):
            game_mode = 0
            max_ghost = 2
        if hard_button.is_selected(mouse_position):
            game_mode = 1
            max_ghost = 3
    if not game_start:
        if info_button.is_selected(mouse_position):
            info_screen = True
        if back_button.is_selected(mouse_position):
            info_screen = False
    elif game_over:
        if play_again_button.is_selected(mouse_position):
            new_game() 
        if easy_button.is_selected(mouse_position):
            game_mode = 0
            max_ghost = 2
        if hard_button.is_selected(mouse_position):
            game_mode = 1
            max_ghost = 3

#updates player velocities and images when key hits 
def key_press(key):
    global player_img_width
    global player_img_height
    global x_pre
    global y_pre
    if game_start and not game_over:
        if key == simplegui.KEY_MAP['right']:
            pacman.vel[0] = player_speed
            if mode == 0:
                player_img_width = 5058/3
                player_img_height = 1569
                pacman.image = pacman1
                x_pre = 1
                y_pre = 0
            else:
                player_img_width = 573/5 
                player_img_height = 105
                pacman.image = pacman2
                x_pre = 1
                y_pre = 0
        if key == simplegui.KEY_MAP['left']:
            pacman.vel[0] = -player_speed
            if mode == 0:
                player_img_width = 5058/3
                player_img_height = 1569
                pacman.image = pacman3
                x_pre = 1
                y_pre = 0
            else:
                player_img_width = 573/5
                player_img_height = 105
                pacman.image = pacman4
                x_pre = 1
                y_pre = 0
        if key == simplegui.KEY_MAP['up']:
            pacman.vel[1] = -player_speed
            if mode == 0:
                player_img_width = 1569
                player_img_height = 5058/3
                pacman.image = pacman5
                x_pre = 0
                y_pre = 1
            else:
                player_img_width = 105
                player_img_height = 573/5
                pacman.image = pacman6
                x_pre = 0
                y_pre = 1
        if key == simplegui.KEY_MAP['down']:
            pacman.vel[1] = player_speed
            if mode == 0:
                player_img_width = 1569
                player_img_height = 5058/3
                pacman.image = pacman7
                x_pre = 0
                y_pre = 1
            else:
                player_img_width = 105
                player_img_height = 573/5
                pacman.image = pacman8
                x_pre = 0
                y_pre = 1
        if key == simplegui.KEY_MAP['T']:
            pacman.check_time()
#updates velocities when key releases         
def key_release(key):
    if game_start and not game_over:    
        if key == simplegui.KEY_MAP['right']:
            pacman.vel[0] = 0
        if key == simplegui.KEY_MAP['left']:
            pacman.vel[0] = 0
        if key == simplegui.KEY_MAP['up']:
            pacman.vel[1] = 0
        if key == simplegui.KEY_MAP['down']:
            pacman.vel[1] = 0

#lists with all map walls/turn points 
BORDERS = [Wall([2.5,375], 5, 750, 'black'), Wall([500,2.5], 1000, 5, 'black'),
           Wall([997.5,375], 5, 750, 'black'), 
           Wall([500,747.5], 1000, 5, 'black')]
CENTER_BOX = [Wall([510,500], 200, 5, 'black'), Wall([407.5,452.5], 5, 100, 'black'), 
              Wall([612.5,452.5], 5, 100, 'black'), 
             Wall([435,400], 60, 5, 'black'), Wall([585,400], 60, 5, 'black')]
MAP = [Wall([510,330], 210, 5, 'black'), Wall([325,490], 5, 180, 'black'), Wall([300,660], 200, 5, 'black'),
      Wall([325,202.5], 5, 255, 'black'), Wall([510,575.5], 210, 5, 'black'), 
       Wall([75,375], 150, 200, 'black'), Wall([100,620], 5, 80, 'black'), Wall([87.5,140], 5, 100, 'black'),
      Wall([205,95], 65, 190, 'black'), Wall([237.5,428], 5, 306, 'black'),
      Wall([122.5,580], 50, 5, 'black'), Wall([600,705], 200, 90, 'black'), Wall([700,487.5], 5, 180, 'black'),
      Wall([510,165], 210, 180, 'black'), Wall([700,200] ,5, 255, 'black'),
      Wall([850,525], 125, 250, 'black'), Wall([850,200], 125, 250, 'black')]
GHOST_TURN_POINTS_VERT = [Wall([655,40], 1, 40, 'white'), Wall([365,40], 1, 40, 'white'),
                         Wall([365,365], 1, 40, 'white'), Wall([655,365], 1, 40, 'white'),
                         Wall([365,615], 1, 40, 'white'), Wall([655,615], 1, 40, 'white')]
GHOST_TURN_POINTS_HORZ = [Wall([955,365], 40, 1, 'white'), Wall([365,295], 40, 1, 'white'),
                         Wall([655,295], 40, 1, 'white'), Wall([365,540], 40, 1, 'white'),
                         Wall([655,540], 40, 1, 'white')]

#powerup list 
powerups = [Ability([505,295]), Ability([50,50]), Ability([50,700]), Ability([950,700]), Ability([950,50])]

#time list with all 4 digits appended 
time = []
ones = Number([635,710], number_image)
time.append(ones)
tens = Number([610,710], number_image)
time.append(tens)
hundreds = Number([585,710], number_image)
time.append(hundreds)
thousands = Number([560,710], number_image)
time.append(thousands) 
#best time list with all 4 digits appended 
best_time = []
best_ones = Number([825,385], number_image)
best_time.append(best_ones)
best_tens = Number([800,385], number_image)
best_time.append(best_tens)
best_hundreds = Number([775,385], number_image)
best_time.append(best_hundreds)
best_thousands = Number([750,385], number_image)
best_time.append(best_thousands)

#buttons
start_button = Start_Button(start_button, (510,150), START_BUTTON_WIDTH, START_BUTTON_HEIGHT)
play_again_button = Playagain_Button(play_again_button, (505,150), PLAY_AGAIN_BUTTON_WIDTH, PLAY_AGAIN_BUTTON_HEIGHT)
easy_button = Difficulty_Button(easy_button, (200,200), DIFFICULTY_BUTTON_WIDTH,  DIFFICULTY_BUTTON_HEIGHT)
hard_button = Difficulty_Button(hard_button, (200,400), DIFFICULTY_BUTTON_WIDTH,  DIFFICULTY_BUTTON_HEIGHT)
info_button = Info_Back_Button(info_button, (200,600), INFO_BACK_BUTTON_WIDTH, INFO_BACK_BUTTON_HEIGHT)
back_button = Info_Back_Button(back_button, (850,100), INFO_BACK_BUTTON_WIDTH, INFO_BACK_BUTTON_HEIGHT)
arrow = Arrows(arrows, (600,500))

#set all elements 
timer = simplegui.create_timer(100, timer_handler)
timer.start()
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_press)
frame.set_keyup_handler(key_release)
frame.set_mouseclick_handler(mouse_handler)
frame.set_canvas_background("white")
# Start the frame animation
frame.start()
