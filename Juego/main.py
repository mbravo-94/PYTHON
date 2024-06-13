# %%
import pygame
import os

# Asegurando que el directorio de trabajo es el correcto
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Iniciando Pygame
pygame.init()

# Configurando la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Jugador
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0  # Inicializar la variable de cambio de posición en X
playerY_change = 0  # Inicializar la variable de cambio de posición en Y

def player(x, y):
    screen.blit(playerImg, (x, y))

def game_loop():
    global playerX, playerY, playerX_change, playerY_change
    running = True
    while running:
        # RGB (Red, Green, Blue)
        screen.fill((0, 0, 0))  # Rellenar la pantalla con color negro

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Pulsar el teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.2
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.2
                if event.key == pygame.K_UP:
                    playerY_change = -0.2
                if event.key == pygame.K_DOWN:
                    playerY_change = 0.2

            # Soltar el teclado
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0

        playerX += playerX_change
        playerY += playerY_change
        player(playerX, playerY)
        pygame.display.update()  # Actualizar la pantalla

    # Salir de Pygame
    pygame.quit()

if __name__ == "__main__":
    game_loop()

# %%
