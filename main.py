import random

def generate_weights():
    weights = []
    fw = random.randint(1, 300)
    sw = random.randint(1, 300)
    tw = 713 - fw - sw
    
    return [fw, sw, tw]

found_boxes = False

while found_boxes != True:

    box_cords = [random.randint(1, 7) for i in range(3)]
    if len(set(box_cords)) != len(box_cords):
        continue
    else:
        print(f"Boxes are buried in {box_cords}")
        box_cords_input = []
        for j in range(3):
            cord = int(input(f"Box {j + 1}: "))
            box_cords_input.append(cord)

        weights = generate_weights()
        weight_found = 0

        for i in range(3):
            if box_cords_input[i] == box_cords[i]:
                weight_found += weights[i]

        if weight_found == 713:
            found_boxes = True

for i in range(3):
    print(f"Box {i + 1} is found at point '{box_cords_input[i]}' and has a weight of {weights[i]}")