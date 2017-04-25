#!/usr/bin/env python

import re
import random

datafile = 'holds.nav'


# read in routes data
routes = list()
with open(datafile) as fh:
    for l in fh.readlines():
        routes.append(re.sub("\s+.*","",l.split(":")[0]))


clearance = list()

"""
   “Cessna 12345 cleared to Nashville as filed, fly runway heading, climb and maintain three thousand, expect seven thousand one zero minutes after departure, departure frequency one two four point six five, squawk two seven one three.”
"""

# callsign
clearance.append("Cessna seven three three tango papa")

# route
clearance.append("cleared to %s as filed" % random.choice(routes))

# 

#
# generate random clearance
#


# say clearance


