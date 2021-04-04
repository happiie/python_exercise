# Snake Game!
# by AKMAL_FARHAN

#import all module needed
import pygame, sys, random, time

#initial pygame  (6,0)
check_error = pygame.init()
if check_error[1] > 0:#if got errors; (succes, fail), fail > 0
    print("(!) had {0} initializing error, existing...".format(check_error[1]))
    sys.exit(-1) #exit program 

else: #(6,0) = no error
    print("(+) pygame succesful initialized!")
    
#create play surface
playSurface = pygame.display.set_mode((720,460)) #set_mode((height,width)); can take 1 arg
pygame.display.set_caption('SNAKE GAME !!!') #set_caption('string only); windows title

#color Color(red, green, blue); start with 0->255
red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

#FPS Controller
fpsController = pygame.time.Clock()

#Important variable
snakePos = [100, 50] #start point
snakeBody = [[100, 50],[90, 50],[80, 50]]

foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0

#Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72) #type & siza font
    GOsurf = myFont.render('GAME OVER !!!', True, red) #draw text into surface
    GOrect = GOsurf.get_rect() #draw text in rectangle
    GOrect.midtop = (360, 15) #draw text center and at top
    playSurface.blit(GOsurf, GOrect) #draw inmage into other
    showScore(0)
    pygame.display.flip() #update full display on screen
    time.sleep(4)
    pygame.quit() #close game
    sys.exit() #close console    

#score function
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score) , True, black)
    Srect = Ssurf.get_rect()
    if choice==1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)
    
# Main Logic of the Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if player want quit
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == osd('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == osd('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_RIGHT or event.key == osd('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == osd('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT)) #pause the game
    #Validation direction
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'DOWN'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'UP'
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'LEFT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'RIGHT'

  # [x, y]
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
    
    #snake body mechanism   
    snakeBody.insert(0,list(snakePos)) #when snake eat 
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False #stop produce food
    else:
        snakeBody.pop()
    
    if foodSpawn == False: #after eat food produce back
        foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
        
    foodSpawn = True
    
    playSurface.fill(white) #set background as white
    for pos in snakeBody: #draw the snake   
        pygame.draw.rect(playSurface, green,pygame.Rect(pos[0],pos[1],10,10))
        #pygame.Rect(pos[x],pos[y],sizeX,sizeY)
    pygame.draw.rect(playSurface, brown,pygame.Rect(foodPos[0],foodPos[1],10,10))

    #boundry (WALL)
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
    
    #self hit
    for block in snakeBody[1:]:
        if snakePos[0] == snakePos[0] and snakePos[1] == snakePos[1]:
            gameOver()
            
    #common stuff
    showScore()
    pygame.display.flip() #show the white background
    fpsController.tick(10) #25frame per second
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        


    
    
    

    
    
    
    
    
    
    
    
    
    
                
                
                
                
                
                
            
    

    
    
    






