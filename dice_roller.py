import random

dice_rolls = int(input("How many dices would you like to roll? "))
dice_size = int(input("How many sides are the dice? "))

player_1_name = input("What is the name of the Player 1? ")
player_2_name = input("What is the name of the Player 2? ")

# TODO: Give the user am option to start another player first
def main():
  turn = "player_1" # "player_1" or "player_2"
  player1_rolls = []
  player2_rolls = []

  while True:

    dice_sum = 0 # Temporal summary of dice rolls
    
    for i in range(0, dice_rolls):
      roll = random.randint(1, dice_size)
      dice_sum += roll

      if roll == 1:
        print(f'You rolled a {roll}! Critical Fail')
      elif roll == dice_size:
        print(f'You rolled a {roll}! Critical Success')
      else:
        print(f'You rolled a {roll}')
      
    # Sum the try to the list...
    if turn == "player_1":
      player1_rolls.append(dice_sum)
    else:
      player2_rolls.append(dice_sum)
    
    print(f'You rolled a total of {dice_sum}')

    turn = turn == "player_1" and "player_2" or "player_1"
    players_turn = turn == "player_1" and player_1_name or player_2_name
    try_again_input = input(f"Would you like to throw again? This time is {players_turn}'s turn [Y/n]").lower()

    if try_again_input == "y" or try_again_input == "":
      # Sum the try?
      continue
    elif try_again_input == "n":
      print(f'Thank you for your time :v')
      # Show dice roll total
      break
    else:
      print("I assume that is a YES!!!")
      continue

if __name__== "__main__":
  main()