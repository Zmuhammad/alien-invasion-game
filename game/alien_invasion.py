from score_board import Scoreboard
import sys
import pygame
from time import sleep
from pygame.constants import FULLSCREEN, K_LEFT
from pygame.display import set_allow_screensaver
from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien
from button import Button
from Game_stats import GameStats
from score_board import Scoreboard


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.game_active = False
        self.settings = Settings()
        self.stats = GameStats(self)

        self.screen = pygame.display.set_mode((0,0) ,pygame.FULLSCREEN )

        self.sb = Scoreboard(self)

        self.play_button = Button(self , "play")
        
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alian Invasion")

        self.bullets =pygame.sprite.Group()
        self.aliens =pygame.sprite.Group()

        # make rocket
        self.rocket = Rocket(self)

        self.creat_fleet()

    

    def creat_fleet(self):
        alien = Alien(self)
        screen_width  = self.settings.screen_width
        screen_hight = self.settings.screen_height
        alien_width , alien_hight = alien.rect.size

        rocket_height = self.rocket.rect.height
        available_space_x = screen_width - (alien_width)
        number_aliens_x = available_space_x  // (2 * alien_width)

        available_space_y = screen_hight - (3 * alien_hight) - rocket_height

        number_rows = available_space_y // (2 * alien_hight)

        for row_number in range (number_rows ):
            for alien_number in range (number_aliens_x):
                self.creat_alien(alien_number , row_number)      

    def creat_alien(self , alien_number , row_number):
        alien = Alien(self) 
        alien_width , alien_hight = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number 
        self.aliens.add(alien)

    def run_game(self):
        while True:
            self.check_events()
            if self.game_active  == True :
                self.rocket.updates()
                self.update_bullets()
                self.update_aliens()

            self.check_bullets_aliens_acollisions()
 
            self.update_screen()

    def update_bullets(self):
     #omit out screen bullets
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)   
            
    def check_bullets_aliens_acollisions(self):
        collision = pygame.sprite.groupcollide(self.bullets , self.aliens , True , True)
        if collision:
            for aliens in collision.values():
                self.stats.score += self.settings.point * len(aliens)

            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self.creat_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()
            
    def update_aliens(self):
        self.aliens.update()
        self.check_fleet_edges()

        if pygame.sprite.spritecollideany(self.rocket , self.aliens):
            self.rocket_hit()

        self.check_aliens_bottom()

    def rocket_hit(self):
        if self.stats.rocket_left > 0 :
            self.stats.rocket_left -= 1
            self.aliens.empty()
            self.bullets.empty()

            self.creat_fleet()
            self.rocket.center_rocket()

            sleep(1)
        else :
            self.game_active = False
            pygame.mouse.set_visible(True)


    def check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom :
                self.rocket_hit()
                break


    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y +=self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def check_events(self):
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)


    def check_play_button(self, mouse_pos):
        button_click = self.play_button.rect.collidepoint(mouse_pos)
        if button_click and not self.game_active:
            if self.play_button.rect.collidepoint(mouse_pos):
                self.stats.reset_stats()
                self.sb.prep_score()
                self.game_active = True

                self.aliens.empty()
                self.bullets.empty()

                self.creat_fleet()
                self.rocket.center_rocket()

                pygame.mouse.set_visible(False)

    def check_keydown_event(self,event):
        if event.key ==pygame.K_RIGHT:
            self.rocket.moving_right = True
        if event.key ==pygame.K_LEFT:
            self.rocket.moving_left = True
        if event.key ==pygame.K_UP:
            self.rocket.moving_up = True
        if event.key ==pygame.K_DOWN: 
            self.rocket.moving_down = True

        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key  ==pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup_event(self,event):
        if event.key ==pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key ==pygame.K_LEFT:
                self.rocket.moving_left = False
        if event.key ==pygame.K_UP:
            self.rocket.moving_up = False
        if event.key ==pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def fire_bullet(self) :
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__== "__main__":
    ai = AlienInvasion()
    ai.run_game()        