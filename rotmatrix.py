#!/usr/bin/python

import numpy as np
from numpy import sin, cos, pi
from numpy import arcsin as asin
from numpy import arccos as acos

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

    print ("Turning a known point, elevation only (azimuth 0)")
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

    print ("Turning a known point with azimuth *and* elevation")
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
    print ("Rotation matrix azi=0, ele=60 and turned back via alpha, beta")
    print ("Observe: almost the identity matrix")
    print (rot_y (-90) @ a2 @ a1)

    a1 = azi_ele    (0,  30)
    a2 = alpha_beta (90, -30)
    print ("Rotation matrix azi=0, ele=30 and turned back via alpha, beta")
    print ("Observe: almost the identity matrix")
    print (rot_y (-90) @ a2 @ a1)

    print ("Example measured from openscad")
    a1 = azi_ele    (45, 60)
    alpha = 68
    beta  = -69.3
    a2 = alpha_beta (alpha, beta)
    a2a1 = a2 @ a1
    angles = np.array \
        ([  np.arccos (a2a1 [0, 0])
         ,  np.arcsin (a2a1 [0, 2])
         , -np.arcsin (a2a1 [2, 0])
         ,  np.arccos (a2a1 [2, 2])
        ])
    print ("Gamma angles from matrix:")
    print (angles)
    if  (    np.sign (angles [0]) != np.sign (angles [1])
         and np.sign (angles [2]) != np.sign (angles [3])
        ):
        angles [0] = -angles [0]
        angles [3] = -angles [3]
    print ("Gamma angles from matrix, sign corrected:")
    print (angles)
    gamma = -sum (angles) / 4 / np.pi * 180
    print ("computed gamma:", gamma)
    print ("After rotating by alpha, beta")
    print (a2a1)
    print ("And finally by gamma, observe its nearly the identity matrix")
    print (rot_y (gamma) @ a2a1)

    print ("Matrix from azimuth/elevation:")
    print (a1)
    print ("alpha:", alpha, "beta:", beta, "gamma:", gamma)
    print ("Matrix from measured alpha beta gamma:")
    print (rot_y (-alpha) @ rot_z (-beta) @ rot_y (-gamma))
    print ("The above two matrices are almost identical")

    phi    = 45 / 180 * np.pi
    theta  = 60 / 180 * np.pi
    alpha  = alpha / 180 * np.pi
    beta   = beta  / 180 * np.pi
    gamma  = gamma / 180 * np.pi

    # this should be zero:
    print ("should be zero:", end = ' ')
    print ( np.sin (alpha) * np.cos (beta) * np.cos (gamma)
          + np.sin (gamma) * np.cos (alpha)
          )

    cosphi = (-np.sin (alpha) * np.sin (gamma)
             + np.cos (alpha) * np.cos (beta) * np.cos (gamma)
             )
    print ('cos phi', cosphi, np.cos (phi))
    phi1 = np.arccos (cosphi)
    sinphi = -np.sin (beta) * np.cos (gamma)
    print ('sin phi', sinphi, np.sin (phi))
    phi2 = np.arcsin (sinphi)
    sintheta = (- (np.sin (alpha) * np.sin (beta)))
    print ('sin theta', sintheta, np.sin (theta))
    theta1 = np.arcsin (sintheta)
    costheta = (-np.sin (alpha) * np.sin (gamma) * np.cos (beta)
               + np.cos (alpha) * np.cos (gamma)
               )
    print ('cos theta', costheta, np.cos (theta))
    theta2 = np.arccos (costheta)
    print ('phi:', phi1 / np.pi * 180, phi2 / np.pi * 180)
    print ('theta:', theta1 / np.pi * 180, theta2 / np.pi * 180)

    print ("And finally everything computed:")
    phi    = 45 / 180 * pi
    theta  = 60 / 180 * pi
    print ("phi:   %7.3f°" % (phi   * 180 / pi))
    print ("theta: %7.3f°" % (theta * 180 / pi))

    beta   = -acos (cos (phi) * cos (theta))
    alpha  = pi - acos ((sin (phi) * cos (theta)) / sin (beta))
    gamma  = asin ((cos (phi) * sin (theta)) / sin (beta))

    print ("alpha: %7.3f°" % (alpha * 180 / pi))
    print ("beta:  %7.3f°" % (beta  * 180 / pi))
    print ("gamma: %7.3f°" % (gamma * 180 / pi))

    # Now back to phi, theta
    theta  = -asin (sin (alpha) * sin (beta))
    phi    = -asin ((cos (alpha) * sin (beta)) / cos (theta))
    print ("phi:   %7.3f°" % (phi   * 180 / pi))
    print ("theta: %7.3f°" % (theta * 180 / pi))
