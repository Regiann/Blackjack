import random
import time


def __main__():

  def game():
    def card_pick():
      global playerCard1, playerCard2, playerTotal, compCard1, compCard2, compTotal
      print("Welcome to the game of Blackjack!" + "\n")
      playerCard1 = random.randint(1, 11)
      print(f"Your first card is {playerCard1}" + "\n")
      time.sleep(1)
      playerCard2 = random.randint(1, 11)
      print(f"Your second card is {playerCard2}" + "\n")
      time.sleep(1)
      playerTotal = playerCard1 + playerCard2
      if playerTotal > 21:
        if playerCard1 == 11:
          if playerTotal > 21: #Ensures that Further conditions make sense.
            playerCard1 = 1
            print("Your first card is now 1 as it would have been an ace, which would make you lose" + "\n")
            time.sleep(1)
            playerTotal = playerCard1 + playerCard2
            print(f"Your total is {playerTotal}" + "\n")
            
        elif playerCard2 == 11:
          if playerTotal > 21:
            playerCard2 = 1
            playerTotal = playerCard1 + playerCard2
            print("Your second card is now 1 as it would have been an ace, which would make you lose" + "\n")
            print(f"Your total is {playerTotal}")
        
        else:
          if playerTotal > 21:
            print("You have gone Bust!" + "\n" + "You lose!" + "\n")
            time.sleep(1)

      else:
        print("You have a total of " + str(playerTotal) + "!" + "\n")
        time.sleep(2)
    
      compCard1 = random.randint(1,11)
      compCard2 = random.randint(1,11)
      compTotal = compCard1 + compCard2
      print(f"The computer's first card is {compCard1}" + "\n")
      time.sleep(2)
      print(f"The computer's second card is {compCard2}" + "\n")
      time.sleep(2)
      if compTotal > 21:
        if compCard1 == 11:
          print("The computer's first card is now 1 as it would have been an ace, which would make them lose")
          compCard1 = 1
          compTotal = compCard1 + compCard2
          print("" + "\n" + "The computer's total is " + str(compTotal))
          time.sleep(2)
        elif compCard2 == 11:
          print("The computer's second card is now 1 as it would have been an ace, which would make them lose")
          compCard2 = 1
          compTotal = compCard1 + compCard2
          print("" + "\n" + "The computer's total is " + str(compTotal))
          time.sleep(2)
        else:
          print("The computer has gone Bust!" + "\n" + "You win!")
      else:
        print("The computer has a total of " + str(compTotal) + "!")
        time.sleep(1)
        turns()

    def turns():
      global playerTotal
      global compTotal
      loop = True
      while loop is True:
        while playerTotal < 21:
          print("Would you like to hit or stand?" + "\n")
          time.sleep(1)
          playerChoice = str(input()).lower()
          if playerChoice == "hit":
            playerCard3 = random.randint(1,11)
            print(f"Your third card is {playerCard3}")
            time.sleep(1)
            playerTotal = playerTotal + playerCard3
            print("Your new total is " + str(playerTotal))
            time.sleep(1)
          elif playerChoice == "stand":
            print("You have chosen to stand." + "\n")
            time.sleep(1)
            break
          if playerTotal == 21:
            print("You have the best possible cards!, Standing Automatically" + "\n")
            time.sleep(1)
            break
        while compTotal < 21:
          if compTotal < 21:
            if compTotal < 17:
              compCard3 = random.randint(1,11)
              print(f"The computer's third card is {compCard3}" + "\n")
              time.sleep(1)
              compTotal = compTotal + compCard3
          elif compTotal > 16:
            print("The computer has chosen to stand." + "\n")
            time.sleep(1)
          checks()

    def checks():
      global playerTotal
      global compTotal
      if playerTotal > 21:
        print("Your total is " + str(playerTotal) + "!" + "\n")
        print("You have gone Bust!" + "\n" + "You lose!" + "\n")
        time.sleep(1)
        quit()
      elif compTotal > 21:
        print("The computer's total is " + str(compTotal) + "!" + "\n")
        time.sleep(1)
        print("The computer has gone Bust!, You win!" + "\n")
        quit()
      elif playerTotal == 21:
        print("You have the perfect Score! You win!" + "\n")
        time.sleep(1)
        quit()
      elif compTotal == 21:
        print("The computer has the perfect Score! You lose!" + "\n")
        time.sleep(1)
        quit()
      else:
        turns()
        
    card_pick()      
    
    
          



  game()


__main__()
