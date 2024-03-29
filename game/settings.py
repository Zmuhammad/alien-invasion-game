class Settings:
    def __init__(self):
        self.bg_color = (15,3,22)
        self.screen_width = 1200
        self.screen_height = 800
        
        #bullet settings
        
        self.bullet_width =  5
        self.bullet_height = 15
        self.bullet_color = (255,165,0)
        
        #alien settings
        
        self.fleet_drop_speed = 10
        
        self.rocket_limits = 3

        self.speedup_scale = 1.1

        self.initialize_daynamic_settings()

    def initialize_daynamic_settings (self):
        self.alien_speed = 1
        self.bullet_speed = 3
        self.rocket_speed = 1.5
        self.fleet_direction = 1
        self.point = 50

    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.rocket_speed *= self.speedup_scale
        self.point = int(self.point * self.speedup_scale)