from random import randint

import pygame, var, sys, eventos, conexion, menu,puntuaciones

from pygame.locals import *


class Coche(pygame.sprite.Sprite):
    # Definimos el objeto coche

    def __init__(self):
        super().__init__()
        self.image = var.coche[0]
        self.rect = self.image.get_rect()
        self.rect.y = var.cy
        self.rect.x = var.cx

    def update(self):
        # Definimos el movimiento del coche
        key = pygame.key.get_pressed()

        if (key[pygame.K_a] or key[pygame.K_LEFT]) and self.rect.x > 50:
            self.rect.x -= var.velocidad
            var.mov = True
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.rect.x < (var.window_width - 250):
            self.rect.x += var.velocidad
            var.mov = True
        if (key[pygame.K_w] or key[pygame.K_UP]) and self.rect.y > 50:
            self.rect.y -= var.velocidad
            var.mov = True
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and self.rect.y < (var.window_height - 150):
            self.rect.y += var.velocidad
            var.mov = True
        if var.mov == True:
            self.image = var.coche[1]
        else:
            self.image = var.coche[0]
        var.mov = False


class cocheContrario(pygame.sprite.Sprite):
    # Definimos el objeto cocheContrario

    def __init__(self):
        super().__init__()
        b = randint(0, 5)
        # Cargamos una imagen de coche aleatoria
        if b == 0:
            self.image = var.coche2[0]
        if b == 1:
            self.image = var.coche2[1]
        if b == 2:
            self.image = var.coche2[2]
        if b == 3:
            self.image = var.coche2[3]
        if b == 4:
            self.image = var.coche2[4]
        if b == 5:
            self.image = var.coche2[5]
        self.rect = self.image.get_rect()

        y = randint(1, 4)
        while y == var.carril:
            if y == var.carril:
                y = randint(1, 4)
        var.carril = y

        if y == 1:
            self.rect.y = randint(var.window_height // 4 - (var.window_height // 5),
                                  var.window_height // 4 - (var.window_height // 10))
        elif y == 2:
            self.rect.y = randint(var.window_height // 4, var.window_height // 4 + (var.window_height // 8))
        elif y == 3:
            self.rect.y = randint(var.window_height // 2, var.window_height // 2 * 1.3)
        elif y == 4:
            self.rect.y = randint(var.window_height - (var.window_height // 4),
                                  var.window_height - (var.window_height // 8))
        self.rect.x = var.window_width + 250
        self.velocidad = randint(var.velocidad_max-2, var.velocidad_max)

    def update(self):
        # Generamos el movimiento del objeto
        self.rect.x -= var.velocidad + self.velocidad
        if self.rect.x < -250:
            self.kill()


# Iniciamos pygame
pygame.init()
pygame.display.set_caption("Drunk Driver")
conexion.Conexion.db_connect(var.base)
reloj = pygame.time.Clock()
key = pygame.key.get_pressed()
while True:
    if var.ce==0:
        # agregamos el coche que controlamos al grupo de sprites
        cochePrincipal = pygame.sprite.Group()
        coche = Coche()
        cochePrincipal.add(coche)
        # agregamos los coches en direccion contraria al grupo de sprites
        enemigos = pygame.sprite.Group()
        cochesCon = cocheContrario()
        enemigos.add(cochesCon)
        var.ce+=1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('salir')
            pygame.quit()
            sys.exit()



    if var.jugando == True:
        if var.musica == 1:
            # agregamos la musica con un bucle infinito al iniciar pygame
            pygame.mixer.music.load('res/Wild West Coast Racing.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
            var.musica = 0
        # Definimos los FPS del juego
        reloj.tick(var.fps)
        #guardamos en la variable tiempo los segundos que pasa el programa en ejecucion
        tiempo=(pygame.time.get_ticks()-var.segundos_actuales)/1000

        if tiempo > var.segundos:
            # Cada vez que la variable tiempo es mayor que los segundos establecidos, se genera un coche nuevo y se incrementa el contador de tiempo en 1
            cochesCon = cocheContrario()
            enemigos.add(cochesCon)
            var.segundos_actuales=pygame.time.get_ticks()
            var.contador_tiempo += 1
            if var.segundos > 0.5:  # 0.5 es la velocidad minima para la generacion de los coches
                if var.contador_tiempo >= var.seg:
                    # Cada vez que el contador tiempo es mayor que 4 se resta 0,1 a la variable segundos por lo que el tiempo de regeneracion de los coches disminuye
                    var.segundos -= 0.1
                    #var.seg=var.seg+2.5
                    var.contador_tiempo = 0
                    print("segundos" + str(var.segundos))
        # Creamos otro temporizador para que cada x segundos aumente la melocidad maxima de los coches
        var.temporizador2 += 1
        tiempo2 = (pygame.time.get_ticks()-var.segundos_velocidad)/1000
        if tiempo2 >= 1:
            # Incrementamos el contador de velocidad cada segundo de ejecucion
            var.contador_velocidad += 1
            var.segundos_velocidad=pygame.time.get_ticks()
            if var.contador_velocidad > 20:
                # Al pasar 20 segundos se incrementa la velocidad en 0.5
                var.contador_velocidad = 0
                if var.velocidad_max <= 5:
                    print(var.velocidad)
                    if var.velocidad <4:
                        var.velocidad+=0.5
                    var.velocidad_max += 1

        eventos.Movimientos.Salir()
        eventos.Movimientos.AtrasMenu()
        if var.chocar == False:
            eventos.Movimientos.MovimientoFondo()
            # Dibujamos los sprites y hacemos los updates de los mismos
            enemigos.update()
            enemigos.draw(var.screen)
            cochePrincipal.update()
            cochePrincipal.draw(var.screen)
            eventos.Movimientos.marcador()
            # Generamos las colisiones entre los sprites
            colision = pygame.sprite.spritecollide(coche, enemigos, False)



            # Al colisionar se cambia la velocidad a 0 por lo que no hay movimiento

            if colision:
                var.velocidad = 0
                eventos.Movimientos.mensajeChocar()
                conexion.Conexion.guardarPuntuacion()
                var.chocar = True
                var.jugando = False
                var.menu=False
                var.puntuaciones=True
                var.botones=0
                pygame.mixer.music.stop()
        pygame.display.update()

    if var.menu==True:
        menu.menu()
    else:
        puntuaciones.puntuaciones()