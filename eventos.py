from random import randint

import var, pygame, sys


class Movimientos():
    def MovimientoFondo():
        """ESTO GENERA EL MOVIMIENTO EN BUCLE DEL FONDO"""

        var.x_fondo -= var.velocidad
        if var.x_fondo < -((var.window_width / 2)):
            var.x_fondo = 0
        var.screen.blit(var.fondo, (var.x_fondo, 0))

    def MovimientoCoche():

        key = pygame.key.get_pressed()

        if (key[pygame.K_a] or key[pygame.K_LEFT]) and var.cx > 50:
            var.cx -= var.velocidad
            var.mov = True
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and var.cx < (var.window_width - 250):
            var.cx += var.velocidad
            var.mov = True
        if (key[pygame.K_w] or key[pygame.K_UP]) and var.cy > 50:
            var.cy -= var.velocidad
            var.mov = True
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and var.cy < (var.window_height - 150):
            var.cy += var.velocidad
            var.mov = True
        if var.mov == True:
            var.screen.blit(var.coche[1], (int(var.cx), int(var.cy)))
        else:
            var.screen.blit(var.coche[0], (int(var.cx), int(var.cy)))

        var.mov = False
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
