#!/usr/bin/env python

import re
import random

datafile = 'holds.nav'


def route_as_filed():
    return("%s as filed" % random.choice(routes))

def route_via():
    return("via %s as filed" % random.choice(routes))

def fly_rw_ref():
    return("runway heading")

def fly_heading_ref():
    heading = random.randint(0,36)*10
    heading_seperate = " ".join(list(str(heading)))
    return("turn %s heading %s" % (random.choice(["left","right"]),
                                   heading_seperate))


# read in routes data
routes = list()
with open(datafile) as fh:
    for l in fh.readlines():
        routes.append(re.sub("\s+.*","",l.split(":")[0]))


clearance = list()

"""
   Cessna 12345 cleared to Nashville as filed, fly runway heading, climb and maintain three thousand, expect seven thousand one zero minutes after departure, departure frequency one two four point six five, squawk two seven one three.
"""

# callsign
clearance.append("Cessna seven three three tango papa")

# route
clearance.append("cleared to %s %s" % (random.choice(routes),
                                       random.choice([route_as_filed,route_via])()))

# directional
clearance.append("fly %s" % (random.choice([fly_rw_ref,fly_heading_ref,fly_heading_ref])()))
#clearance.append("fly %s" % random.choice(

# 

#
# generate random clearance
#


# say clearance
print clearance


