import pygame
pygame.init()


# Definir paleta de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
player_width = 15
player_height = 120
ancho_pantalla = 1280
centro_pantalla_x = 640
centro_platalla_y = 360

# Definimos tamaño ventana
screen_size = (1280, 720)

# Creamos la ventana del juego
screen = pygame.display.set_mode(screen_size)

# Creamos el reloj del juego
clock = pygame.time.Clock()

# Coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 360 - (player_height / 2)
player1_y_speed = 0

# Coordenadas y velocidad del jugador 2
player2_x_coor = 1230 - player_width
player2_y_coor = 360 - (player_height / 2)
player2_y_speed = 0

# Coordenadas de la pelota
pelota_x = 640
pelota_y = 360
pelota_speed_x = 5
pelota_speed_y = 5

# Definimos la variable para salir del juego
game_over = False

# Bucle principal del juego
while not game_over:
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            game_over = True
        if Event.type == pygame.KEYDOWN:
            # Jugador 1
            if Event.key == pygame.K_w:
                player1_y_speed = -5
            if Event.key == pygame.K_s:
                player1_y_speed = 5
            # Jugador 2
            if Event.key == pygame.K_UP:
                player2_y_speed = -5
            if Event.key == pygame.K_DOWN:
                player2_y_speed = 5
                
        if Event.type == pygame.KEYUP:
            # Jugador 1
            if Event.key == pygame.K_w:
                player1_y_speed = 0
            if Event.key == pygame.K_s:
                player1_y_speed = 0
            # Jugador 2
            if Event.key == pygame.K_UP:
                player2_y_speed = 0
            if Event.key == pygame.K_DOWN:
                player2_y_speed = 0
        
    # Efecto rebote superior e inferior de la pelota
    if pelota_y > 710 or pelota_y < 10:
        pelota_speed_y *= -1
        
    # Efecto si la pelota sale por el lado derecho
    if pelota_x > 1280:
        pelota_x = centro_pantalla_x
        pelota_y = centro_platalla_y
        # Si sale de la pantalla invierte la dirección
        pelota_speed_x *= -1
        pelota_speed_y *= -1
        
    # Efecto si la pelota sale por el lado izquierdo
    if pelota_x < 0:
        pelota_x = centro_pantalla_x
        pelota_y = centro_platalla_y
        # Si sale de la pantalla invierte la dirección
        pelota_speed_x *= -1
        pelota_speed_y *= -1
   
    # Modifica las coordenadas para dar movimiento a los jugadores y la pelota
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed
    # Movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y 
    
    screen.fill(BLACK)
    
    # Zona de dibujo de sprites
    jugador1 = pygame.draw.rect(screen, WHITE, (player1_x_coor, player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(screen, WHITE, (player2_x_coor, player2_y_coor, player_width, player_height))
    pelota = pygame.draw.circle(screen, WHITE, (pelota_x, pelota_y), 10)
    
    # Colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1
    
    pygame.draw.line(screen, WHITE, (centro_pantalla_x, 0), (centro_pantalla_x, 800), 2)
    # pygame.draw.circle(screen, WHITE, (centro_pantalla_x, centro_platalla_y), 50, 2)
    # Zona de dibujo de sprites
    
    # Actualizar pantalla
    pygame.display.flip()
    
    # Definimos la velocidad del juego
    clock.tick(60)
            
            
pygame.quit()