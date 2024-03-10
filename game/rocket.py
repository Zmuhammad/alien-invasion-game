from settings import Settings
import pygame

class Rocket:
    def __init__(self,ai_game) :
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.rocket_speed = ai_game.settings.rocket_speed 

        #load image
        self.image = pygame.image.load('W:\coding work\game\picture\game.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        
        #movement equalizer
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #movemnt contiueing by holding keys
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def blitme (self):
        self.screen.blit(self.image,self.rect) 

    def updates(self):
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.rocket_speed
        if self.moving_left and self.rect.left > 0 :
            self.x -= self.rocket_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
            self.y += self.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def center_rocket (self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)