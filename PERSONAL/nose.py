import pygame
import random

# Inicializar pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Configuración de la ventana
ANCHO = 400
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Flappy Bird")

# Configuración del pájaro
PÁJARO_ANCHO = 28
PÁJARO_ALTO = 28
gravedad = 0.8
salto = -12

# Configuración de las tuberías
TUBERÍA_ANCHO = 60
TUBERÍA_ALTURA = 400
DISTANCIA_TUBERÍAS = 235
VEL_TUBERÍAS = 5

# Definir la clase para el pájaro
class Pajaro:
    def __init__(self):
        self.x = 50
        self.y = ALTO // 2
        self.velocidad_y = 0
        self.imagen = pygame.Surface((PÁJARO_ANCHO, PÁJARO_ALTO))
        self.imagen.fill(ROJO)

    def saltar(self):
        self.velocidad_y = salto

    def mover(self):
        self.velocidad_y += gravedad
        self.y += self.velocidad_y

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

# Definir la clase para las tuberías
class Tubería:
    def __init__(self):
        self.x = ANCHO
        self.altura = random.randint(100, ALTO - 100)
        self.velocidad_x = VEL_TUBERÍAS
        self.espacio = 150

    def mover(self):
        self.x -= self.velocidad_x

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, VERDE, (self.x, 0, TUBERÍA_ANCHO, self.altura))
        pygame.draw.rect(pantalla, VERDE, (self.x, self.altura + self.espacio, TUBERÍA_ANCHO, ALTO))

    def colisiona_con_pajaro(self, pajaro):
        if self.x < pajaro.x + PÁJARO_ANCHO and self.x + TUBERÍA_ANCHO > pajaro.x:
            if pajaro.y < self.altura or pajaro.y + PÁJARO_ALTO > self.altura + self.espacio:
                return True
        return False

# Función para mostrar el mensaje de "Game Over"
def mostrar_game_over(puntaje):
    fuente = pygame.font.SysFont("Arial", 30)
    texto_game_over = fuente.render("Game Over", True, BLANCO)
    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    texto_reintentar = fuente.render("Presiona 'R' para reintentar", True, BLANCO)

    pantalla.fill(NEGRO)
    pantalla.blit(texto_game_over, (ANCHO // 2 - texto_game_over.get_width() // 2, ALTO // 4))
    pantalla.blit(texto_puntaje, (ANCHO // 2 - texto_puntaje.get_width() // 2, ALTO // 2))
    pantalla.blit(texto_reintentar, (ANCHO // 2 - texto_reintentar.get_width() // 2, ALTO // 1.5))
    pygame.display.flip()

# Función principal del juego
def juego():
    reloj = pygame.time.Clock()
    pajaro = Pajaro()
    tuberias = [Tubería()]
    puntaje = 0
    corriendo = True
    while corriendo:
        pantalla.fill(AZUL)

        # Comprobar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pajaro.saltar()

        # Mover el pájaro y las tuberías
        pajaro.mover()
        for tuberia in tuberias:
            tuberia.mover()

        # Crear nuevas tuberías
        if tuberias[-1].x < ANCHO - DISTANCIA_TUBERÍAS:
            tuberias.append(Tubería())

        # Eliminar tuberías que se han ido de la pantalla
        if tuberias[0].x < -TUBERÍA_ANCHO:
            tuberias.pop(0)
            puntaje += 1

        # Comprobar colisiones con las tuberías o el suelo
        if pajaro.y > ALTO - PÁJARO_ALTO or pajaro.y < 0:
            mostrar_game_over(puntaje)
            while True:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        corriendo = False
                        pygame.quit()
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:  # Reiniciar el juego
                            juego()
                            return

        for tuberia in tuberias:
            if tuberia.colisiona_con_pajaro(pajaro):
                mostrar_game_over(puntaje)
                while True:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            corriendo = False
                            pygame.quit()
                        if evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_r:  # Reiniciar el juego
                                juego()
                                return

        # Dibujar todo en la pantalla
        pajaro.dibujar(pantalla)
        for tuberia in tuberias:
            tuberia.dibujar(pantalla)

        # Mostrar puntaje
        fuente = pygame.font.SysFont("Arial", 30)
        texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
        pantalla.blit(texto, (10, 10))

        # Actualizar pantalla
        pygame.display.flip()

        # Controlar FPS
        reloj.tick(25)

    pygame.quit()

# Iniciar el juego
juego()