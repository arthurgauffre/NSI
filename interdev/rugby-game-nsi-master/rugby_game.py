class RugbyGame:
    def __init__(self, team_1, team_2):
        self.team_1 = team_1
        self.team_2 = team_2
        self.score = "0-0"
        
    def get_score(self):
        return self.score

    def drop(self, equipe):
        if equipe == self.team_1:
            self.score[0] = str(int(self.score[0]) + 3)
        if equipe == self.team_2:
            self.score[2] = str(int(self.score[2]) + 3)
        

    

