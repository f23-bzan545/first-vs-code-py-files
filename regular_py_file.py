import random

# sides selfishly based on how adam sees you from his POV
room_sides = ["left", "right"]
rows = ["front", "middle", "back"]

side = random.choice(room_sides)
row = random.choice(rows)

message = f"Would someone from the *{row} row* on\nthe *{side} side* of the room please answer?"

print(message)
