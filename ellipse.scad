module schuessel (r = 20, t = 0.1, ele = 30, azi = 45)
{
    rotate ([0, 0, azi])
    rotate ([-ele, 0, 0])
    rotate ([-90, 0, 0])
        difference () {
        union () {
            cylinder (r = r, h = t);
            translate ([0, -r, 0])
                cylinder (r = 1, h = t);
        }
        translate ([0, 0, t / 2])
            cylinder (r = 2*r, h = t);
        }
}

// This is the case ele = 30, azi = 0
// rotate ([0, -90, 0])
// rotate ([0, 0, -acos (17.3 / 20)])
// rotate ([0, 90, 0])
// schuessel (azi = 0, ele = 30, $fa=1);

// This is the case ele = 60, azi = 0
// rotate ([0, -90, 0])
// rotate ([0, 0, -60])
// rotate ([0, 90, 0])
// schuessel (azi = 0, ele = 60, $fa=1);

// An arbitrary angle
rotate ([0, -40.967, 0])
rotate ([0, 0, -69.3])
rotate ([0, 68, 0])
schuessel (ele = 60, azi = 45, $fa=1);

// This needs no Y-Rotation
// rotate ([0, 0, -90])
// rotate ([0, 60, 0])
// schuessel (ele = 60, azi = 90, $fa=1);

// Another arbitrary example
// rotate ([0, -27, 0])
// rotate ([0, 0, -75.5])
// rotate ([0, 63.5, 0])
// schuessel (ele = 60, azi = 60, $fa=1);

//schuessel (ele = 0, azi = 0, $fa=1);
