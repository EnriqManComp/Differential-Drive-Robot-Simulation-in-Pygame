import pygame
import math

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)

# Definir dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Definir parámetros del LIDAR
NUM_PUNTOS = 360               # Número de puntos a escanear
DISTANCIA_MAX = 300            # Distancia máxima de escaneo

# Clase para el robot
class Robot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación de LIDAR")

# Función para dibujar la simulación del LIDAR
def dibujar_lidar(surface, origen):
    for i in range(NUM_PUNTOS):
        angulo = math.radians(i)  # Convertir a radianes
        x_destino = origen[0] + DISTANCIA_MAX * math.cos(angulo)
        y_destino = origen[1] + DISTANCIA_MAX * math.sin(angulo)
        pygame.draw.line(surface, VERDE, origen, (x_destino, y_destino))

# Crear un robot
robot = Robot(ANCHO // 2, ALTO // 2)

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Limpiar pantalla
    pantalla.fill(NEGRO)

    # Dibujar el robot
    pantalla.blit(robot.image, robot.rect)

    # Obtener posición del robot
    origen_lidar = (robot.rect.centerx, robot.rect.top)

    # Dibujar la simulación del LIDAR
    dibujar_lidar(pantalla, origen_lidar)

    # Actualizar la pantalla
    pygame.display.flip()

    # Control de la frecuencia de actualización
    pygame.time.Clock().tick(30)

# Salir de Pygame
pygame.quit()
