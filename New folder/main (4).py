#Define the base class player
class Player:
  def player(self):
    print("The player is playing cricket.")

#Define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

#Define the derived class Bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

#Creat object of Btsman and Bowling classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()