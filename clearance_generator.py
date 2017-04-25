#!/usr/bin/env python

import re
import random
import subprocess

rate = 250
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


# callsign
clearance.append("Cessna 7 3 3 tango papa")

# route
clearance.append("cleared to %s %s" % (random.choice(routes),
                                       random.choice([route_as_filed,route_via])()))

# directional
clearance.append("flie %s" % (random.choice([fly_rw_ref,fly_heading_ref,fly_heading_ref])()))

# altitude
initial_altitude = random.randint(3,8)
cruise_altitude = random.randint(initial_altitude+1,14)
clearance.append("climb and maintain %s thousand.  expect %s thousand %s minutes after departure" %
                    (initial_altitude,cruise_altitude,
                     random.choice(["5","1 0","1 5"])))

# frequency
clearance.append("departure frequency %s point %s" %
                    (" ".join(list(str(random.randint(108,136)))),
                     random.choice(['',1,2,3,4,5,6,7,8,9,'0 2','0 2 5','0 5 0','7 5'])))

# squak
clearance.append("squawk %s %s %s %s" % (random.randint(1,6),random.randint(0,9),random.randint(0,9),random.randint(0,9)))

# say clearance
subprocess.call(["/usr/bin/say","-r",str(rate),". ".join(clearance)])

print "\n".join(clearance)
print "\n"


