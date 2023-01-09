import pygame
import sys
pygame.init()

# Definir paleta de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)


size = (1280, 720)

# Crear ventana
screen = pygame.display.set_mode(size)

# variable para establecer la velocidad del juego (FPS)
clock = pygame.time.Clock()

# Coordenadas
cord_x = 400
cord_y = 200

# Velocidad de movimiento del cuadrado
speed_x = 3
speed_y = 3

while True:
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            sys.exit()
    
    # ----- LOGICA
    
    
    
    # ----- LOGICA
    
    # Establecer color de fondo        
    screen.fill(BLACK)
    
    ### ----- ZONA DE DIBUJO
    
    
    
    ### ----- ZONA DE DIBUJO
    
    # Actualizar pantalla
    pygame.display.flip()
    
    # Definimos la velocidad del juego
    clock.tick(60)
            
