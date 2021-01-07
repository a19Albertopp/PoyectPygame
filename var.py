from win32api import GetSystemMetrics
import pygame

window_height=GetSystemMetrics(1)
window_width=GetSystemMetrics(0)





screen=pygame.display.set_mode((window_width, window_height))
fondo=pygame.image.load('res/carretera1.png').convert()
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
segundos=2
carril=0
global ui
global dlgNombre
global editNombre
global nombre
base='coches.db'

global window
# "Wild West Coast Racing" by Eric Matyas soundimage.org
