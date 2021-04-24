import pygame
import random
pygame.init()


ancho=800
alto=600
blanco=(255,255,255)
negro=(0,0,0)
verde=(0,255,0)
azul=(0,0,255)
rojo=(255,0,0)
jugando=True


x1=100
y1=100
volver=True
FPS=5
velx=0
vely=0
velocidad=2
y2=300
x2=0
anchonave=50
altonave=50
anchoaste=50
altoaste=50
anchoaste2=50
altoaste2=50
x3=750
y3=175
x4=random.randint(0,750)
y4=random.randint(0,550)
anchocomi=50
altocomi=50
x5=300
y5=0
anchoaste3=50
altoaste3=50
puntos=0
# Ventana
ventana=pygame.display.set_mode((ancho,alto))
# Bucle principal


# Eventos
jugando=True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
            if event.key == pygame.K_a:
                velx -= velocidad
            if event.key == pygame.K_d:
                velx += velocidad
            if event.key == pygame.K_w:
                vely -= velocidad
            if event.key == pygame.K_s:
                vely += velocidad

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                velx =0
            if event.key == pygame.K_d:
                velx =0
            if event.key == pygame.K_w:
                vely =0
            if event.key == pygame.K_s:
                vely =0

    if x1 >= 750:
        x1=750
    if x1 <= 0:
        x1=0
    if y1 >= 550:
        y1=550
    if y1 <= 0:
        y1=0
    x1 += velx
    y1 += vely

    # Dibujos
    ventana.fill(negro)
    fuente = pygame.font.SysFont("consolas", 30)
    texto = fuente.render("Puntaje: " + str(puntos), True, blanco)
    #texto2 =fuente.render("0", True, blanco)
    # Nave
    pygame.draw.rect(ventana, rojo, (x1, y1, anchonave, altonave))

    # Cuadrado 1
    x2+=2
    if x2==800:
        x2=-50
        y2 = random.randint(0, 550)
    pygame.draw.rect(ventana, verde, (x2, y2, anchoaste, altoaste))
    if x2 + anchoaste > x1 and \
        x2 < x1 + anchonave and \
        y2 + altonave > y1 and \
        y2 < y1 + altonave:
        pygame.time.delay(1000)
        puntos = 0
        x1=100
        y1=100
    # Cuadrado 2
    x3 -= 2
    if x3 == -50:
        x3 = 800
        y3 = random.randint(0,550)
    pygame.draw.rect(ventana, verde, (x3, y3, anchoaste2, altoaste2))
    if x3 + anchoaste2 > x1 and \
        x3 < x1 + anchonave and \
        y3 + altonave > y1 and \
        y3 < y1 + altonave:
        pygame.time.delay(1000)
        puntos = 0
        x1 = 100
        y1 = 100
    # Cuadrado 3
    y5 -= 2
    if y5 == -50:
        y5 = 550
        x5 = random.randint(0,750)
    pygame.draw.rect(ventana, verde, (x5, y5, anchoaste3, altoaste3))
    if x5 + anchoaste3 > x1 and \
        x5 < x1 + anchonave and \
        y5 + altonave > y1 and \
        y5 < y1 + altonave:
        pygame.time.delay(1000)
        puntos = 0
        x1 = 100
        y1 = 100
    # Comida
    pygame.draw.rect(ventana, blanco, (x4, y4, anchocomi, altocomi))
    if x4 + anchocomi > x1 and \
            x4 < x1 + anchonave and \
            y4 + altonave > y1 and \
            y4 < y1 + altonave:
        pygame.time.delay(0)
        puntos += 1
        x4 = random.randint(0,750)
        y4 = random.randint(0,550)
    ventana.blit(texto, (10, 10))
    # Actualizar
    pygame.display.update()
    pygame.time.delay(FPS)






# Salir
pygame.quit()