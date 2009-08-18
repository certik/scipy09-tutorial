# INTEGRATION

from sympy import *
var("x y z")
e = Integral(sin(x), (x, 0, pi))
from scipy.integrate import quad
f = lambdify(e.args[1][0][0], e.args[0])
quad(f, e.args[1][0][1][0], e.args[1][0][1][1])

# see the bug, show how to fix it.

# FACTORING

In [1]: e = (x+y+z)**2

In [2]: e
Out[2]: 
           2
(x + y + z) 

In [3]: e.expand()
Out[3]: 
                         2    2    2
2⋅x⋅y + 2⋅x⋅z + 2⋅y⋅z + x  + y  + z 

In [4]: factor(e.expand())
Out[4]: 
           2
(x + y + z) 
