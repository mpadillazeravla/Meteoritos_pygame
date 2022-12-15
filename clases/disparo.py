import pygame

class Misil(pygame.sprite.Sprite):
    
    # aqui pasamos self y las coordenadas de la posicion para que el disparo se ejecute desde la posicion
    # que tiene el misil
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenMisil = pygame.image.load("imagenes/misil.png")
        self.rect = self.imagenMisil.get_rect()
        self.velocidadDisparo = 10
        self.rect.top = posY
        self.rect.left = posX
        
    # el recorrido d misil sera la posicion hasta arriba menos la velocidad de disparo para que el misil suba
    #   
    def recorrido(self):
        self.rect.top = self.rect.top - self.velocidadDisparo
        
    def dibujar ( self, superficie):
        superficie.blit(self.imagenMisil, self.rect)