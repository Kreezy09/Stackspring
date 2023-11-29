import pygame
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos() #mouse position
        
        if self.rect.collidepoint(pos): #if mouse is over button    
            if pygame.mouse.get_pressed()[0] and self.clicked == False: #if left mouse button is pressed  
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == False: #if left mouse button is not pressed
            self.clicked = False
        #draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action