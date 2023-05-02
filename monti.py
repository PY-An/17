import random

def select_door():
    doors = ['A', 'B', 'C']
    return random.choice(doors)

def get_player_choice():
    return input("Choose a door (A, B, or C), or type 'end' to exit the game: ").upper()

