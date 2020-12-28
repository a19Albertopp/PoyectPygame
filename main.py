from random import randint

import pygame, var, sys, eventos


class cocheContrario(pygame.sprite.Sprite):
    # Definimos el objeto cocheContrario

    def __init__(self):
        super().__init__()
        b = randint(0, 1)
        #Cargamos una imagen de coche aleatoria
        if b == 1:
            self.image = var.coche2[0]
            b = 0
        else:
            self.image = var.coche2[1]
            b += 1
        self.rect = self.image.get_rect()
        #
        y = randint(1, 4)
        if y == 1:
            self.rect.y = var.window_height // 4 - 220
            print(y)
        elif y == 2:
            self.rect.y = var.window_height // 2 - 220
            print(y)
        elif y == 3:
            self.rect.y = var.window_height // 4 + var.window_height // 4 * 2 - 220
            print(y)
        elif y == 4:
            self.rect.y = var.window_height - 220
            print(y)

        self.rect.x = var.window_width - 250

    def update(self):
        # Generamos el movimiento del objeto
        self.rect.x -= var.velocidad
        if self.rect.x < -250:
            self.kill()


# Iniciamos pygame
pygame.init()
pygame.display.set_caption("Drunk Driver")
# agregamos los coches en direccion contraria al grupo de sprites
sprites = pygame.sprite.Group()
coches = cocheContrario()
sprites.add(coches)

while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if var.musica == 1:
        pygame.mixer.music.load('res/Wild West Coast Racing.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        var.musica = 0

    eventos.Movimientos.MovimientoFondo()
    sprites.update()
    sprites.draw(var.screen)
    eventos.Movimientos.MovimientoCoche()
    eventos.Movimientos.marcador()

    pygame.display.update()
