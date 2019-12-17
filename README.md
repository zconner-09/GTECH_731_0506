# GTECH_731_0506
Homework assignment 5/6 for GTECH 731. The idea with this homework is to take a basic GIS algorithm, and implement it once in pure Python, and once in ArcPy, and to compare the results. 

The specific problem below should exercise a few of the different things we have covered so far, but you can also pick a different tool if you prefer - just be sure to pick something where you have a good grasp of the solution.  

The nearest neighbor index describes the distribution of points, a value of less than one suggesting clustered, close to one random, and greater than one more evenly dispersed.  A description is here:

http://desktop.arcgis.com/en/arcmap/10.6/tools/spatial-statistics-toolbox/average-nearest-neighbor.htm

For the ArcPy portion of the assignment, the ArcGIS help should be enough to get you started. 

For your pure Python solution, there will be a few steps.  it should be possible to do it using plain Python without Point objects or any special libraries, although the Xaio book does have an example using his geometry classes.  The main calculation would be the average nearest neighbor distance, which requires steps along these lines:

 -- Read in the points
 -- For each point
 -- Calculate the distance to all other points (i.e., nested loops)
 -- Find the minimum of these distances
 -- Calculate the average minimum distance across all points

Once this average nearest neighbor distance is calculated, it can then divided by the expected average nearest neighbor distance if the distribution were random, resulting in a single index value.  
