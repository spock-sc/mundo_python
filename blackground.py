# Importacion de las librerias
import pygame

# Inicializamos pygame
pygame.init()

#Definimos la paleta de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# Definimos el modo de la pantalla
screen = pygame.display.set_mode([720, 720])

# Inicializamos el reloj del juego
clock = pygame.time.Clock()

# Variable para salir del juego
game_over = False

# Oculta el puntero del mouse
pygame.mouse.set_visible(0)

# Cargamos en memoria la imagen de fondo
background = pygame.image.load("assets/background.png").convert()

# Bucle principal del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
    # Cargamos la imagen de fondo del juego
    screen.blit(background, [0, 0])
        
    # Actualización de la pantalla
    pygame.display.flip()
    
    # Velocidad del reloj del Juego (FPS)   
    clock.tick(60)
    
pygame.quit()