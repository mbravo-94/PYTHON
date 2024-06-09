# %%
import pygame

# Iniciando Pygame
pygame.init()

# Configurando la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Invaders')

# Game Loop
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Rellenar la pantalla con color negro
    pygame.display.flip()   # Actualizar la pantalla

# Salir de Pygame
pygame.quit()

# %%