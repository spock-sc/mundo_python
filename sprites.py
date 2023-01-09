# Importacion de las librerias
import pygame
import random

# Inicializamos pygame
pygame.init()

#Definimos la paleta de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# CONSTANTES
ANCHO_PANTALLA = 1280
ALTO_PANTALLA = 720

# Definimos las clases
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y += 1
    
        if self.rect.y > ALTO_PANTALLA:
            self.rect.y = -10
            self.rect.x = random.randrange(ANCHO_PANTALLA)
                 
            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]
        

# Definimos el modo de la pantalla
screen = pygame.display.set_mode([ANCHO_PANTALLA, ALTO_PANTALLA])

# Inicializamos el reloj del juego
clock = pygame.time.Clock()

# Variable para salir del juego
game_over = False

# Definimos un marcador para acumular puntos
score = 0

# Oculta el puntero del mouse
# pygame.mouse.set_visible(0)

# Cargamos en memoria la imagen de fondo
background = pygame.image.load("assets/fondo_estrellas.jpg").convert()

#meteor_list = pygame.sprite.Group()
#all_sprite_list = pygame.sprite.Group()

# Creación de las listas para cargar grupos de sprites
meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

# Creamos las instancias de los sprites
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(1200)
    meteor.rect.y = random.randrange(700)
    
    # Añadimos las listas
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)
    
    
player = Player()
all_sprite_list.add(player)
           
# Bucle principal del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    
    all_sprite_list.update()
    
        
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_list, True)
    
    
    for meteor in meteor_hit_list:
        score += 1
        print(score)
                    
    # Cargamos la imagen de fondo del juego
    screen.blit(background, [0, 0])
    
    # Dibujamos los sprites en la pantalla
    all_sprite_list.draw(screen)
    
    # Actualización de la pantalla
    pygame.display.flip()
    
      
    # Velocidad del reloj del Juego (FPS)   
    clock.tick(60)
    
pygame.quit()
            