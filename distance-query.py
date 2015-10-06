##################################################
#
#  This code is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
##################################################

# Standard Libraries

import math

def FXY(fltLng0,fltLat0,fltLng,fltLat):
         
    ##################################################
    #
    # Simplified Spherical Transverse Mercator Projection
    #
    # Inputs (Degrees)
    #
    # Lng0 - Central Meridian (Lng of query origin)
    # Lat0 - Base Latitude (0 for the Equator)
    #
    # Lng/Lat - spherical coords of point to be projected
    #
    # Outputs
    #
    # X/Y - Cartesian Coords of projected point
    #
    # Notes
    #
    # Originally coded in VB.net
    #
    ##################################################
        
    # Declarations

    fltR = 6367445.0            # Approx. Radius of Earth
        
    # Convert to radians
        
    fltLat0 *= math.pi / 180.0
    fltLng0 *= math.pi / 180.0
        
    fltLat *= math.pi / 180.0
    fltLng *= math.pi / 180.0
        
    # Covenience variable
        
    fltB = math.cos(fltLat) * math.sin(fltLng - fltLng0)
        
    # Forward - X/Y
        
    fltX = fltR * math.log((1 + fltB) / (1 - fltB)) / 2
    fltY = fltR * (math.atan(math.tan(fltLat) / math.cos(fltLng - fltLng0)) - fltLat0)

    # return

    return (fltX,fltY)
        
def FLngLat(fltLng0,fltLat0,fltX,fltY):
         
    ##################################################
    #
    # Simplified Inverse Spherical Transverse Mercator Projection
    #
    # Inputs (Degrees)
    #
    # Lng0 - Central Meridian (Lng of query origin)
    # Lat0 - Base Latitude (0 for the Equator)
    #
    # Inputs (metres)
    #
    # X/Y - Cartesian Coords of point
    #
    # Ouptut (Degrees)
    #
    # lng/lat - Spherical Coordinates
    #
    # Notes
    #
    # Originally coded in VB.net
    #
    ##################################################
        
    # Declarations
        
    fltR = 6367445.0     # Approx. Radius of Earth
        
    # Convert to radians
        
    fltLat0 *= math.pi / 180.0
    fltLng0 *= math.pi / 180.0
        
    # Convenience variable
        
    fltD = fltY / fltR + fltLat0
        
    # Reverse
        
    fltLat = math.asin(math.sin(fltD) / math.cosh(fltX / fltR))
    fltLng = fltLng0 + math.atan(math.sinh(fltX / fltR) / math.cos(fltD))
        
    # Convert from radians to Degrees
        
    fltLat *= 180.0 / math.pi
    fltLng *= 180.0 / math.pi

    # Return

    return (fltLat,fltLng)

############################################################
#
# Creates a lat/lng bounding box which is a square with
# side of 2*R where R is given in metres.
#
# Reference
#
# http://solar-bucket.co.uk/programming/distance_query.aspx
#
# Note
#
# Code has been used with values of R in the range 5000 to
# 100000 metres
#
############################################################

# Centre of the square (decimal degrees)

fltLng =  -0.167
fltLat = +50.839

# Search radius (metres)

fltR = 10000.0

# Origin of transverse mercator projection

fltLat0 = 0.0
fltLng0 = fltLng

# Centre of square as X/Y (metres)

fltX,fltY = FXY(fltLng0,fltLat0,fltLng,fltLat)

# Bounding box as X/Y (metres)

fltXmin = fltX - fltR
fltYmin = fltY - fltR
fltXmax = fltX + fltR 
fltYmax = fltY + fltR

# Bounding Box as lat/lng (decimal degrees)

fltLngMin,fltLatMin = FLngLat(fltLng0,fltLat0,fltXmin,fltYmin)
fltLngMax,fltLatMax = FLngLat(fltLng0,fltLat0,fltXmax,fltYmax)

# Dump the results

print fltLngMin,fltLatMin,fltLngMax,fltLatMax
        

