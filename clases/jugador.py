import pygame
# importamos disparo ya que sera el jugador el que haga el disparo, tenemos metodo disparar en clase Nave
from clases import disparo

class Nave(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("imagenes/nave.png")
        self.imagenExplota = pygame.image.load("imagenes/naveExplota.png")
        
        # cogemos el rectangulo de la imagen con GET_RECT()
        self.rect = self.imagenNave.get_rect()
        
        # establecemos la posicion inicial de la nave
        self.rect.centerx= 240
        self.rect.centery = 690
        self.velocidad = 20
        self.vida = True
        self.listaDisparo = []
        # cargamos el sonido del disparo
        self.sonidoDisparo = pygame.mixer.Sound("sonidos/disparo.aiff")
    
    # definimos el metodo para que se mueva la nave. Tiene que estar viva y no salirse por izq ni derecha
    def mover(self):
        if self.vida == True:
            # si esta a la izquierda, no se puede mover mas a la izquierda
            if self.rect.left<=0:
                self.rect.left=0
            # si esta a la derecha, no se puede mover mas a la derecha    
            elif self.rect.right>490:
                self.rect.right=490
        
                
    # metodo disparar            
    def disparar(self , x, y):
        if self.vida == True:
            # print("pium pium")
            misil = disparo.Misil(x,y)
            self.listaDisparo.append(misil)
            self.sonidoDisparo.play()
        
    # metododo dibujar la nave
    def dibujar (self, superficie):
        if self.vida == True:
            superficie.blit(self.imagenNave, self.rect)
        else:
            superficie.blit(self.imagenExplota, self.rect)