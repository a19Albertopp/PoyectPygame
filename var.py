from win32api import GetSystemMetrics
import pygame

window_height=GetSystemMetrics(1)
window_width=GetSystemMetrics(0)





screen=pygame.display.set_mode((window_width, window_height))
fondo_menu=pygame.image.load('fondo_menu.png').convert()
fondo=pygame.image.load('res/carretera1.png').convert()
boton_1=pygame.image.load('res/boton_1.png').convert()
boton_2=pygame.image.load('res/boton_2.png').convert()
boton_1=pygame.transform.scale(boton_1,(window_width//5,window_height//10))
boton_2=pygame.transform.scale(boton_2,(window_width//5,window_height//10))
boton_1.set_colorkey((0,0,0))
boton_2.set_colorkey((0,0,0))
fondo=pygame.transform.scale(fondo,(window_width*2,window_height))
coche=[pygame.image.load('res/coche2.png'),
        pygame.image.load('res/coche3.png')]
coche2=[pygame.image.load('res/coche_con1.png'),
        pygame.image.load('res/coche_con2.png'),
        pygame.image.load('res/coche_con3.png'),
        pygame.image.load('res/coche_con4.png'),
        pygame.image.load('res/coche_con5.png'),
        pygame.image.load('res/coche_con6.png')]
chocar=False
mov=False
jugando=False
menu=True
musica=1
velocidad=3
x_fondo=0
puntos=0
cx=window_width*0.1
cy=window_height*0.35
fps=144
temporizador=0
temporizador2=0
contador_tiempo=0
contador_velocidad=0
velocidad_max=3
segundos=1.5
carril=0
global ui
global dlgNombre
global editNombre
global nombre
base='coches.db'
botones=0

global window
# "Wild West Coast Racing" by Eric Matyas soundimage.org
jugador=""


ce=0