import pygame

class Asteroide(pygame.sprite.Sprite):
    
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenAsteroide = pygame.image.load("imagenes/asteroide.png")
        self.rect = self.imagenAsteroide.get_rect()
        self.velocidad = 3
        self.rect.top = posY
        self.rect.left = posX
        self.listaAsteroides = []
    
    def recorrido(self):
        # aqui sumamos la velocidad porque los meteoritos iran bajando
        self.rect.top = self.rect.top + self.velocidad
        
    def dibujar(self, superficie):
        superficie.blit(self.imagenAsteroide , self.rect)