from win32api import GetSystemMetrics
import pygame

window_height=GetSystemMetrics(1)
window_width=GetSystemMetrics(0)
screen=pygame.display.set_mode((window_width, window_height))
fondo=pygame.image.load('img/carretera2.png').convert()
coche=[pygame.image.load('img/coche2.png'),
        pygame.image.load('img/coche3.png')]
mov=False
velocidad=1.5
x_fondo=0
puntos=0
cx=window_width*0.1
cy=window_height*0.35

