
import pygame, sys
from pygame.locals import *
from random import randint
from time import perf_counter

# importamos las clases que hemos creado
from clases import jugador
from clases import asteroide


# variables 
ANCHO = 480
ALTO = 700
listaAsteroide = []
puntos = 0
colorFuente = (120,200,40)

# booleano para comprobar si estamos jugando
jugando = True

# carga asteroides
def cargarAsteroides(x,y):
    meteoro = asteroide.Asteroide(x,y)
    listaAsteroide.append(meteoro)

def gameOver():
    global jugando
    jugando = False
    for meteoritos in listaAsteroide:
        listaAsteroide.remove(meteoritos)
    
# funcion principal
def meteoritos():
    pygame.init()
    
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    #imagen de fondo
    fondo = pygame.image.load("./imagenes/fondo.png")
    
    # icono
    icono = pygame.image.load("imagenes/icono.png")
    pygame.display.set_icon(icono)
    
    # cargamos el fondo a partir de las coordenadas 0,0. Pero lo cargamos finalmente abajo
    
    # titulo
    pygame.display.set_caption("Meteoritos by M.PADILLA")
    
    # creamos el objeto jugador, importandolo de la clase Nave 
    # y lo llamamos nave para llamar a sus metodos como nave.xxx
    nave = jugador.Nave()
    contador = 0
    
    # sonidos
    pygame.mixer.music.load("sonidos/asteroids.wav")
    pygame.mixer.music.play(3)
    sonidoColision = pygame.mixer.Sound("sonidos/colision.aiff")
    
    # fuente marcador
    fuenteMarcador = pygame.font.SysFont("Consolas", 20)
    
    # while que ejecuta el ciclo del juego
    # mientras sea verdad, actualiza la pantalla.
    # cuando evento de pygame sea QUIT (pulsar en X de cerrar ventana), sale del sistema
    while True:
        
        # cargamos el fondo a partir de las coordenadas 0,0. Lo cargamos aqui por si hay que cargar el juego
        # otra vez, para que se vuelva a dibujar el fondo
        ventana.blit(fondo, (0,0))
        
        # llamamos metodo dibujar de Nave
        nave.dibujar(ventana)
        
        # tiempo
        tiempo = perf_counter()
        
        # marcador . Ponemos PUNTOS como variable global para que funcione en toda la app
        global puntos
        textoMarcador = fuenteMarcador.render("Puntos: "+str(puntos), 0 , colorFuente)
        ventana.blit(textoMarcador, (5,5))
        
        # creamos asteroides
        if tiempo - contador > 1:
            contador = tiempo
            # el intervalo de la coordenada donde se crea asteroide es para que no se salga de la pantalla
            posX = randint(2,478)
            cargarAsteroides(posX, 0)
            
        # comprobamos lista asteroide, si hay asteroides, lo dibujamos y lo movemos (recorrido)
        # si el asteroide esta en posicion 700, lo eliminamos de la lista
        if len(listaAsteroide) > 0:
            for x in listaAsteroide :
                if jugando == True:
                    x.dibujar(ventana)
                    x.recorrido()
                if x.rect.top > 700:
                    listaAsteroide.remove(x)
                else:
                    # si el asteroide colisiona con la nave, ejecutamos funcion gameover
                    if x.rect.colliderect(nave.rect):
                        listaAsteroide.remove(x)
                        sonidoColision.play()
                        nave.vida = False
                        gameOver()
        
        # disparo de misil
        # si el array listadisparo tiene elementos, hacer el disparo
        if len(nave.listaDisparo)>0:
            for x in nave.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                # si el misil llega arriba, quitar ese disparo del array listadisparo
                if x.rect.top < -10:
                    nave.listaDisparo.remove(x)
                else:
                    # aqui hacemos que si el disparo da a un meteorito, el meteorito y el disparo desaparecen
                    for meteoritos in listaAsteroide:
                        if x.rect.colliderect(meteoritos.rect):
                            listaAsteroide.remove(meteoritos)
                            nave.listaDisparo.remove(x)
                            puntos +=1
        nave.mover()
        
        for evento in pygame.event.get():
            
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            # comprobamos si se ha pulsado una tecla    
            elif evento.type == pygame.KEYDOWN:
                if jugando == True:
                    # si la tecla que se ha pulsado es izquierda, voy a izq (movimiento es sumando velocidad)
                    if evento.key == K_LEFT:
                        nave.rect.left-= nave.velocidad
                    elif evento.key == K_RIGHT:
                        nave.rect.right+= nave.velocidad
                    # aqui comprobamos si se pulsa espacio, que haria el disparo
                    elif evento.key == K_SPACE:
                        # aqui detecta posicion de la nave cuando se dispara, para pasarlo a DISPARAR
                        # y que salga de ahi el misil (coordenadas x ,y)
                        # le he restado unos pixeles a posicion, para que el disparo salga centrado
                        xNave,yNave = nave.rect.center
                        y = yNave - 30
                        x = xNave - 5
                        nave.disparar(x,y)
                    
        # variable para cuando termine el juego y acciones que haremos entonces            
        if jugando == False:
            FuenteGameOver = pygame.font.SysFont("Consolas", 60)
            textoGameOver = FuenteGameOver.render("Game OVer", 0 , colorFuente)
            ventana.blit(textoGameOver, (80,320))
            pygame.mixer.music.fadeout(3000)

                    
        pygame.display.update()
    
# llamada a la funcion principal meteoritos
meteoritos()