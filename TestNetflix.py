#!/usr/bin/env python

# ---------------------------
# Name  : Ryan J. Prater
#       : Bryan Vuong
# EID   : rp22566
#       : bkv85
# CSID  : rprater
#       :
# CS373 - Downing - Project #3 - Netflix
# ---------------------------

"""
To test the program:
    % python TestNetflix.py >& TestNetflix.out
    % chmod ugo+x TestNetflix.py
    % TestNetflix.py >& TestNetflix.out
"""

# -------
# imports
# -------

import StringIO
import unittest
from Netflix import read_avg_customer_cache, read_avg_movie_cache, compute_estimated_rating, square_diff

# -----------
# TestPFD
# -----------

class TestNetflix (unittest.TestCase) :

    # ----
    # read_avg_customer_cache
    # ----
    def test_read_customer_cache1 (self) :
        size    = 10
        r = StringIO.StringIO("")
        result      = read_avg_customer_cache(r, size)
        self.assert_(result == ([0]*size))

    def test_read_customer_cache2 (self) :
        size    = 5
        r = StringIO.StringIO("1:2\n2:3\n3:4\n4:5\n")
        result      = read_avg_customer_cache(r, size)
        self.assert_(result[1] == 2)
        self.assert_(result[2] == 3)
        self.assert_(result[3] == 4)
        self.assert_(result[4] == 5)

    def test_read_customer_cache3 (self) :
        size    = 51
        r = StringIO.StringIO("48:4\n34:2\n18:2\n42:5\n7:3\n33:4\n")
        result      = read_avg_customer_cache(r, size)
        self.assert_(result[48] == 4)
        self.assert_(result[34] == 2)
        self.assert_(result[18] == 2)
        self.assert_(result[42] == 5)
        self.assert_(result[7] == 3)
        self.assert_(result[33] == 4)


    # ----
    # read_avg_movie_cache
    # ----
    def test_read_movie_cache1 (self) :
        size        = 10
        r           = StringIO.StringIO("")
        result      = read_avg_movie_cache(r, size)
        self.assert_(result == ([0]*size))

    def test_read_movie_cache2 (self) :
        size        = 16
        r           = StringIO.StringIO("15:4\n9:2\n4:5\n12:3")
        result      = read_avg_movie_cache(r, size)
        self.assert_(result[15] == 4)
        self.assert_(result[9] == 2)
        self.assert_(result[4] == 5)
        self.assert_(result[12] == 3)

    def test_read_movie_cache3 (self) :
        size        = 1001
        r           = StringIO.StringIO("1:4\n1000:5\n4:2\n98:3\n998:4\n888:3\n45:3\n555:2\n84:4\n")
        result      = read_avg_movie_cache(r, size)
        self.assert_(result[1] == 4)
        self.assert_(result[1000] == 5)
        self.assert_(result[4] == 2)
        self.assert_(result[98] == 3)
        self.assert_(result[998] == 4)
        self.assert_(result[888] == 3)
        self.assert_(result[45] == 3)
        self.assert_(result[555] == 2)
        self.assert_(result[84] == 4)


    # ----
    # compute_estimated_rating
    # ----
    def test_compute1 (self) :
        x           = 0
        y           = 0
        result      = compute_estimated_rating(x,y)
        self.assert_(type(result) == float)
        self.assert_(result == 0.0)

    def test_compute2 (self) :
        x           = 3
        y           = 4
        result      = compute_estimated_rating(x,y)
        self.assert_(type(result) == float)
        self.assert_(result == 3.5)

    def test_compute3 (self) :
        x           = 1000
        y           = 2000
        result      = compute_estimated_rating(x,y)
        self.assert_(type(result) == float)
        self.assert_(result == 1500.0)


    # ----
    # square_diff
    # ----
    def test_squareDiff1 (self) :
        x           = 1000
        y           = 2000
        result      = square_diff(x,y)
        self.assert_(result == 1000000)

    def test_squareDiff2 (self) :
        x           = 25.8
        y           = 30.3
        result      = square_diff(x,y)
        self.assert_(result == 20.25)

    def test_squareDiff3 (self) :
        x           = 543
        y           = 500
        result      = square_diff(x,y)
        self.assert_(result == 1849)

# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."