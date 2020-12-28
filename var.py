from win32api import GetSystemMetrics
import pygame

window_height=GetSystemMetrics(1)
window_width=GetSystemMetrics(0)
screen=pygame.display.set_mode((window_width, window_height))
fondo=pygame.image.load('res/carretera2.png').convert()
coche=[pygame.image.load('res/coche2.png'),
        pygame.image.load('res/coche3.png')]
coche2=[pygame.image.load('res/spr_van_0.png'),
        pygame.image.load('res/spr_car4_0.png')]
mov=False
musica=1
velocidad=1.5
x_fondo=0
puntos=0
cx=window_width*0.1
cy=window_height*0.35
# "Wild West Coast Racing" by Eric Matyas soundimage.org
