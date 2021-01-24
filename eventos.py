from random import randint

import var, pygame, sys


class Movimientos():
    def MovimientoFondo():
        """ESTO GENERA EL MOVIMIENTO EN BUCLE DEL FONDO"""

        var.x_fondo -= var.velocidad
        if var.x_fondo < -((var.window_width / 2) + 185):
            var.x_fondo = 0
        var.screen.blit(var.fondo, (var.x_fondo, 0))

    def Salir():
        # Definimos que al pulsar escape se cierre el juego
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def AtrasMenu():
        # Definimos que al pulsar escape se cierre el juego
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            pygame.mixer.music.stop()
            var.jugando=False
            var.menu=True

    def marcador():
        # La puntuacion es un autoincrementable que crece indefinidamente
        fuente = pygame.font.SysFont("serif", 30)
        var.puntos += 1
        # definimos como se van a mostrar los puntos
        mensaje = fuente.render("Puntos: " + str(var.puntos), True, (0, 0, 0))
        var.screen.blit(mensaje, (var.window_width - 200, +30))

    def mensajeChocar():
        fuente = pygame.font.SysFont("serif", 100)
        mensajeChocar = fuente.render("HAS CHOCADO", True, (0, 0, 0))
        var.screen.blit(mensajeChocar, (var.window_width // 4, var.window_height // 2))

