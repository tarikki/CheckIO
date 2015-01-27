import math


def checkio(a, b, c):
    sides = [a, b, c]                       # store the variables in a list
    more_sides = [a, b, c]                  # oh wait we need two
    biggest = max(sides)                    # get the biggest side
    sides.remove(biggest)                   # remove it from one list

    if (a == b == c) and c is not 0:        # check for equal sides and return the correct angles
        return [60, 60, 60]

    if biggest >= (sides[0] + sides[1]):    # the previous check makes this return a true value
        print("too short")                  # if this is not true then the triangle inequality is not satisfied
        return [0, 0, 0]
    angles = []                             # store the angles in an list we can return
    for i in range(0, 3):                   # create a loop
        x = more_sides[i % 3]               # and use modulo
        y = more_sides[(i + 1) % 3]         # to rotate the different sides
        z = more_sides[(i + 2) % 3]         # so we get all the angles from the cosine equation
        angles.append(int(((math.acos((x ** 2 - (y ** 2 + z ** 2)) / (-2 * y * z))) / math.pi * 180) + .5))

    angles.sort()                           # finally just sort the angles before returning them
    return angles

