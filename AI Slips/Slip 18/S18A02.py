"""
A* Approach for Arranging Objects in a Room

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python arrange_objects_astar.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 arrange_objects_astar.py
"""

import heapq

class RoomState:
    def __init__(self, room_width, room_height):
        self.room_width = room_width
        self.room_height = room_height
        self.objects = []

    def add_object(self, width, height):
        self.objects.append((width, height))

    def is_valid_placement(self, x, y, width, height):
        return 0 <= x <= self.room_width - width and 0 <= y <= self.room_height - height

    def is_goal_state(self):
        return len(self.objects) == 9  # Assuming 5 rectangular and 4 square-shaped objects

    def __lt__(self, other):
        return False  # Dummy comparison method, not used in A* search

def heuristic(state):
    # A simple heuristic: prioritize placing larger objects first
    return -max(max(obj) for obj in state.objects)

def a_star_search(initial_state):
    open_set = [(heuristic(initial_state), initial_state)]
    closed_set = set()

    while open_set:
        _, current_state = heapq.heappop(open_set)

        if current_state.is_goal_state():
            return current_state

        closed_set.add(current_state)

        for width, height in current_state.objects:
            for x in range(current_state.room_width):
                for y in range(current_state.room_height):
                    if current_state.is_valid_placement(x, y, width, height):
                        new_state = RoomState(current_state.room_width, current_state.room_height)
                        new_state.objects = current_state.objects.copy()
                        new_state.objects.remove((width, height))
                        new_state.add_object(width, height)
                        new_state.add_object(current_state.room_width - x - width, current_state.room_height - y - height)

                        if new_state not in closed_set:
                            heapq.heappush(open_set, (heuristic(new_state), new_state))

    return None

if __name__ == "__main__":
    # Define the dimensions of the room
    room_width = 10
    room_height = 10

    # Create the initial state
    initial_state = RoomState(room_width, room_height)

    # Add objects to be arranged
    initial_state.add_object(2, 3)
    initial_state.add_object(4, 2)
    initial_state.add_object(3, 3)
    initial_state.add_object(1, 1)
    initial_state.add_object(2, 2)
    initial_state.add_object(1, 3)
    initial_state.add_object(3, 2)
    initial_state.add_object(2, 1)
    initial_state.add_object(1, 2)

    # Run A* search
    result_state = a_star_search(initial_state)

    # Print the result
    if result_state:
        print("Objects Placement:")
        for idx, (width, height) in enumerate(result_state.objects, start=1):
            print(f"Object {idx}: ({width} x {height})")
    else:
        print("No valid arrangement found.")
