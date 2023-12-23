Dish-Orientation
================

This project lets you determine the azimuth and elevation of a dish
antenna you see from some location. You need to know your location (we
call this the observer location in the following) and the location of
the antenna:

- The height of both locations
- The distance
- The direction the observer is located from the antenna (for azimuth
  correction)

There is currently much code to originally derive the equations needed
to compute the dish azimuth and elevation. The antenna is seen from the
observer location as an ellipse (e.g. when you take a photo). The
ellipse major axis is called l1, the minor axis l2.

.. image:: ellipse.svg
  :width: 400
  :alt: Ellipse drawing

Our coordinate system: Z points up, Y points away from the observer to
the antenna, X points right as seen from the observer. This is a right
handed coordinate system. The right-hand rule holds, to determine which
is the positive rotation angle around an axis, point your right-hand
thumb in the direction of the positive axis, then the fingers point in
the direction of the positive rotation angle.

To sum up:

- Measure l1, l2 of ellipse and compute beta = arccos (l2 / l1)
- Measure alpha: angle between l1 and vertical Z-axis, positive angles
  turn the ellipse right, we measure by how much ellipsis needs to be
  turned to be upright
- In the real world determine psi, our angle to the antenna. If we're
  higher than the antenna, the angle is positive, if we're lower,
  negative. If we're the same height psi = 0.
- Compute theta, phi, gamma::

    theta=-asin(sin(alpha)*sin(beta))
    phi=-asin((cos(alpha)*sin(beta))/cos(theta))
    gamma=asin((cos(phi)*sin(theta))/sin(beta))

- Compute theta_r, phi_r, xi::

    theta_r=asin(cos(psi)*sin(theta)+cos(phi)*sin(psi)*cos(theta))
    phi_r=asin((sin(phi)*cos(theta))/cos(theta_r)) 
    xi=-asin((sin(phi)*sin(psi))/cos(theta_r))

Now theta_r is the real elevation of the antenna and phi_r is the real
(well uncorrected, we're still asuming we're in the north of the
antenna) azimuth.

Azimuth correction (correcting the asumption that we're north of the
antenna) is left as an exercise.

OpenScad
--------

This project contains an OpenScad file to simulate the rotation. The
antenna without rotation (azimuth = 0, elevation = 0) points to the
observer. You can rotate the antenna:

- By specifying a non-zero elevation
- By specifying a non-zero azimuth
- By specifying a non-zero phi-angle between observer and antenna, a
  possitive angle means the observer is higher than the antenna

Rotations in openscad get an object to rotate as parameter, so the
following code::

 rotate ([0, 0, -51.066])
 rotate ([0, 62.966, 0])
 schuessel (ele = 60, azi = 45, psi = 20)

Specifies a dish (Schüssel in German) with 60° elevation and 45°
azimuth where the observer is located 20° above the antenna. This
antenna is then rotated by 62.966° around the Y-axis, then around the
Z-axis by -51.066°.

After starting openscad with ``ellipse.scad``, you want to select
``Front`` from the ``View`` menu. An un-rotated antenna is visible as a
circle (so it points at the observer). The inside of the antenna is
yellow, the backside is green.
