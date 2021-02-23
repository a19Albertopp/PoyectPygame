from win32api import GetSystemMetrics
import pygame

window_height=GetSystemMetrics(1)
window_width=GetSystemMetrics(0)
import conexion




screen=pygame.display.set_mode((window_width, window_height))
fondo_menu=pygame.image.load(conexion.Conexion.resource_path('res/fondo_menu.png')).convert()
fondo_puntuaciones=pygame.image.load(conexion.Conexion.resource_path('res/fondo_puntuaciones.png')).convert()
fondo=pygame.image.load(conexion.Conexion.resource_path('res/carretera1.png')).convert()
awsd=pygame.image.load(conexion.Conexion.resource_path('res/awsd.png')).convert()
awsd.set_colorkey((255,255,255))
awsd=pygame.transform.scale(awsd,(window_width//9,window_height//9))
awsd_arrow=pygame.image.load(conexion.Conexion.resource_path('res/awsd_arrows.png')).convert()
awsd_arrow.set_colorkey((255,255,255))
awsd_arrow=pygame.transform.scale(awsd_arrow,(window_width//9,window_height//9))
boton_1=pygame.image.load(conexion.Conexion.resource_path('res/boton_1.png')).convert()
boton_1=pygame.transform.scale(boton_1,(window_width//5,window_height//10))
boton_1.set_colorkey((0,0,0))
boton_menu=pygame.image.load(conexion.Conexion.resource_path('res/boton_menu.png')).convert()
boton_menu=pygame.transform.scale(boton_menu,(window_width//5,window_height//10))
boton_menu.set_colorkey((0,0,0))
boton_puntuaciones=pygame.image.load(conexion.Conexion.resource_path('res/boton_puntuaciones.png')).convert()
boton_puntuaciones=pygame.transform.scale(boton_puntuaciones,(window_width//5,window_height//10))
boton_puntuaciones.set_colorkey((0,0,0))
boton_3=pygame.image.load(conexion.Conexion.resource_path('res/boton_nombre.png')).convert()
boton_3.set_colorkey((255,255,255))
boton_2=pygame.image.load(conexion.Conexion.resource_path('res/boton_2.png')).convert()
boton_2=pygame.transform.scale(boton_2,(window_width//5,window_height//10))
boton_2.set_colorkey((0,0,0))
fondo=pygame.transform.scale(fondo,(window_width*2,window_height))
coche=[pygame.image.load(conexion.Conexion.resource_path('res/coche2.png')),
        pygame.image.load(conexion.Conexion.resource_path('res/coche3.png'))]
coche2=[pygame.image.load(conexion.Conexion.resource_path('res/coche_con1.png')),
        pygame.image.load(conexion.Conexion.resource_path('res/coche_con2.png')),
        pygame.image.load(conexion.Conexion.resource_path('res/coche_con3.png')),
        pygame.image.load(conexion.Conexion.resource_path('res/coche_con4.png')),
        pygame.image.load(conexion.Conexion.resource_path('res/coche_con5.png')),
        pygame.image.load(conexion.Conexion.resource_path('res/coche_con6.png'))]
chocar=False
mov=False
jugando=False
menu=True
musica=1
velocidad=4
x_fondo=0
puntos=0
cx=window_width*0.1
cy=window_height*0.35
fps=144
temporizador=0
temporizador2=0
contador_tiempo=0
contador_velocidad=0
velocidad_max=4
segundos=1
carril=0
base='coches.db'
botones=0
seg=10
global window
# "Wild West Coast Racing" by Eric Matyas soundimage.org
jugador="ESCRIBE TU NOMBRE"
escribiendo=False
aviso=False
ce=0

global tiempo_inicial
global segundos_actuales
global segundos_velocidad

puntuaciones=False
contador_puntuacion_global=0
contador_puntuacion_personal=0
recoger_puntG=True