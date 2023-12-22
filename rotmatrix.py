#!/usr/bin/python

import numpy as np

def rot_x (angle):
    angle = angle / 180 * np.pi
    return np.array ([ [1,              0,               0]
                     , [0, np.cos (angle), -np.sin (angle)]
                     , [0, np.sin (angle),  np.cos (angle)]])
# end def rot_x

def rot_y (angle):
    angle = angle / 180 * np.pi
    return np.array ([ [ np.cos (angle), 0, np.sin (angle)]
                     , [0,               1,              0]
                     , [-np.sin (angle), 0, np.cos (angle)]])
# end def rot_y

def rot_z (angle):
    angle = angle / 180 * np.pi
    return np.array ([ [np.cos (angle), -np.sin (angle), 0]
                     , [np.sin (angle),  np.cos (angle), 0]
                     , [0,               0,              1]])
# end def rot_z

def azi_ele (azi, ele):
    return rot_z (azi) @ rot_x (-ele)
# end def azi_ele

def alpha_beta (alpha, beta):
    return rot_z (beta) @ rot_y (alpha)
# end def alpha_beta

if __name__ == '__main__':

    # Rückwärts

    alpha = -40.9
    beta  = -69.3

    pt = np.array ([0, 0, 1])
    print (pt)
    pt = azi_ele (0, 60) @ pt
    print (pt)
    pt = rot_y (90) @ pt
    print (pt)
    pt = rot_z (-60) @ pt
    print (pt)
    pt = rot_y (-90) @ pt
    print (pt)
    print ()

    pt = np.array ([0, 0, 1])
    print (pt)
    pt = azi_ele (45, 60) @ pt
    print (pt)
    pt = rot_y (68) @ pt
    print (pt)
    pt = rot_z (-69.3) @ pt
    print (pt)
    pt = rot_y (-68) @ pt
    print (pt)
    print ()

    a1 = azi_ele    (0,  60)
    a2 = alpha_beta (90, -60)
    print (rot_y (-90) @ a2 @ a1)

    a1 = azi_ele    (0,  30)
    a2 = alpha_beta (90, -30)
    print (rot_y (-90) @ a2 @ a1)

    a1 = azi_ele    (45, 60)
    a2 = alpha_beta (68, -69.3)
    a2a1 = a2 @ a1
    angles = np.array \
        ([  np.arccos (a2a1 [0, 0])
         ,  np.arcsin (a2a1 [0, 2])
         , -np.arcsin (a2a1 [2, 0])
         ,  np.arccos (a2a1 [2, 2])
        ])
    print (angles)
    if  (    np.sign (angles [0]) != np.sign (angles [1])
         and np.sign (angles [2]) != np.sign (angles [3])
        ):
        angles [0] = -angles [0]
        angles [3] = -angles [3]
    print (angles)
    y_angle = sum (angles) / 4 / np.pi * 180
    print (y_angle)
    print (a2a1)
    print (rot_y (-y_angle) @ a2a1)
