import pygame

# Inicializamos pygame
pygame.init()

# Definimos la paleta de colores para el juego
white = (255, 255, 255)
black = (0, 0, 0)

# Definimos el modo de la pantalla
screen = pygame.display.set_mode([1720, 720])

# Inicializamos el reloj del juego
clock = pygame.time.Clock()

# Variable para salir del juego
game_over = False

# Oculta el puntero del mouse
pygame.mouse.set_visible(0)

# Cargamos en memoria la imagen de fondo
background = pygame.image.load("assets/background.png").convert()

# Cargamos en memoria la imagen de la nave del jugador
player = pygame.image.load("assets/player.png")

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Localizar la posición del mouse
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    
    #colocamos el fondo de pantalla en pantalla
    screen.blit(background, [0, 0])
    
    # Colocamos la imagen de la nave del jugador en pantalla
    screen.blit(player, [x, y])
    
    # Actualización de la pantalla
    pygame.display.flip()
    
    # Velocidad del reloj del Juego (FPS)
    clock.tick(60)
    
pygame.quit()
            