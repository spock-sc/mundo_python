# Importacion de las librerias
import pygame
import random

#Definimos la paleta de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# CONSTANTES
HEIGHT_SCREEN = 1280
WIDTH_SCREEN = 720
             
# Inicializamos pygame
pygame.init()

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
              

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() 
        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = 620
        
        
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/laser.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y -= 5


# Definimos el modo de la pantalla
screen = pygame.display.set_mode([HEIGHT_SCREEN, WIDTH_SCREEN])

# Inicializamos el reloj del juego
clock = pygame.time.Clock()

# Variable para salir del juego
game_over = False

# Marcador
score = 0

# Oculta el puntero del mouse
pygame.mouse.set_visible(1)

# Cargamos en memoria la imagen de fondo
background = pygame.image.load("assets/fondo_estrellas.jpg").convert()

# Lista de Sprites
all_sprites_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()

# Creación de los meteoros
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(HEIGHT_SCREEN)
    meteor.rect.y = random.randrange(500)
    
    meteor_list.add(meteor)
    all_sprites_list.add(meteor)

# Creamos las instancias del juego
player = Player()
all_sprites_list.add(player)

# Bucle principal del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser = Laser()
            laser.rect.x = player.rect.x + 45
            laser.rect.y = player.rect.y -20
            
            all_sprites_list.add(laser)
            laser_list.add(laser)

    # Llamamos al metodo update
    all_sprites_list.update()
    
    # Colisiones laser-meteoros
    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)
        for meteor in meteor_hit_list:
            all_sprites_list.remove(laser)
            laser_list.remove(laser)
            score += 100
            print(score)
        if laser.rect.y < -10:
            all_sprites_list.remove(laser)
            laser_list.remove(laser)
            
    # Cargamos la imagen de fondo del juego
    screen.blit(background, [0, 0])

    # Dibujamos los sprites en pantalla
    all_sprites_list.draw(screen)
            
    # Actualización de la pantalla
    pygame.display.flip()
    
    # Velocidad del reloj del Juego (FPS)   
    clock.tick(60)
    
pygame.quit()    