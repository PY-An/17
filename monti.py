import random

def select_door():
    doors = ['A', 'B', 'C']
    return random.choice(doors)

def get_player_choice():
    return input("Choose a door (A, B, or C), or type 'end' to exit the game: ").upper()

def play_monty_hall(): # 소현
    """
    몬티 홀 게임을 실행합니다.
    """
    answer = select_door()
    player_choice = get_player_choice()

    if player_choice == 'END':
        print("Game ended.")
        return None

    non_answer_door = get_non_answer_door(['A', 'B', 'C'], player_choice, answer)
    print(f"The door {non_answer_door} does not contain the answer.")

    remaining_door = get_remaining_door(['A', 'B', 'C'], player_choice, non_answer_door)
    if ask_to_change_door(remaining_door):
        player_choice = remaining_door

    if player_choice == answer:
        print("Congratulations! You won the prize!")
        return True
    else:
        print(f"Sorry, the answer was behind door {answer}. Better luck next time!")
        return False

