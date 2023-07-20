import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 740, 480

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tamaño del gato y el ratón
CAT_SIZE = 50
MOUSE_SIZE = 20

# Velocidad de movimiento del gato
CAT_SPEED = 2

# Creación de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Catch the Mouse')

# Función para cargar una imagen y cambiar su tamaño
def load_and_resize_image(image_path, width, height):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, (width, height))

# Cargar las imágenes del gato y el ratón
cat_image = load_and_resize_image('cat.png', CAT_SIZE, CAT_SIZE)
mouse_image = load_and_resize_image('mouse.png', MOUSE_SIZE, MOUSE_SIZE)

# Función para mostrar un mensaje en la pantalla
def show_message(message, size=30):
    font = pygame.font.Font(None, size)
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)

# Función para reiniciar el juego
def restart_game():
    cat_x, cat_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    mouse_x, mouse_y = random.randint(0, SCREEN_WIDTH-MOUSE_SIZE), random.randint(0, SCREEN_HEIGHT-MOUSE_SIZE)
    return cat_x, cat_y, mouse_x, mouse_y

# Inicialización de las posiciones iniciales del gato y el ratón
cat_x, cat_y, mouse_x, mouse_y = restart_game()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Movimiento del gato
    if keys[pygame.K_LEFT]:
        cat_x -= CAT_SPEED
    if keys[pygame.K_RIGHT]:
        cat_x += CAT_SPEED
    if keys[pygame.K_UP]:
        cat_y -= CAT_SPEED
    if keys[pygame.K_DOWN]:
        cat_y += CAT_SPEED

    # Limitar las coordenadas del gato dentro de la pantalla
    cat_x = max(0, min(SCREEN_WIDTH - CAT_SIZE, cat_x))
    cat_y = max(0, min(SCREEN_HEIGHT - CAT_SIZE, cat_y))

    # Mover el ratón de forma aleatoria
    mouse_x += random.randint(-35, 35)
    mouse_y += random.randint(-35, 35)
    mouse_x = max(0, min(SCREEN_WIDTH - MOUSE_SIZE, mouse_x))
    mouse_y = max(0, min(SCREEN_HEIGHT - MOUSE_SIZE, mouse_y))

    # Comprobar si el gato ha atrapado al ratón
    if cat_x < mouse_x + MOUSE_SIZE and cat_x + CAT_SIZE > mouse_x and cat_y < mouse_y + MOUSE_SIZE and cat_y + CAT_SIZE > mouse_y:
        show_message("¡Atrapaste al ratón!")
        cat_x, cat_y, mouse_x, mouse_y = restart_game()

    # Dibujar el gato y el ratón en la pantalla
    screen.fill(BLACK)
    screen.blit(cat_image, (cat_x, cat_y))
    screen.blit(mouse_image, (mouse_x, mouse_y))
    pygame.display.update()
    pygame.time.delay(30)
