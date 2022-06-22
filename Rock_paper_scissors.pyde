import random
player_selection = 0
player2_selection = 0
player_one_selected = None
score1 = 0
score2 = 0
mode = 0

def setup():
    global player_selection, player_one_selected,score1,score2,mode

    size(1000,1000)

def draw():
    global player_selection, player_one_selected,mode
    background(255)

    game_board()
    player1score()
    player2score()
    player_two_choice()
    win_screen()
    win2_screen()
    
    if player_selection == 1:
        Image = loadImage("Rock.jpg")
        image(Image,230,330)

    elif player_selection == 2:
        Image2 = loadImage("Paper.jpg")
        image(Image2,245,325)

    elif player_selection == 3:
        Image3 = loadImage("Scissors.jpg")
        image(Image3,245,320)
        
    
          
def game_board():
    
        
        
    if mode == 0:
        fill(255)
        strokeWeight(6)
        rect(100,100,100,110)
        rect(800,100,100,110)
        
        rect(200,300,200,200)
        rect(600,300,200,200)
        
        rect(100,700,200,200)
        rect(400,700,200,200)
        rect(700,700,200,200)
        fill(0)
        textSize(26)
        text("Select rock, paper, or scissor",325,650)
        text("VS",480,410)
        text("Player 1 score",65,80)
        text("Player 2 score",765,80)
        Image = loadImage("Rock.jpg")
        image(Image,130,730)
        Image2 = loadImage("Paper.jpg")
        image(Image2,450,730)
        Image3 = loadImage("Scissors.jpg")
        image(Image3,750,725)
    



  
def win_screen():
    if mode == 1:
        reset()
        background(255)
        textSize(26)
        fill(255)
        stroke(0)
        rect(400,400,200,100)
        fill(0)
        text("Congradulations you won!",335,350)
        text("Return",455,460)
       
       
       
def win2_screen():
    if mode == 2:
        reset()
        background(255)
        textSize(26)
        fill(255)
        stroke(0)
        rect(400,400,200,100)
        fill(0)
        text("The computer has won!",345,350) 
        text("Return",455,460)
             
def player_two_choice():
    global player2_selection, player_one_selected
    
    
    if player2_selection == 1:
        Image = loadImage("Rock.jpg")
        image(Image,630,330)

    elif player2_selection == 2:
        Image2 = loadImage("Paper.jpg")
        image(Image2,645,325)

    elif player2_selection == 3:
        Image3 = loadImage("Scissors.jpg")
        image(Image3,650,320)



def win():
    global score1,score2,player_two_selection,player2_selection, player_one_selected,mode

    
    if player_selection == 1 and player2_selection == 2:
        score2 += 1
        player_one_selected = False
    if player_selection == 2 and player2_selection == 3:
        score2 += 1
        player_one_selected = False
    if player_selection == 3 and player2_selection == 1:
        score2 += 1
        player_one_selected = False
    if player_selection == 2 and player2_selection == 1:
        score1 += 1
        player_one_selected = False
    if player_selection == 3 and player2_selection == 2:
        score1 += 1
        player_one_selected = False
    if player_selection == 1 and player2_selection == 3:
        score1 += 1
        player_one_selected = False
    

    

    if score1 == 3:
        mode = 1

    if score2 == 3:
        mode = 2
        
        

# player 1 score              
def player1score():
    fill(0)
    textSize(100)
    text(score1,120,190)
    
        
# player 2 score
def player2score():
    fill(0)
    textSize(100)
    text(score2,820,190)    
  
def reset():
    global score1,score2,player_selection,player2_selection
    score1 = 0
    score2 = 0
    player_selection = 0
    player2_selection = 0    
def mousePressed():
    global player_selection,player2_selection,mode 

    println(mouseX)
    println(mouseY)
    if mouseX < 300 and mouseX > 100 and mouseY < 900 and mouseY > 700:
        player_selection = 1
        player2_selection = random.randint(1,3)
        win()

    if mouseX < 600 and mouseX > 400 and mouseY < 900 and mouseY > 700:
        player_selection = 2
        player2_selection = random.randint(1,3)
        win()

    if mouseX < 900 and mouseX > 700 and mouseY < 900 and mouseY > 700:
        player_selection = 3
        player2_selection = random.randint(1,3)
        win()

    if mouseX < 600 and mouseX > 400 and mouseY < 500 and mouseY > 395 and (mode == 1 or mode == 2) :
        mode = 0
    
