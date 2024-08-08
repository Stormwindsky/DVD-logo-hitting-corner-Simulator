import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des constantes
WIDTH, HEIGHT = 640, 480
SPEED = 2
LOGO_SIZE = 50

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Définition du logo DVD
logo = pygame.Surface((LOGO_SIZE, LOGO_SIZE))
logo.fill((255, 0, 0))  # couleur rouge

# Définition de la position et de la vitesse du logo
x, y = WIDTH // 2, HEIGHT // 2
vx, vy = SPEED, SPEED

# Boucle principale
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacement du logo
    x += vx
    y += vy

    # Collision avec les bords de l'écran
    if x < 0 or x > WIDTH - LOGO_SIZE:
        vx = -vx
    if y < 0 or y > HEIGHT - LOGO_SIZE:
        vy = -vy

    # Dessin du logo
    screen.fill((0, 0, 0))  # fond noir
    screen.blit(logo, (x, y))

    # Mise à jour de l'écran
    pygame.display.flip()
    pygame.time.Clock().tick(60)