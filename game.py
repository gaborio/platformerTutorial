# Importamos pygame y os
import pygame
import os

# Inicializamos pygame
pygame.init()

# Definimos el tamaño de la ventana y el título
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de plataformas sencillo")

# Definimos los colores que vamos a usar
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (227, 53, 13)
GREEN = (77, 173, 91)
BLUE = (0, 117, 190)

# Definimos la fuente que vamos a usar para el texto
font = pygame.font.SysFont("Arial", 32)

# Definimos una función para cargar una imagen desde la carpeta "assets"
def load_image(filename):
  # Obtenemos la ruta completa del archivo
  path = os.path.join("assets", filename)
  # Cargamos la imagen con pygame
  image = pygame.image.load(path)
  # Devolvemos la imagen
  return image

# Definimos una función para cargar un sonido desde la carpeta "assets"
def load_sound(filename):
  # Obtenemos la ruta completa del archivo
  path = os.path.join("assets", filename)
  # Cargamos el sonido con pygame
  sound = pygame.mixer.Sound(path)
  # Devolvemos el sonido
  return sound
# Definimos una clase para representar al jugador
class Player(pygame.sprite.Sprite):
    # Definimos el constructor de la clase
    def __init__(self, x, y):
        # Llamamos al constructor de la clase padre (pygame.sprite.Sprite)
        super().__init__()
        # Cargamos la imagen del jugador
        self.image = load_image("player.png")
        # Obtenemos el rectángulo que contiene a la imagen
        self.rect = self.image.get_rect()
        # Establecemos la posición inicial del jugador según los parámetros x e y
        self.rect.x = x
        self.rect.y = y
        # Establecemos la velocidad inicial del jugador en el eje x e y
        self.speed_x = 0
        self.speed_y = 0

    # Definimos un método para actualizar el estado del jugador
    def update(self):
        # Actualizamos la posición del jugador según su velocidad en el eje x e y
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


# Comprobamos si el jugador ha chocado con alguna plataforma en el eje x
platform_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
# Si ha chocado con alguna plataforma
for platform in platform_hit_list:
    # Si se estaba moviendo hacia la derecha, colocamos al jugador al borde izquierdo de la plataforma
    if self.speed_x > 0:
        self.rect.right = platform.rect.left
    # Si se estaba moviendo hacia la izquierda, colocamos al jugador al borde derecho de la plataforma
    elif self.speed_x < 0:
        self.rect.left = platform.rect.right

    # En cualquier caso, detenemos el movimiento horizontal del jugador
    self.speed_x = 0

# Comprobamos si el jugador ha chocado con alguna plataforma en el eje y
platform_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
# Si ha chocado con alguna plataforma
for platform in platform_hit_list:
    # Si se estaba moviendo hacia abajo, colocamos al jugador sobre la plataforma y detenemos su caída
    if self.speed_y > 0:
        self.rect.bottom = platform.rect.top
        self.speed_y = 0
    # Si se estaba moviendo hacia arriba, colocamos al jugador debajo de la plataforma y detenemos su salto
    elif self.speed_y < 0:
        self.rect.top = platform.rect.bottom
        self.speed_y = 0

# Aplicamos la gravedad al jugador, aumentando su velocidad en el eje y
self.speed_y += 0.5

# Comprobamos si el jugador ha salido de los límites de la pantalla
if self.rect.left < 0:
    # Si ha salido por la izquierda, lo colocamos en el borde izquierdo
    self.rect.left = 0
if self.rect.right > 800:
    # Si ha salido por la derecha, lo colocamos en el borde derecho
    self.rect.right = 800
if self.rect.top < 0:
    # Si ha salido por arriba, lo colocamos en el borde superior
    self.rect.top = 0
if self.rect.bottom > 600:
    # Si ha salido por abajo, lo colocamos en el borde inferior y detenemos su caída
    self.rect.bottom = 600
    self.speed_y = 0


# Definimos un método para que el jugador salte
def jump(self):
    # Comprobamos si el jugador está sobre alguna plataforma
    self.rect.y += 2  # Movemos al jugador un poco hacia abajo para facilitar la detección de colisiones
    platform_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
    self.rect.y -= 2  # Movemos al jugador a su posición original


# Si el jugador está sobre alguna plataforma, puede saltar
if platform_hit_list:
  # Establecemos una velocidad negativa en el eje y para que el jugador suba
  self.speed_y = -15
  # Reproducimos el sonido de salto
  jump_sound.play()


# Definimos una clase para representar a las plataformas
class Platform(pygame.sprite.Sprite):
    # Definimos el constructor de la clase
    def __init__(self, x, y, width, height):
        # Llamamos al constructor de la clase padre (pygame.sprite.Sprite)
        super().__init__()
        # Creamos una imagen vacía del tamaño indicado por los parámetros width y height
        self.image = pygame.Surface([width, height])
        # Rellenamos la imagen con el color verde
        self.image.fill(GREEN)
        # Obtenemos el rectángulo que contiene a la imagen
        self.rect = self.image.get_rect()
        # Establecemos la posición inicial de la plataforma según los parámetros x e y
        self.rect.x = x
        self.rect.y = y


