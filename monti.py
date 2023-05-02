def ask_to_change_door(remaining_door): # 필용
    """
    참가자에게 다른 문으로 바꿀 것인지 물어봅니다.
    """
    change_door = input(f"Do you want to switch to the remaining door ({remaining_door})? (y/n)").lower()
    return change_door == 'y'
