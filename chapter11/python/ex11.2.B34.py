# Gauss-Generalized Laguerre quadrature
from numpy import sin, arctan, exp, inf
from scipy.special import roots_genlaguerre
from scipy.special import gamma  # for unit-test
         # Function f(x) 
def f(x):
   return sin(k * x) 
         # Give the exact solution for unit test
def exactSolution(x):
   return (b*b+k*k)**(-(a+1)/2)*gamma(1+a)*sin(k*x+(1+a)*arctan(k/b)) 
      # unit test
# global Parameters
a = -0.5  # a(lpha) = -0.5
b = 2.8   # b(eta) = 2.8
k = 2     # k in sin(k x)
x = 0     # in integrand
n = 20    # Number of quadrature points

# only once : roots and weights for the generalized 
# Gauss-Laguerre quadrature 
h, w = roots_genlaguerre(n, a)
# Print the roots and weights
print("Roots:", h)
print("Weights:", w)

t = h/b                # coordinate transform b*t = h
dV =  b**(-(1+a))      # volume element 

# Compute the integral as a sum of weighted function calls
for i in range(0, 10):
   x = 0.1 * i
   result = dV * sum(w * f(x + t))
   errrel = (result - exactSolution(x)) / result
   print("Result x, y, errrel:", x, result, errrel)
