#!/usr/bin/python3

from sympy import Matrix, symbols, sin, cos

angle, theta, phi, alpha, beta, gamma, psi, phi_r, theta_r, xi = symbols (
    'angle, theta, phi, alpha, beta, gamma, psi, phi_r, theta_r, xi',
    real = True)

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

# Now we compute the real azimuth/elevation when the antenna is elevated
# after elevation/azimuth rotations, we call that phi_r and theta_r (for
# "real"). The additional elevation on the X-axis psi (after applying
# theta and phi) is positive if the observer is higher than the antenna
# and negative if lower. Note that this introduces another rotation
# around the central axis of the antenna, we try several variants.

print ('rot_y applied to m_real')
m_real     = rot_x (psi) @ rot_z (phi_r) @ rot_x (-theta_r) @ rot_y (xi)
m_measured = rot_z (phi) @ rot_x (-theta)
print (m_real)
print (m_measured)

print ('rot_y applied to m_measured')
m_real     = rot_x (psi) @ rot_z (phi_r) @ rot_x (-theta_r)
m_measured = rot_z (phi) @ rot_x (-theta) @ rot_y (xi)
print (m_real)
print (m_measured)

print ('We can apply inverse psi to measured, xi on measured')
m_real     = rot_z (phi_r) @ rot_x (-theta_r)
m_measured = rot_x (-psi) @ rot_z (phi) @ rot_x (-theta) @ rot_y (xi)
print (m_real)
print (m_measured)

print ('We can apply inverse psi to measured, xi on real')
m_real     = rot_z (phi_r) @ rot_x (-theta_r) @ rot_y (xi)
m_measured = rot_x (-psi) @ rot_z (phi) @ rot_x (-theta)
print (m_real)
print (m_measured)
