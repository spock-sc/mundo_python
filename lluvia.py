import pygame, sys, random
pygame.init()

# Definir paleta de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)


size = (1280, 720)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cord_list = []
for i in range(160):
    x = random.randint(0, 1280)
    y = random.randint(0, 720)
    cord_list.append([x, y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    screen.fill(WHITE)


    for cord in cord_list:        
        pygame.draw.circle(screen, RED, cord, 2)
        cord[1] += 1
        if cord[1] > 800:
            cord[1] = 0
                
            
    pygame.display.flip()
    clock.tick(60)
            