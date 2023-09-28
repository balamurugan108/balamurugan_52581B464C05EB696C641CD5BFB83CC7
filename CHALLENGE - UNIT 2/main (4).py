class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")
# Creating instances of the derived classes
player = Player()
batsman = Batsman()
bowler = Bowler()

# Calling the play() method for each object
player.play()
batsman.play()
bowler.play()


