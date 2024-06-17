# %%
import pygame
import os
import random

# Asegurando que el directorio de trabajo es el correcto
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Iniciando Pygame
pygame.init()

# Configurando la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Fondo de pantalla
background = pygame.image.load('background_image.jpg')
background = pygame.transform.scale(background, (800, 600))

# Jugador
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0  # Inicializar la variable de cambio de posición en X
playerY_change = 0  # Inicializar la variable de cambio de posición en Y

# Enemigo
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800 - enemyImg.get_width())
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

# Bala
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = -0.5
bullet_state = "ready"

# Obtener dimensiones del jugador
player_width = playerImg.get_width()
player_height = playerImg.get_height()

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state, bulletX, bulletY
    bullet_state = "fire"
    bulletX = x
    bulletY = y
    screen.blit(bulletImg, (x + 16, y + 10))

def game_loop():
    global playerX, playerY, playerX_change, playerY_change, enemyX, enemyY, enemyX_change, enemyY_change, bulletY, bullet_state
    running = True
    while running:
        screen.fill((0, 0, 0))  # Rellenar la pantalla con color negro

        # Background image
        screen.blit(background, (0, 0))

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
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    fire_bullet(playerX, playerY)

            # Soltar el teclado
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0

        # Actualizar la posición del jugador
        playerX += playerX_change
        playerY += playerY_change

        # Configurando el margen horizontal del jugador
        if playerX <= 0:
            playerX = 0
        elif playerX >= 800 - player_width:
            playerX = 800 - player_width

        # Configurando el margen vertical del jugador
        if playerY <= 0:
            playerY = 0
        elif playerY >= 600 - player_height:
            playerY = 600 - player_height

        # Configurando los movimientos del enemigo
        enemyX += enemyX_change

        if enemyX <= 0 or enemyX >= 736:
            enemyX_change = -enemyX_change  # Cambiar la dirección
            enemyY += enemyY_change  # Mover hacia abajo

        # Movimiento de la bala
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY += bulletY_change

        # Reiniciar la bala cuando salga de la pantalla
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        # Dibujar el jugador y el enemigo en las nuevas posiciones
        player(playerX, playerY)
        enemy(enemyX, enemyY)

        pygame.display.update()  # Actualizar la pantalla

    pygame.quit()

if __name__ == "__main__":
    game_loop()


# %%
