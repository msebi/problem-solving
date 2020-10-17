import math

ab = int(input())
bc = int(input())

# ac = (ab ** 2 + bc ** 2) ** (1/2)
# sin_val = ab / ac
#
# eps = 0.5
#
# print('angle: ' + str(math.asin(sin_val) * 180 / math.pi - eps))


print(str(round(math.degrees(math.atan2(ab, bc)))) + '°')

