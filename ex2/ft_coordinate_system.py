
import math


def calculate_pos(cords1: tuple[float, float, float],
                  cords2: tuple[float, float, float]) -> float:
    x1, y1, z1 = cords1
    x2, y2, z2 = cords2

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    return distance


def get_player_pos() -> tuple[float, float, float]:
    while True:
        pos = input("Enter new coordinates as floats in format 'x,y,z': ")

        num = pos.split(',')

        if (len(num) != 3):
            print("Invalid syntax")
            continue

        nums = []

        for n in num:
            try:
                nums.append(float(n))
            except ValueError as error:
                print(f"Error on parameter '{n}': {error}")
                break

        else:
            return (nums[0], nums[1], nums[2])


if __name__ == '__main__':
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    first_cords = get_player_pos()

    print(f"Got a first tuple: {first_cords}")
    print(f"It includes: X={first_cords[0]}, "
          f"Y={first_cords[1]}, Z={first_cords[2]}")

    center = (0.0, 0.0, 0.0)
    distance_center = round(calculate_pos(first_cords, center), 4)
    print(f"Distance to center: {distance_center}\n")

    print("Get a second set of coordinates")
    second_pos = get_player_pos()

    distance_between = round(calculate_pos(first_cords, second_pos), 4)
    print(f"Distance between the 2 sets of coordinates: {distance_between}")
