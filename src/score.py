class Score:
    score = 0

    @staticmethod
    def increment_score():
        Score.score += 1
        
    @staticmethod
    def reset_score():
        Score.score = 0

    @staticmethod
    def get_score():
        return Score.score