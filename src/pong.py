import pygame
from pygame.locals import *

# Definizione dei colori
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

# Dimensioni della finestra
WIDTH = 800
HEIGHT = 600

# Inizializzazione di Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Variabile di controllo per il ciclo principale
running = True

# Colore di sfondo
background = GRAY

# Parametri della palla
BALL_RADIUS = 30
ball_pos = [WIDTH // 2, HEIGHT // 2]
speed = [5, 2]

# Parametri della piattaforma
OFFSET_PLATFORM = 20
PLATFORM_H = 10
PLATFORM_W = 100
platform_pos = [WIDTH // 2 - PLATFORM_W // 2, HEIGHT - OFFSET_PLATFORM]
platform_speed = 10

# Clock per controllare il frame rate
clock = pygame.time.Clock()

# Suono
boing_sound = pygame.mixer.Sound("./../assets/boing.mp3")
sound_enabled = True

# Variabile per il punteggio
hit_platform = 0

# Font per il testo
font = pygame.font.Font(None, 36)

# Ciclo principale del gioco
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = GREEN
            elif event.key == pygame.K_m:
                sound_enabled = False
            elif event.key == pygame.K_u:
                sound_enabled = True

    keys = pygame.key.get_pressed()
    # Movimento della piattaforma
    platform_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * platform_speed
    # Assicurarsi che la piattaforma rimanga all'interno dei bordi dello schermo
    platform_pos[0] = max(0, min(platform_pos[0], WIDTH - PLATFORM_W))

    # Disegno dello sfondo
    screen.fill(background)

    # Movimento della palla
    ball_pos[0] += speed[0]
    ball_pos[1] += speed[1]

    # Controllo collisioni con i bordi dello schermo
    if ((ball_pos[0] + BALL_RADIUS) > WIDTH or (ball_pos[0] - BALL_RADIUS) < 0):
        speed[0] *= -1
        ball_pos[0] += speed[0]
    if ((ball_pos[1] + BALL_RADIUS) > HEIGHT or (ball_pos[1] - BALL_RADIUS) < 0):
        speed[1] *= -1
        ball_pos[1] += speed[1]

    # Disegno del punteggio
    score_text = font.render(f"Hit: {hit_platform}", True, WHITE)
    score_rect = score_text.get_rect(topleft=(10, 10))
    pygame.draw.rect(screen, MAGENTA, score_rect.inflate(10, 5))

    # Controllo bounds della piattaforma
    if (platform_pos[0] <= PLATFORM_W // 2):
        platform_pos[0] = PLATFORM_W // 2
    if (platform_pos[0] >= (WIDTH - PLATFORM_W // 2)):
        platform_pos[0] = WIDTH - PLATFORM_W // 2

    # Controllo se la palla tocca la piattaforma
    if ((platform_pos[0]) <= ball_pos[0] <= (platform_pos[0] + PLATFORM_W) and
            platform_pos[1] <= (ball_pos[1] + BALL_RADIUS) <= (platform_pos[1] + OFFSET_PLATFORM)):
        speed[1] *= -1
        hit_platform += 1

    # Controllo se la palla è caduta
    if ((ball_pos[1] + BALL_RADIUS) >= HEIGHT):
        running = False

    # Disegno della piattaforma, della palla e del punteggio
    pygame.draw.rect(screen, MAGENTA, (platform_pos[0], platform_pos[1], PLATFORM_W, PLATFORM_H))
    screen.blit(score_text, score_rect)
    pygame.draw.circle(screen, WHITE, (ball_pos[0], ball_pos[1]), BALL_RADIUS)

    # Aggiornamento della schermata
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
