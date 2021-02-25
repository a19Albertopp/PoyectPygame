import sys

import pygame, var, eventos

from pygame.locals import *

reloj = pygame.time.Clock()


# Crear un sprite de botones y en el update comparar la posicion de los botones con el mause y si clicka que haga el evento

class Boton(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = var.boton_1
        self.rect = self.image.get_rect()
        if var.botones == 0:
            self.image = var.boton_1
            self.rect.y = var.window_height / 2 - 200
            self.rect.x = var.window_width / 2 - 200
        if var.botones == 1:
            self.image = var.boton_2
            self.rect.y = var.window_height / 2 + 200
            self.rect.x = var.window_width / 2 - 200
        if var.botones == 2:
            self.image = var.boton_3
            self.rect.y = var.window_height / 3.7
            self.rect.x = var.window_width / 13
        if var.botones == 3:
            self.image = var.boton_puntuaciones
            self.rect.y = var.window_height / 2
            self.rect.x = var.window_width / 2 - 200
        self.boton = var.botones

    def update(self, mx, my):
        if self.rect.collidepoint(mx, my):
            if self.boton == 0:
                if var.jugador == "ESCRIBE TU NOMBRE":
                    var.aviso = True
                else:
                    print('jugar')
                    ini()
            if self.boton == 1:
                print('salir')
                pygame.quit()
                sys.exit()
            if self.boton == 2:
                if (var.jugador == "ESCRIBE TU NOMBRE"):
                    var.jugador = ""
                var.escribiendo = True
            if self.boton == 3:
                print('puntuaciones')
                var.menu = False
                var.botones = 0
                var.puntuaciones = True
                var.aviso = False


def ini():
    var.chocar = False
    var.mov = False
    var.musica = 1
    var.velocidad = 3
    var.x_fondo = 0
    var.puntos = 0
    var.cx = var.window_width * 0.1
    var.cy = var.window_height * 0.35
    var.fps = 144
    var.contador_tiempo = 0
    var.contador_velocidad = 0
    var.velocidad_max = 3
    var.segundos = 1
    var.carril = 0
    # Se inician los contadores de tiempo
    var.tiempo_inicial = pygame.time.get_ticks()
    var.segundos_actuales = pygame.time.get_ticks()
    var.segundos_velocidad = pygame.time.get_ticks()
    var.jugando = True
    var.menu = False
    var.puntuaciones = False
    var.sprites_iniciales = 0
    var.aviso = False
    Botones.remove()


Botones = pygame.sprite.Group()


def menu():
    while var.menu == True:
        eventos.Movimientos.Salir()
        font = pygame.font.SysFont("serif", 35)
        font2 = pygame.font.SysFont("serif", 35, bold=True)
        var.screen.blit(var.fondo_menu, (0, 0))

        while var.botones <= 3:
            boton = Boton()
            Botones.add(boton)
            var.botones += 1
        mx, my = pygame.mouse.get_pos()
        Botones.draw(var.screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if var.escribiendo == False:

                    if event.key == K_p:
                        var.menu = False
                        var.puntuaciones = True
                    if event.key == K_RETURN:
                        if var.jugador == "ESCRIBE TU NOMBRE":
                            var.aviso = True
                        else:
                            ini()
                    if event.key == K_n:
                        var.jugador = ""
                        var.escribiendo2 = True
                if event.key == K_RETURN:
                    var.escribiendo = False
            if event.type == MOUSEBUTTONDOWN:
                var.escribiendo = False
                if var.jugador == "":
                    var.jugador = "ESCRIBE TU NOMBRE"
                Botones.update(mx, my)

            if var.escribiendo:
                var.escribiendo2 = False
                if event.type == KEYDOWN:  # para el editText

                    var.jugador += event.unicode

                key = pygame.key.get_pressed()
                if key[pygame.K_BACKSPACE]:
                    var.jugador = var.jugador[:-2]

        if var.escribiendo2 == True:
            var.escribiendo = True
        texto = font.render(var.jugador, True, (255, 0, 0))  # editText
        var.screen.blit(texto, (var.window_width / 13, var.window_height / 3.7))
        if var.aviso == True:
            texto2 = font2.render("ESCRIBE UN NOMBRE!!!", True, (255, 0, 0))
            var.screen.blit(texto2, (var.window_width / 2.5, var.window_height / 2.35))
        texto3 = font2.render("CONTROLES", True, (255, 0, 0))
        var.screen.blit(texto3, (var.window_width - var.window_width / 4.5, var.window_height / 3.5))
        # texto4 = font2.render("M -> MENU", True, (255, 0, 0))
        # texto5 = font2.render("J -> JUGAR", True, (255, 0, 0))
        # texto6 = font2.render("P -> PUNTUACIONES", True, (255, 0, 0))
        # texto7 = font2.render("ESC -> SALIR", True, (255, 0, 0))
        # var.screen.blit(texto4, (var.window_width - var.window_width / 4.8, var.window_height / 1.9))
        # var.screen.blit(texto5, (var.window_width - var.window_width / 4.8, var.window_height / 1.75))
        # var.screen.blit(texto6, (var.window_width - var.window_width / 4.1, var.window_height / 1.6))
        # var.screen.blit(texto7, (var.window_width - var.window_width / 4.8, var.window_height / 1.48))

        var.screen.blit(var.awsd, (var.window_width - var.window_width / 6.5, var.window_height / 2.75))
        var.screen.blit(var.awsd_arrow, (var.window_width - var.window_width / 3.5, var.window_height / 2.75))

        pygame.display.update()
        reloj.tick(var.fps)
