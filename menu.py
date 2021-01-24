import sys

import pygame, var

from pygame.locals import *

reloj = pygame.time.Clock()

#Crear un sprite de botones y en el update comparar la posicion de los botones con el mause y si clicka que haga el evento

class Boton(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = var.boton_1
        self.rect = self.image.get_rect()
        if var.botones==0:
            self.image = var.boton_1
            print('boton 1')
            self.rect.y = var.window_height/2-200
            self.rect.x = var.window_width/2-200
        self.boton=var.botones
        if var.botones==1:
            print('boton 2')
            self.image = var.boton_2
            self.rect.y = var.window_height/2
            self.rect.x = var.window_width/2-200
        self.boton=var.botones

    def update(self,mx,my):
        if self.rect.collidepoint(mx,my):
            if self.boton==0:
                ini()
            if self.boton==1:
                pygame.quit()
                sys.exit()
            if self.boton==2:
                pass
            if self.boton==3:
                pass



# def Texto(text, font, color, surface, x, y):
#      textobj = font.render(text, 1, color)
#      textrect = textobj.get_rect()
#      textrect.topleft = (x, y)
#      surface.blit(textobj, textrect)

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
    var.temporizador = 0
    var.temporizador2 = 0
    var.contador_tiempo = 0
    var.contador_velocidad = 0
    var.velocidad_max = 3
    var.segundos = 1.5
    var.carril = 0
    var.jugando = True
    var.menu = False
    var.ce = 0

Botones=pygame.sprite.Group()
def menu():

    while var.menu == True:
        font = pygame.font.SysFont("serif", 35)
        var.screen.blit(var.fondo_menu, (0, 0))

        #texto=font.render(var.jugador,True,(255,0,0)) editText
        #var.screen.blit(texto,(0,0))
        while var.botones<=1:

            boton=Boton()
            Botones.add(boton)
            var.botones+=1
        mx,my = pygame.mouse.get_pos()
        Botones.draw(var.screen)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                Botones.update(mx,my)
                if event.button == 1:
                    pass
            #if event.type==KEYDOWN: para el editText
                #var.jugador+=event.unicode
        pygame.display.update()
        reloj.tick(var.fps)