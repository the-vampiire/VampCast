from random import random

def generate_title_table(title, edge_character = "#", height = 11, width = 80, thickness = 2,   side_thickness = 3):
    mid_row = (height / 2) if height % 2 == 0 else ((height + 1) / 2)
    middle_rows = [(mid_row - 1), mid_row, (mid_row + 1)]
    title_length = len(title)
    number_of_spaces = int((((width - (side_thickness * 2)) - title_length) / 2))
    left_spaces = (number_of_spaces * " ")
    right_spaces = left_spaces if title_length % 2 == 0 else ((number_of_spaces + 1) * " ")
    edge = side_thickness * edge_character
    output = ""

    for row in range(1, height + 1):
        if row not in middle_rows: # normal rows
            if row in [(thickness - 1), thickness, (height - 1), height]: # top / bottom
                output += ((edge_character * width)  + "\n")
            else: # character-edged rows
                output += (edge + (" " * (width - (2 * side_thickness))) + edge + "\n")
        else: # title rows
            if row != mid_row:
                output += (edge + left_spaces + ("-" * title_length) + right_spaces + edge + "\n")
            else:
                output += (edge + left_spaces + title.upper() + right_spaces + edge + "\n")
    return output


def roll_dice(num_dice, num_games):
    list_of_rolls = [[0 for i in range(num_dice)] for j in range(num_games)]
    for roll in range(len(list_of_rolls)):
      for die in range(len(list_of_rolls[roll])):
          list_of_rolls[roll][die] = int(random() * 6 + 1)
    return list_of_rolls

def sum_of_roll(list_of_rolls):
    return [sum(roll) for roll in list_of_rolls] 

def got_yahtzee(roll):
    return 1 if [roll[0] for die in roll] == roll else 0

def yahtzee(list_of_rolls):
    return sum((got_yahtzee(roll) for roll in list_of_rolls))

def game_summary(list_of_rolls):
    return { 
        "sum": sum_of_roll(list_of_rolls), 
        "yahtzee_count": yahtzee(list_of_rolls) 
    }

def main():
    while True:
        try:
            num_dice = int(input("how many dice per roll?\n>>> "))
        except ValueError:
            print("you must enter an integer value for dice")
        else:
            try:
                num_games = int(input("how many rolls per game?\n>>> "))
            except ValueError:
                print("you must enter an integer value for number of games")
            else:
                game = roll_dice(num_dice, num_games)
                summary = game_summary(game)

                if summary["yahtzee_count"]: 
                    print(generate_title_table("YOU ROLLED A YAHTZEE!",  '$'))
                else: 
                    print("sum of the game rolls: {0}".format(summary["sum"]))

                quit_check = input('type "quit" to exit. type any other key to start a new game\n>>> ')
                if quit_check == "quit": 
                    break

if __name__ == "__main__":
    print(generate_title_table("yahtzee!", '@', 9, 30))
    main()

