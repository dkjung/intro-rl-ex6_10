from enum import Enum
import random


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27,   7.1492e7)
    SATURN  = (5.688e+26, 6.0268e7)
    URANUS  = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)


print('list(Color) = ', list(Color))
print('len(Color) =', len(Color))

for color in Color:
    print(color)
    print(color.name, color.value)

for i, color in enumerate(Color):
    print(i, color)

cnt = {Color.RED: 4, Color.GREEN: 3, Color.BLUE: 6}

print()
for _ in range(len(Color) * 2):
    print(random.choice(list(Color)))

print(list(Planet))
print(list(Planet))
