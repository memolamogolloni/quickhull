# Quickhull

Implementation of one the algorithms used to get the convex hull of a given set of points in R².  Complexity is O(n * log(n)) on its best case and O(n2)  on its worst.



### 1. Installation

This project was developed under Python 3.7 and is using [Pygame](https://github.com/pygame/) library. To install Pygame version used during this project:

```bash
pip3 install -r requirements.txt
```



### 2. Algorithm

* Find the most left and most right points, to define a line that divides the set of points. 
* Look for farthest points in each group and add them to the result.
* Make a triangle from the two initial points and the farthest point just found. Discard the line that connects the initial points and repeat recursively the process from the step before with the leaving ones.
* Stop recursion when there's no points farther than the ones on any of the two lines.





---
PS: maybe quite over-engineered by now, just sketching an architecture for a forthcoming micro-library.