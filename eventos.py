from random import randint
from VenChocar import *
from Ven_Nombre import *
import var, pygame, sys,juego


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


class eventosVentanas():
    def cerrarNombre():
        try:
            var.dlgNombre.show()
            if var.dlgNombre.exec_():
                var.dlgNombre.hide()
        except Exception as error:
            print('Error cerrarNombre: %s' % str(error))

    def ValidarNombre():
        try:
            var.dlgNombre.show()

            juego.Juego.bucle_juego()
            if var.dlgNombre.exec_():
                var.dlgNombre.hide()
        except Exception as error:
            print('Error ValidarNombre: %s' % str(error))
    def abrirNombre():
        try:
            var.dlgNombre.show()
            if var.dlgNombre.exec_():
                var.dlgNombre.hide()
        except Exception as error:
            print('Error abrirNombre: %s' % str(error))
