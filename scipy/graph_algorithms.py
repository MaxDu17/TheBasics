# there are some graph theoretic operations you can perform with scipy
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

# depth first traversal, breadth first traversal
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order
arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)
# returns traversal order and prdecessors
print(depth_first_order(newarr, 1))
print(breadth_first_order(newarr, 1))


arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

# returns number of components, and labels for each of the nodes
print(connected_components(newarr))

# return distance matrix and predeecessors, which is a matrix that can be used to reconstruct shortest path
print(dijkstra(newarr, return_predecessors=True, indices=0)) # find shortest path
# in this case, we get [0, 1, 2] as distances, which makes sense because we start our search from 0

from scipy.sparse.csgraph import bellman_ford
arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors=True, indices=0))



# all pairs shortest paths
from scipy.sparse.csgraph import floyd_warshall
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

# returns distance matrix and matrix of predecessors (used for reconstruction)
print(floyd_warshall(newarr, return_predecessors=True))
