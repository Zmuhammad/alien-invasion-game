class GameStats:
    def __init__(self , ai_game) :
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0

    def reset_stats (self):
        self.rocket_left = self.settings.rocket_limits
        self.score = 0
        self.level = 1