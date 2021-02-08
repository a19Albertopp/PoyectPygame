import sys

import pygame, var, menu, conexion

from pygame.locals import *

reloj = pygame.time.Clock()


# Crear un sprite de botones y en el update comparar la posicion de los botones con el mause y si clicka que haga el evento

class Bot(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = var.boton_1
        self.rect = self.image.get_rect()
        if var.botones == 0:
            self.image = var.boton_1
            self.rect.y = var.window_height - var.window_height / 6
            self.rect.x = var.window_width / 7
        if var.botones == 1:
            self.image = var.boton_2
            self.rect.y = var.window_height - var.window_height / 6
            self.rect.x = var.window_width - var.window_width / 3
        if var.botones == 2:
            self.image = var.boton_menu
            self.rect.y = var.window_height - var.window_height / 6
            self.rect.x = var.window_width - var.window_width / 1.65
        self.boton = var.botones

    def update(self, mx, my):
        if self.rect.collidepoint(mx, my):
            if self.boton == 0:
                print('JUGAR')
                var.botones = 0
                menu.ini()
            if self.boton == 1:
                print('Salir')
                pygame.quit()
                sys.exit()
            if self.boton == 2:
                print('menu')
                var.puntuaciones=False
                var.menu=True





def Texto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

Btn = pygame.sprite.Group()
def puntuaciones():

    while var.puntuaciones == True:
        var.screen.blit(var.fondo_puntuaciones, (0, 0))
        font = pygame.font.SysFont("serif", 40, bold=True)
        while var.botones <= 2:
            boton = Bot()
            Btn.add(boton)
            var.botones += 1
        mx, my = pygame.mouse.get_pos()
        Btn.draw(var.screen)
        texto = font.render(str(var.puntos), True, (255, 0, 0))
        var.screen.blit(texto, (var.window_width / 2.1, var.window_height / 4.5))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                Btn.update(mx, my)
        conexion.Conexion.puntuacionGlobal()
        conexion.Conexion.puntuacionPersonal()

        pygame.display.update()
        reloj.tick(var.fps)


def escribirPuntGlob(datos, x, y):
    font = pygame.font.SysFont("serif", 20, bold=True)
    if var.contador_puntuacion_global < 10:
        texto = font.render(datos[0], True, (255, 0, 0))
        var.screen.blit(texto, (x, y))
        texto = font.render(datos[1], True, (255, 0, 0))
        var.screen.blit(texto, (x + var.window_width / 20, y))
        texto = font.render(datos[2], True, (255, 0, 0))
        var.screen.blit(texto, (x + + var.window_width / 22 * 3.5, y))
        texto = font.render(datos[3], True, (255, 0, 0))
        var.screen.blit(texto, (x + + var.window_width / 22 * 5.5, y))


def escribirPuntPers(datos, x, y):
    font = pygame.font.SysFont("serif", 20, bold=True)
    if var.contador_puntuacion_personal < 10:
        texto = font.render(datos[0], True, (255, 0, 0))
        var.screen.blit(texto, (x, y))
        texto = font.render(datos[1], True, (255, 0, 0))
        var.screen.blit(texto, (x + var.window_width / 20, y))
        texto = font.render(datos[2], True, (255, 0, 0))
        var.screen.blit(texto, (x + var.window_width / 22 * 3.3, y))
        texto = font.render(datos[3], True, (255, 0, 0))
        var.screen.blit(texto, (x + var.window_width / 22 * 5.3, y))
