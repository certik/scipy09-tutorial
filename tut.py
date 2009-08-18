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



# Linear Solving

var('a b c d e f g h i')
f_1 = a*x + b*y + c*z - 1
f_2 = d*x + e*y + f*z - 1
f_3 = g*x + h*y + i*z - 1
s = solve([f_1, f_2, f_3], x, y, z)
s
f_1.subs(s)
simplify(f_1.subs(s))
simplify(f_2.subs(s))
simplify(f_3.subs(s))

# Nonlinear Solving

f_1 = x**2 + y + z - 1
f_2 = x + y**2 + z - 1
f_3 = x + y + z**2 - 1
solve([f_1, f_2, f_3], x, y, z)

# Factorization

factor(x**56-1, x)
f = x**16+4*x**15+14*x**14+32*x**13+47*x**12+92*x**11+66*x**10+120*x**9 \
    -50*x**8-24*x**7-132*x**6-40*x**5-52*x**4-64*x**3-64*x**2-32*x+16
factor(f, x)

# Term Rewriting

36/(x**5-2*x**4-2*x**3+4*x**2+x-2)
f = apart(36/(x**5-2*x**4-2*x**3+4*x**2+x-2), x)
f = apart(36/(x**5-2*x**4-2*x**3+4*x**2+x-2), x, evaluate=False)
Add(*[ g.doit() for g in f.args ])

# Matrices

M = Matrix(4, 4, lambda i,j: i*j+1)
M.eigenvals()
M = Matrix(4, 4, lambda i,j: i*j+2)
M.eigenvals()
M = Matrix(4, 4, lambda i,j: i*j+3)
M.eigenvals()
M = Matrix(4, 4, lambda i,j: i*j+x)
M.eigenvals()
