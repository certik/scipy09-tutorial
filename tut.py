from sympy import *
var("x y z n")

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

# General relativity example

# $ examples/advanced/relativity.py


# Integrals table

from sympy import *

def derivative_table(functions, x):
    for f in functions:
        s = printing.latex(Eq(Derivative(f, x), diff(f, x)))
        print ":<math>" + s[1:-1] + "</math>", "\n"

def integral_table(functions, x):
    for f in functions:
        s = printing.latex(Eq(Integral(f, x), integrate(f, x)))
        print ":<math>" + s[1:-1] + "</math>", "\n"

var('x')

print "===Derivatives==="
derivative_table([cos(x)/(1 + sin(x)**i) for i in range(1, 5)], x)

print "===Integrals==="
integral_table([x**i * exp(i*x) for i in range(1, 5)], x)


# Million digits of pi

a = pi.evalf(10**6)
len(str(a))
str(a)[:50]


# Numerical Integration

# One-liner:

Integral(sin(1/x), (x, 0, 1)).transform(x, 1/x).evalf(quad="osc")
# 0.504067061906928

# Detailed steps:

e = Integral(sin(1/x), (x, 0, 1))
e
e.transform(x, 1/x)
e.transform(x, 1/x).evalf(quad="osc")
e.transform(x, 1/x).evalf(40, quad="osc")

# Numerical Summation

# quickly convergent series:

Sum((2*n**3+1)/factorial(2*n+1), (n, 0, oo)).evalf(1000)

# slowly convergent (polynomial rate) series:

Sum(n/(n**3+9), (n, 1, oo)).evalf(1000)

# Numerical Simplification

a = float(1/7)
nsimplify(a)
a = float(1/81)
nsimplify(a)
nsimplify(pi, tolerance=0.01)
nsimplify(pi, tolerance=0.001)
nsimplify(0.33333, tolerance=1e-4)
nsimplify(4.71, [pi], tolerance=0.01)
nsimplify(2.0**(1/3.), tolerance=0.001)
nsimplify(2.0**(1/3.), tolerance=0.001, full=True)
nsimplify(4/(1+sqrt(5)), [GoldenRatio])
nsimplify(2 + exp(2*atan('1/4')*I))
nsimplify((1/(exp(3*pi*I/5)+1)))
nsimplify(I**I, [pi])
nsimplify(Sum(1/n**2, (n, 1, oo)), [pi])
nsimplify(gamma('1/4')*gamma('3/4'), [pi])

# Ordinary differential equations

f = Function("f")
e = Eq(f(x).diff(x, x) + 9*f(x) + 1, 1)
dsolve(e, f(x))

e = Eq(f(x).diff(x, x) + 8*f(x) + 1, 1)
dsolve(e, f(x))


# Limits

# sympy/series/tests/test_demidovich.py
# e.g.:

sqrt3 = lambda x: x**(S(1)/3)
limit((sqrt3(x**2)-2*sqrt3(x)+1)/(x-1)**2, x, 1)
