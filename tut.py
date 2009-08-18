from sympy import *
var("x y z")
e = Integral(sin(x), (x, 0, pi))
from scipy.integrate import quad
f = lambdify(e.args[1][0][0], e.args[0])
quad(f, e.args[1][0][1][0], e.args[1][0][1][1])

# see the bug, show how to fix it.
