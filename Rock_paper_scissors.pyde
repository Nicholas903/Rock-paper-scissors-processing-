

def setup():
    background(255)
    size(1000,1000)

def draw():
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
    text("Player 1 score",65,90)
    text("Player 2 score",765,90)
