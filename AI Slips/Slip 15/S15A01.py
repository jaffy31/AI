def monkey_banana_problem(room):
    monkey_position = (0, 0)
    banana_positions = [(3, 1), (2, 2), (1, 4)]
    bananas_eaten = 0

    # Function to check if a position is valid (not a wall)
    def is_valid_position(position):
        x, y = position
        return 0 <= x < len(room) and 0 <= y < len(room[0]) and room[x][y] != "WALL"

    # Function to move the monkey to the banana position
    def move_to_banana(banana_position):
        nonlocal monkey_position, bananas_eaten
        if is_valid_position(banana_position):
            monkey_position = banana_position
            bananas_eaten += 1
            print(f"The monkey moves to {banana_position} and eats a banana.")
        else:
            print(f"The monkey cannot move to {banana_position} because of a wall.")

    # Iterate through the banana positions and simulate the monkey eating them
    for banana in banana_positions:
        move_to_banana(banana)

    return bananas_eaten

if __name__ == "__main__":
    # Define the room with "WALL" representing walls
    room = [
        ["", "", "", "", ""],
        ["", "", "", "WALL", ""],
        ["", "", "WALL", "", ""],
        ["", "", "", "", ""],
    ]

    bananas_eaten = monkey_banana_problem(room)
    print(f"The monkey can eat {bananas_eaten} bananas.")
