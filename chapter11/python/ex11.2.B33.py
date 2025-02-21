from numpy import sin, arctan, exp, inf
from scipy.integrate import quad
from scipy.special   import gamma  # for unit-test

   # Function f(x) 
def f(x):
   return sin(k * x) 

   # Give the exact solution for unit test
def exactSolution(x):
   return (b*b+k*k)**(-(a+1)/2)*gamma(1+a)*sin(k*x+(1+a)*arctan(k/b)) 

   # Define the integrand
def integrand(h):
   return (h**a) * exp(-b*h) * f(x+h)

# global Parameters
a = -0.5  # a(lpha) = -0.5
b = 2.8   # b(eta) = 2.8
k = 2     # k in sin(k x)
x = 0     # in integrand

for i in range(0, 10):
   x = 0.1 * i
      # Integration with full_output to get detailed information
   result, error, info_dict = quad(
         integrand, 0, inf, args=(),
         epsrel = 3e-8,   # Relative error tolerance
         full_output = True
   )
   errrel = (result - exactSolution(x)) / result
   print("x, y:", x, result)
   print(error priori, posteriori: ", error, errrel )
      # Access the number of subintervals used
   numSubintervals = info_dict['neval']
   print(Number of function calls: ", numSubintervals)