# Definimos una clase para representar a los enemigos
class Enemy(pygame.sprite.Sprite):
    # Definimos el constructor de la clase
    def __init__(self, x, y):
        # Llamamos al constructor de la clase padre (pygame.sprite.Sprite)
        super().__init__()
        # Cargamos la imagen del enemigo
        self.image = load_image("enemy.png")
        # Obtenemos el rectángulo que contiene a la imagen
        self.rect = self.image.get_rect()
        # Establecemos la posición inicial del enemigo según los parámetros x e y
        self.rect.x = x
        self.rect.y = y

# Definimos un método para actualizar el estado del enemigo
def update(self):
    # Movemos al enemigo hacia la izquierda a una velocidad constante
    self.rect.x -= 5

# Definimos una función para crear los niveles del juego
def create_level(level):
    # Creamos unas listas vacías para almacenar las plataformas y los enemigos del nivel actual
    platform_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()

    # Si el nivel es el 1
    if level == 1:
        # Creamos unas plataformas con sus coordenadas y tamaños
        platform1 = Platform(0, 550, 800, 50)
        platform2 = Platform(100, 450, 100, 20)
        platform3 = Platform(300, 350, 100, 20)
        platform4 = Platform(500, 250, 100, 20)
        platform5 = Platform(700, 150, 100, 20)

        # Añadimos las plataformas a la lista de plataformas
        platform_list.add(platform1)
        platform_list.add(platform2)
        platform_list.add(platform3)
        platform_list.add(platform4)
        platform_list.add(platform5)

        # Creamos unos enemigos con sus coordenadas
        enemy1 = Enemy(800, 500)
        enemy2 = Enemy(900, 400)
        enemy3 = Enemy(1000, 300)

        # Añadimos los enemigos a la lista de enemigos
        enemy_list.add(enemy1)
        enemy_list.add(enemy2)
        enemy_list.add(enemy3)

    # Devolvemos las listas de plataformas y enemigos del nivel actual
    return platform_list, enemy_list


# Creamos una variable para controlar el bucle principal del juego
running = True

# Creamos una variable para almacenar el nivel actual del juego (solo uno para este ejercicio)
level = 1

# Creamos unas variables para almacenar las listas de plataformas y enemigos del nivel actual
platform_list, enemy_list = create_level(level)

# Creamos un grupo de sprites que contiene al jugador, las plataformas y los enemigos
sprite_list = pygame.sprite.Group()
sprite_list.add(player)
sprite_list.add(platform_list)
sprite_list.add(enemy_list)

# Creamos unas variables para almacenar si el jugador ha ganado o perdido el juego
win = False
lose = False

# Bucle principal del juego
while running:
    # Limpiamos la pantalla con el color blanco
    screen.fill(WHITE)

    # Dibujamos todos los sprites en la pantalla
    sprite_list.draw(screen)

    # Actualizamos todos los sprites
    sprite_list.update()

# Procesamos los eventos que ocurren en el juego
for event in pygame.event.get():
    # Si el usuario cierra la ventana, salimos del bucle
    if event.type == pygame.QUIT:
        running = False
    # Si el usuario presiona una tecla
    if event.type == pygame.KEYDOWN:
        # Si la tecla es la flecha izquierda, movemos al jugador hacia la izquierda
        if event.key == pygame.K_LEFT:
            player.speed_x = -5
        # Si la tecla es la flecha derecha, movemos al jugador hacia la derecha
        if event.key == pygame.K_RIGHT:
            player.speed_x = 5
        # Si la tecla es la barra espaciadora, hacemos que el jugador salte
        if event.key == pygame.K_SPACE:
            player.jump()
    # Si el usuario suelta una tecla
    if event.type == pygame.KEYUP:
        # Si la tecla es la flecha izquierda o derecha, detenemos el movimiento horizontal del jugador
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player.speed_x = 0

# Comprobamos si el jugador ha chocado con algún enemigo
enemy_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
# Si ha chocado con algún enemigo, indicamos que el jugador ha perdido el juego y reproducimos el sonido de derrota
if len(enemy_hit_list) > 0:
    lose = True
    lose_sound.play()

# Comprobamos si el jugador ha llegado al final del nivel (el último círculo de la derecha)
if player.rect.x > 750 and player.rect.y < 100:
    # Si ha llegado al final del nivel, aumentamos el nivel en uno y creamos las nuevas listas de plataformas y enemigos
    level += 1
    platform_list, enemy_list = create_level(level)
    # Si no hay más niveles, indicamos que el jugador ha ganado el juego y reproducimos el sonido de victoria
    if platform_list is None and enemy_list is None:
        win = True
        win_sound.play()
    # Si hay más niveles, vaciamos el grupo de sprites y lo volvemos a llenar con el jugador, las plataformas y los enemigos del nuevo nivel
    else:
        sprite_list.empty()
        sprite_list.add(player)
        sprite_list.add(platform_list)
        sprite_list.add(enemy_list)
    # Colocamos al jugador en la posición inicial del nuevo nivel
    player.rect.x = 50
    player.rect.y = 500


# Si el jugador ha ganado o perdido el juego, mostramos un mensaje en la pantalla y detenemos el bucle principal del juego
if win:
    show_message("¡Has ganado! Felicidades.")
    running = False
if lose:
    show_message("Has perdido. Inténtalo de nuevo.")
    running = False

# Actualizamos la pantalla con lo que hemos dibujado
pygame.display.flip()

# Salimos de pygame y terminamos el juego
pygame.quit()
