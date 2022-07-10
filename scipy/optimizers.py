# there is an optimizer that yo ucan use
from scipy.optimize import root
from math import cos
def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)
print(myroot)
print(myroot.x)

## you can find extrema too
from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

# methods:
# 'CG'
# 'BFGS'
# 'Newton-CG'
# 'L-BFGS-B'
# 'TNC'
# 'COBYLA'
# 'SLSQP'

# 0 is the initial guess
mymin = minimize(eqn, 0, method='BFGS')
print(mymin)
