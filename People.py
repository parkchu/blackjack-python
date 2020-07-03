class People(object):
    
    def hasAce(self):
        for x in self.hand:
            if x.num == 1:
                return True
        return False
            
    def totalScore(self):
        total_score = 0
        for x in self.hand:
            total_score += x.num
        if self.hasAce():
            if total_score + 10 <= 21:
                total_score += 10
            return total_score
        
        else:
            return total_score

    def whetherBust(self):
        total_score = self.totalScore()
        if total_score > 21:
            return True
            
        elif total_score <= 21:
            return False
