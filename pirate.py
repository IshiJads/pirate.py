import pygame
import random
import time
pygame.init()

WIDTH = 1210
HEIGHT = 908

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pirate = pygame.image.load("images/sword.png")
pirate = pygame.transform.scale(pirate, (60, 90))

gem_red = pygame.image.load("images/gemstone_red.png")
gem_red = pygame.transform.scale(gem_red, (40, 40))

gem_yellow = pygame.image.load("images/gemstone_yellow.png")
gem_yellow = pygame.transform.scale(gem_yellow, (40, 40))

gem_green = pygame.image.load("images/gemstone_green.png")
gem_green = pygame.transform.scale(gem_green, (40, 40))

gem_blue = pygame.image.load("images/gemstone_blue.png")
gem_blue = pygame.transform.scale(gem_blue, (40, 40))

bombimg = pygame.image.load("images/bomb.png")
bombimg = pygame.transform.scale(bombimg,(50,50))

background = pygame.image.load("images/background1.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

gem_images = [gem_red, gem_yellow, gem_green, gem_blue]

score = 0
font = pygame.font.SysFont("Arial", 36)
text = font.render("Score: " + str(score), True, (255, 255, 255))
starttime = time.time()

class Pirate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pirate
        self.rect = self.image.get_rect()
        self.rect.center = x, y

pirate = Pirate(WIDTH // 2, HEIGHT // 2)
pirate_group = pygame.sprite.Group()
pirate_group.add(pirate)

class Gemstone(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = random.choice(gem_images)
        self.rect = self.image.get_rect()
        self.rect.center = x, y

class Bomb (pygame.sprite.Sprite):
    def __init__ (self,x,y):
        super().__init__()
        self.image = bombimg
        self.rect = self.image.get_rect()
        self.rect.center = x,y

gem_group = pygame.sprite.Group()
for i in range(15):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(100, HEIGHT - 100)
    gem = Gemstone(x, y)
    gem_group.add(gem)

bomb_group = pygame.sprite.Group()
for i in range(15):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(100, HEIGHT - 100)
    bomb = Bomb(x, y)
    bomb_group.add(bomb)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            pirate.rect.center = pos
    screen.fill("sky blue")
    screen.blit(background, (0, 0))
    time_elapsed=time.time()-starttime
    print (time_elapsed)
    if time_elapsed>10:
        if score>=10:
            screen.blit(background,(0,0))
            text2 = font.render("Your loot was sucessful.",True,(255,255,255))
            screen.blit(text2,(400,400))
        else:
            screen.blit(background,(0,0))
            text2 = font.render("Try again next time.",True,(255,255,255))
            screen.blit(text2,(400,400))

    gemhit=pygame.sprite.spritecollide(pirate,gem_group,True)
    bombhit=pygame.sprite.spritecollide(pirate,bomb_group,True)
    for item in gemhit:
        score+=1
        text=font.render("score:"+ str(score), True,(255,255,255))

    for item in bombhit:
        score-=1
        text=font.render("score:"+ str(score), True,(255,255,255))

    
    pirate_group.draw(screen)
    gem_group.draw(screen)
    bomb_group.draw(screen)
    screen.blit(text, (250, 50))
    pygame.display.update()