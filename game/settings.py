class Settings:
    def __init__(self):
        self.bg_color = (15,3,22)
        self.screen_width = 1200
        self.screen_height = 800
        
        #bullet settings
        
        self.bullet_width =  6
        self.bullet_height = 16
        self.bullet_color = (255,170,0)
        
        #alien settings
        
        self.fleet_drop_speed = 11
        
        self.rocket_limits = 3

        self.speedup_scale = 1.11

        self.initialize_daynamic_settings()

    def initialize_daynamic_settings (self):
        self.alien_speed = 0.9
        self.bullet_speed = 3.1
        self.rocket_speed = 1.5
        self.fleet_direction = 1
        self.point = 50

    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.rocket_speed *= self.speedup_scale
        self.point = int(self.point * self.speedup_scale)
