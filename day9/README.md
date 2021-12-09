# Day 9

For part 1 I just did a simple for loop and compared each point to its neighbors to see
if it was a low point. 

For part 2 I started by computing the low points like in part 1 and then used a UnionFind 
to keep track of clusters (representing basins). For each low point you can check its neighbors
see if they are also in a basin and then add this neighbor to the cluster of the low point. Now
you can just push this neighbor to the stack of low points and repeat until the stack is empty!
