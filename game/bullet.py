import pygame
from pygame.sprite import Sprite
from settings import Settings

#bullet shape construction

class Bullet(Sprite) :
    def __init__ (self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settigs =ai_game.settings
        self.color = self.settigs.bullet_color

        self.rect = pygame.Rect(0,0 , self.settigs.bullet_width, self.settigs.bullet_height)
        self.rect.midtop = ai_game.rocket.rect.midtop

        self.y = float(self.rect.y)

    def update (self):
        self.y -= self.settigs.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        
