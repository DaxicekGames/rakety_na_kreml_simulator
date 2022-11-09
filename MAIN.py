import pygame
import time
import random
pygame.init()
pygame.font.init()
 
class rocket:
    def __init__(self, x, y, speed, image):
        self.image = pygame.transform.scale(pygame.image.load(image), (100, 100))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def vykresli(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_d] and self.rect.x < WIDTH - speed * 20:
            self.rect.x += speed
        if pressed_keys[pygame.K_a] and self.rect.x > speed:
            self.rect.x -= speed
        if pressed_keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= speed
        if pressed_keys[pygame.K_s] and self.rect.y < HEIGHT - speed * 20:
            self.rect.y += speed
        hokno.blit(self.image, (self.rect.x, self.rect.y))
 
class meteor:
    def __init__(self, speed, image):
        self.image = pygame.transform.scale(pygame.image.load(image), (70, 70))
        self.speed = speed
 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(30, WIDTH-30)
        self.rect.y = -70
        
 
# Konstanty
WIDTH = 800
HEIGHT = 600
VIOLET = 130, 0, 100
WHITE = 255, 255, 255
 
# funkce
def add_meteor():
    global meteors
    meteors.append(meteor( random.randint(5,8), "asteroid.png" ))
 
# Proměnné
hokno = pygame.display.set_mode((WIDTH, HEIGHT))
font1 = pygame.font.SysFont('Arial', 80)
lose = font1.render('YOU LOSE!', True, VIOLET)
running = True
speed = 5
old_time = 0
 
# Sprity
raketa = rocket(WIDTH / 2, HEIGHT / 2, 0, "rocket.png")
meteors = []
 
# add_meteor()
bg = pygame.transform.scale(pygame.image.load("galaxy.jpg"), (WIDTH, HEIGHT))
# Vykreslení
def draw():
    hokno.blit(bg, (0, 0))
    for m in meteors:
        hokno.blit(m.image, (m.rect.x, m.rect.y))
    # hokno.blit(zlobak, (0, 0))
    raketa.vykresli()
    pygame.display.flip()
 
# Hlavní smyčka
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    if pygame.sprite.spritecollide(raketa, meteors, False):
        hokno.blit( lose, (WIDTH/2, HEIGHT/2))
        pygame.display.flip()
        time.sleep(5)
        break
 
    if time.time() - old_time > .5:
        old_time = time.time()
        add_meteor()
    for m in meteors:
        m.rect.y += m.speed
        if (m.rect.y > HEIGHT):
            meteors.remove(m)
 
    draw()
    time.sleep(1/60)
 
pygame.quit()
 