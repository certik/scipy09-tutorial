from sympy import *
var("x y z")

# FACTORING

e = (x+y+z)**2
e
e.expand()
factor(e.expand())

# INTEGRATION

integrate(sin(x)*exp(x), x)
integrate(sin(x)*exp(2*x), x)
integrate(1/(x**2+1), x)
integrate(1/(x**4+1), x)
integrate(x/(x**2+1), x)
integrate(x/(x**2+1), x).diff(x)
simplify(integrate(x/(x**2+1), x).diff(x))

a = integrate(LambertW(x), x)
a.diff(x)
trim(a)
var('a b')
a = integrate(a*LambertW(b*x), x)
a.diff(x)
trim(a)
integrate(sin(2*sqrt(x)), x)
f = (x-tan(x))/tan(x)**2 + tan(x)
integrate(f, x)



e = Integral(sin(x), (x, 0, pi))
from scipy.integrate import quad
f = lambdify(e.args[1][0][0], e.args[0])
quad(f, e.args[1][0][1][0], e.args[1][0][1][1])

# see the bug, show how to fix it.
# ipdb:

#ipdb> mlib.mpf_eq?
#*** SyntaxError: invalid syntax (<stdin>, line 1)

# -> better is ipython embed
