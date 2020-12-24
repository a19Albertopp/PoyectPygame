import pygame,var,sys,eventos
pygame.init()

puntos=0
while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    eventos.Movimientos.MovimientoFondo()
    eventos.Movimientos.MovimientoCoche()
    eventos.Movimientos.marcador()
    pygame.display.update()





