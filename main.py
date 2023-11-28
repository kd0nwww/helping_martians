# importing random module to generate weights and positions of boxes
import random

# function that generates and returns 3 random weights that exceed 713
def generate_weights():
    weights = []
    fw = random.randint(1, 300)
    sw = random.randint(1, 300)
    tw = 713 - fw - sw
    
    return [fw, sw, tw]

# i used this variable to control while loop
found_boxes = False

while found_boxes != True:

    # generation of random integers not exceeding 7
    # that will be the coordinates of boxes
    box_cords = [random.randint(1, 7) for i in range(3)]
    
    # iteration is skipped when coordinates are not unique
    # thats because two or three boxes cannot be buried in the same place
    if len(set(box_cords)) != len(box_cords):
        continue
    else:
        # here i'm giving a hint
        print(f"Boxes are buried in {box_cords}")
        # input of user coordinates
        box_cords_input = []
        for j in range(3):
            cord = int(input(f"Box {j + 1}: "))
            box_cords_input.append(cord)
        # weights generation
        weights = generate_weights()
        weight_found = 0

        # iteration through user-defined coordinates and checking the sum of weights
        # if sum of weights id not equal to 713 then loop starts over again
        for i in range(3):
            if box_cords_input[i] == box_cords[i]:
                weight_found += weights[i]

        if weight_found == 713:
            found_boxes = True

# output
for i in range(3):
    print(f"Box {i + 1} is found at point '{box_cords_input[i]}' and has a weight of {weights[i]}")