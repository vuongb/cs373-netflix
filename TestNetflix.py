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


# -----------
# TestPFD
# -----------

class TestPFD (unittest.TestCase) :

    # ----
    # testTest
    # ----
    def testTest (self) :
        self.assert_(True)


# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."