# How many boxes of tiles do I need?
import math


room_length = float(input("Enter the length of the room: "))
room_width = float(input("Enter the width of the room: "))


room_area = room_length * room_width
extra_tiles = room_area * 1.10
boxes_needed = extra_tiles / 12
total_boxes = math.ceil(boxes_needed)

print(f"You will need {total_boxes} boxes of tiles.")