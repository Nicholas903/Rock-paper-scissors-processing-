import random
player_selection = 0
player2_selection = 0
player_one_selected = None


def setup():
    global player_selection, player_one_selected

    background(255)
    size(1000,1000)

def draw():
    global player_selection, player_one_selected
    game_board()
    player_one_choice()
    player_two_choice()
    
          
def game_board():
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
    


def player_one_choice():
    global player_selection, player_one_selected 
    if player_selection == 1:
        Image = loadImage("Rock.jpg")
        image(Image,230,330)
        player_one_selected = True

    elif player_selection == 2:
        Image2 = loadImage("Paper.jpg")
        image(Image2,245,325)
        player_one_selected = True

    elif player_selection == 3:
        Image3 = loadImage("Scissors.jpg")
        image(Image3,245,320)
        player_one_selected = True

  
  
        
                    
def player_two_choice():
    global player2_selection, player_one_selected
    if player_one_selected == True:
        player2_selection = random.randint(1,4)
        print(player2_selection)

    
    
    if player2_selection == 1:
        Image = loadImage("Rock.jpg")
        image(Image,430,330)
        player_one_selected = None

    elif player2_selection == 2:
        Image2 = loadImage("Paper.jpg")
        image(Image2,445,325)
        player_one_selected = None

    elif player2_selection == 3:
        Image3 = loadImage("Scissors.jpg")
        image(Image3,445,320)
        player_one_selected = None


        
        
        
def mousePressed():
    global player_selection

    println(mouseX)
    println(mouseY)
    if mouseX < 300 and mouseX > 100 and mouseY < 900 and mouseY > 700:
        player_selection = 1
    if mouseX < 600 and mouseX > 400 and mouseY < 900 and mouseY > 700:
        player_selection = 2
    if mouseX < 900 and mouseX > 700 and mouseY < 900 and mouseY > 700:
        player_selection = 3
    
    
