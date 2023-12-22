#!/usr/bin/python3

from sympy import Matrix, symbols, sin, cos

angle, theta, phi, alpha, beta, gamma = symbols (
    'angle, theta, phi, alpha, beta, gamma', positive = True, real = True)

def rot_x (angle):
    return Matrix ([ [1,          0,             0]
                   , [0, cos (angle), -sin (angle)]
                   , [0, sin (angle),  cos (angle)]])
# end def rot_x

def rot_y (angle):
    return Matrix ([ [ cos (angle), 0, sin (angle)]
                   , [0,            1,           0]
                   , [-sin (angle), 0, cos (angle)]])
# end def rot_y

def rot_z (angle):
    return Matrix ([ [cos (angle), -sin (angle), 0]
                   , [sin (angle),  cos (angle), 0]
                   , [0,            0,           1]])
# end def rot_z

m1 = rot_z (phi) @ rot_x (-theta)
m2 = rot_y (-alpha) @ rot_z (-beta) @ rot_y (-gamma)

print (m1)
print (m2)
