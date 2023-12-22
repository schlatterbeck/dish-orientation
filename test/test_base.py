#!/usr/bin/python3

import pytest
import numpy as np
from rotmatrix import rot_x, rot_y, rot_z

class Test_Rotation:

    def test_rot_x (self):
        for a in 0, 30, 45, 60, 90:
            r_x_p = rot_x (a)
            r_x_m = rot_x (-a)
            assert (np.abs (r_x_p @ r_x_m - np.eye (3)) < 1e-6).all ()
            assert (np.abs (r_x_m @ r_x_p - np.eye (3)) < 1e-6).all ()
    # end def test_rot_x

    def test_rot_y (self):
        for a in 0, 30, 45, 60, 90:
            r_y_p = rot_y (a)
            r_y_m = rot_y (-a)
            assert (np.abs (r_y_p @ r_y_m - np.eye (3)) < 1e-6).all ()
            assert (np.abs (r_y_m @ r_y_p - np.eye (3)) < 1e-6).all ()
    # end def test_rot_y

    def test_rot_z (self):
        for a in 0, 30, 45, 60, 90:
            r_z_p = rot_z (a)
            r_z_m = rot_z (-a)
            assert (np.abs (r_z_p @ r_z_m - np.eye (3)) < 1e-6).all ()
            assert (np.abs (r_z_m @ r_z_p - np.eye (3)) < 1e-6).all ()
    # end def test_rot_z

    def test_rot_z_via_xy (self):
        r = rot_x (-90) @ rot_y (90) @ rot_x (90)
        assert (np.abs (r - rot_z (-90)) < 1e-6).all ()
    # end def test_rot_z_via_xy

# end class Test_Rotation


