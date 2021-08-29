import random
from Game_Dice_simulator import game_dice_sum, game_dice_sum_random
def cube_throw():
    "Return number from 1 - 6 "
    return random.choice(list(range(1, 7)))

def game_2001():
    """
    function add 2x diffrent dices throws to user points and computer points
    :return: point winner
    """
    user_points = 0
    computer_points = 0
    while user_points < 2001 and computer_points < 2001:
        dice_y = [3, 4, 6, 8, 10, 12, 20, 100]
        throw_user_number = sum([game_dice_sum() for x in range(2)])
        user_points += throw_user_number
        throw_computer_number = sum([game_dice_sum_random() for x in range(2)])
        computer_points += throw_computer_number
        run_game = input("Press Enter to continue")
        if throw_user_number == 7:
            user_points = user_points // 7
        elif throw_user_number == 11:
            user_points = user_points * 11
        elif throw_computer_number == 7:
            computer_points = computer_points // 7
        elif throw_computer_number == 11:
            computer_points = computer_points * 11
        print(f"User: {user_points}  Computer: {computer_points}")
    if user_points > computer_points:
        print("You win!")
    elif computer_points > user_points:
        print("Computer win!")
    else:
        print("Draw!")

    return f"Your points: {user_points}, computer points: {computer_points} "

print(game_2001())