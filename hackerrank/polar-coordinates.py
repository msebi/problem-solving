import cmath

com = input()

# print('Complex number: ', com)


# def is_valid_char(c):
#     if string.isdigit(c) is False and c != '+' and c != '-' and c != 'j':
#         return False
#     return True
#
#
# x = ''
# y = ''
# is_x_done = False
#
# for c in com:
#     if c == 'j':
#         break
#     if is_valid_char(c) and is_x_done is False:
#         x += str(c)
#     elif is_valid_char(c) and is_x_done is True:
#         y += str(c)

com = "(" + com + ")"
c = complex(com)

print((c.real ** 2 + c.imag ** 2) ** (1/2))
print(cmath.phase(complex(c.real, c.imag)))

