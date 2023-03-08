import time
import pygame
import random



# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)

RED = (255,0,0)
GREEN = (0,255,0)

BRIGHT_RED = (200,0,0)
BRIGHT_GREEN = (0,200,0)

# Define some game constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
char_WIDTH = 100

PAUSE = True

# Set up game
randomNum = random.randint(1, 6)

pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('Shuriken')

musicAdd = 'assets/sound' + str(randomNum) + '.wav'
pygame.mixer.music.load(musicAdd)
pygame.mixer.music.play(-1)

# Load some resources

backImgAdd = 'assets/background' + str(randomNum) + '.jpg'
backImg = pygame.image.load(backImgAdd)


backRect = backImg.get_rect()

introImg = pygame.image.load('assets/konoha.jpg')
villageImg = pygame.image.load('assets/village.jpg')
ramenImg = pygame.image.load('assets/ramen.jpg')

narutoImg = pygame.image.load('assets/naruto.png')
sasukeImg = pygame.image.load('assets/sasuke.png')
kakashiImg = pygame.image.load('assets/kakashi.png')
leeImg = pygame.image.load('assets/lee.png')
shikamaruImg = pygame.image.load('assets/shikamaru.png')

CHARIMG = sasukeImg # initialize character img

imageList = [sasukeImg, narutoImg]

weapon1 = pygame.image.load('assets/s1.png')
weapon2 = pygame.image.load('assets/s2.png')
weapon3 = pygame.image.load('assets/s3.png')
weapon4 = pygame.image.load('assets/s4.png')
weaponList = [weapon1, weapon2, weapon3, weapon4]



clock = pygame.time.Clock()

def textObjects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def messageDisplay(text, color, img):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = textObjects(text, largeText,color)
    TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    gameLoop(img)

def die(img):
    messageDisplay("Ouch!", RED, img)

def hit(weaponImg, img, x, y, wx, wy):
    # Check if a Shuriken hits Character
    charSurf = img.convert_alpha()
    weaponSurf = weaponImg.convert_alpha()
    char_mask = pygame.mask.from_surface(charSurf)
    weapon_mask = pygame.mask.from_surface(weaponSurf)
    offset = (int(wx - x), int(wy - y))
    return char_mask.overlap(weapon_mask, offset)

def button(msg,x,y,w,h,ic,ac,action=None, args = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if args == None:
                action()
            else:
                action(args)
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("impact",20)
    textSurf, textRect = textObjects(msg, smallText, BLACK)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def selectCharButton(msg,x,y,w,h,ic,ac,img):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1:
            gameLoop(img)

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("impact",20)
    textSurf, textRect = textObjects(msg, smallText, BLACK)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitGame():
    pygame.quit()
    quit()

def gameIntro():
    intro = True

    while intro:

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(WHITE)
        placeObject(introImg, DISPLAY_WIDTH / 2 - 150, DISPLAY_HEIGHT / 2 - 300)
        largeText = pygame.font.SysFont("impact",115)
        TextSurf, TextRect = textObjects("Shuriken", largeText, BLACK)
        TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT * 0.6))
        gameDisplay.blit(TextSurf, TextRect)

        button("START",150,600,100,50,GREEN,BRIGHT_GREEN,chooseCharacter)
        button("Quit",550,600,100,50,RED,BRIGHT_RED,quitGame)

        pygame.display.update()
        clock.tick(15)

def placeObject(image, x, y):
    gameDisplay.blit(image,(x,y))

def displayScore(score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("SCORE: "+str(score), True, BLACK)
    gameDisplay.blit(text,(0,0))

def sayHi():
    print ("Hi!")


def chooseCharacter():

    choosing = True

    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(villageImg, backRect)
        largeText = pygame.font.SysFont("impact", 70)
        TextSurf, TextRect = textObjects("Choose Your Character:", largeText, BLACK)
        TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_WIDTH / 10))
        gameDisplay.blit(TextSurf, TextRect)

        # selectCharButton(msg,x,y,w,h,ic,ac,img)
        selectCharButton("Naruto", 350, 200, 100, 50, GREEN, BRIGHT_GREEN, narutoImg)
        selectCharButton("Sasuke", 350, 300, 100, 50, GREEN, BRIGHT_GREEN, sasukeImg)
        selectCharButton("Kakashi", 350, 400, 100, 50, GREEN, BRIGHT_GREEN, kakashiImg)
        selectCharButton("Lee", 350, 500, 100, 50, GREEN, BRIGHT_GREEN, leeImg)
        selectCharButton("Shikamaru", 350, 600, 100, 50, GREEN, BRIGHT_GREEN, shikamaruImg)

        # button(msg,x,y,w,h,ic,ac,action=None, args = None)
        button("Quit", 350, 700, 100, 50, RED, BRIGHT_RED, quitGame)

        pygame.display.update()
        clock.tick(15)

def unpause():
    global PAUSE
    PAUSE = False


def paused():
    gameDisplay.blit(ramenImg, backRect)
    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRect = textObjects("Take A Break", largeText, GREY)
    TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
    gameDisplay.blit(TextSurf, TextRect)

    global PAUSE
    PAUSE = True
    while PAUSE:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)

        button("Continue", 150, 500, 100, 50, GREEN, BRIGHT_GREEN, unpause)
        button("Quit", 550, 500, 100, 50, RED, BRIGHT_RED, quitGame)

        pygame.display.update()
        clock.tick(15)

def gameLoop(img):

    # Set positions for char
    x = (DISPLAY_WIDTH * 0.45)
    y = DISPLAY_HEIGHT - 213

    # Will adjust char's horizontal position
    x_change = 0

    # Set positions for Shuriken

    wwidth = 100
    wheight = 100
    wx = random.randrange(0, DISPLAY_WIDTH - wwidth)
    wy = -600
    wspeed = 7
    wcount = 1

    score = 0

    weapon = weaponList[random.randrange(0, 4)]
    gameExit = False

    while not gameExit:


        gameDisplay.blit(backImg, backRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -wspeed * 1.2
                if event.key == pygame.K_RIGHT:
                    x_change = wspeed * 1.2
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        button("CHANGE CHARACTER", 620, 10, 160, 50, GREEN, BRIGHT_GREEN, chooseCharacter)

        x += x_change

        if x < 0:
            placeObject(img, 0, y)
        elif x + char_WIDTH > DISPLAY_WIDTH:
            placeObject(img, DISPLAY_WIDTH - char_WIDTH, y)
        else:
            placeObject(img, x, y)


        placeObject(weapon, wx, wy)
        displayScore(score)
        wy += wspeed


        if wy > DISPLAY_HEIGHT:
            wy = 0 - wheight
            wx = random.randrange(0, DISPLAY_WIDTH - wwidth)
            score += 1
            if wspeed < 10:
                wspeed += 1
            n = random.randrange(0, 4)
            weapon = weaponList[n]

        # hit(weaponImg, x, y, wx, wy)
        if hit(weapon, img, x, y, wx, wy):
            die(img)

        pygame.display.update()
        clock.tick(120)


gameIntro()
gameLoop(CHARIMG)
pygame.quit()
quit()
