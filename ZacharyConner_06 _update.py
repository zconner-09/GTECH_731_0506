#######################################################
# Zachary Conner
# GTECH 731 HW 6
#
# The following code is a comparison of the average nearest neighbor calculation
# done in arcpy and in pure python.
#
# The first code takes a shapefile as an input, and performs the calculation.
#
# The second code is a pure python solution for this calculation.
# -GeoJSON is taken as input
# -Coordinates are read into a list
# -A nested loop is created to calculate distance to each point
# -The minimum of the distances is calculated
# -The average of the minimum is calculated
######################################################
# Arcpy Solution
######################################################
import arcpy as ap

ap.env.workspace = r'C:\Users\zconner\Downloads\hw_6\hw_6\files\shape_files'
file = 'manh_elementary_schools.shp'
nn_output = ap.AverageNearestNeighbor_stats(file, "EUCLIDEAN_DISTANCE", "GENERATE_REPORT", 635000000)

print(" The ArcPy Nearest Neighbor is ", nn_output)
expected = nn_output[3]
#####################################################
# Pure Python Solution                              
#####################################################
import math
import json

man_area = 635000000
coords = []

with open(r"C:\Users\zconner\Downloads\hw_6\hw_6\files\manh_elementary_schools.geojson") as f:
    data = f.read()
    d = json.loads(data)
    for feature in d["features"]:
        pts = feature["geometry"]["coordinates"]
        coords.append(pts)

distDict = {}

for loc in coords:
    distDict[tuple(loc)] = []
    newCoords = [i for i in coords if i != loc]
    for otherLoc in newCoords:
        dist = math.sqrt((loc[0] - otherLoc[0])**2 + (loc[1] - otherLoc[1])**2)
        distDict[tuple(loc)].append(dist)

minDists = [min(dists) for loc,dists in distDict.items()]
avginDist = sum(minDists)/len(minDists)

pp_output =  avginDist/float(expected)

print('Pure Python nearest neighbor is ', pp_output)

