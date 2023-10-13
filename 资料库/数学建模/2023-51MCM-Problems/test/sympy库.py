import sympy
import sympy as sym
from sympy import exp,log,sqrt,ln
from sympy.abc import t,h,e,k,m,g,r,v
from sympy import diff,integrate
from sympy import  simplify
from sympy import  nsolve,solve,pprint,Eq
# print(sym.solve([x + y - 1,x - y -3],[x,y]))

# def ln(x):
#     return log(x,e)
# h=300
# v0=300/3.6
# k=0.02
# g=9.8
# m=50
# vf=5
# t=ln(exp(k*h/m)+sqrt(exp(2*k*h/m)-1))/(sqrt(k*g/m))
# print(t)
# print(simplify(t))
# eql=Eq()
print(solve(t*2-4,t))
tt=m/k*ln((exp(2*sqrt(k*g/m)*t)+1)/2)-sqrt(m*g/k)*t
pprint(tt)
print(sympy.solve(Eq(m/k*ln((exp(2*sqrt(k*g/m)*t)+1)/2)-sqrt(m*g/k)*t,h),t))
print(m/k*ln((exp(2*sqrt(k*g/m)*t)+1)/2)-sqrt(m*g/k)*t)
pprint(simplify(m/k*ln((exp(2*sqrt(k*g/m)*t)+1)/2)-sqrt(m*g/k)*t))
# sol=solve(m/k*ln((exp(2*sqrt(k*g/m)*t)+1)/2)-sqrt(m*g/k)*t-h,t)
# print(simplify(sol[0]))
# # # print(t)
# #
# r=m*v/(k*v*t+m)
# pprint(integrate(r,t))
# pprint(sqrt(g*m/k)*(-h*k*log(e) + m*log((e**(h*k/m) + sqrt(e**(2*h*k/m) - 1))**2/2 + 1/2))/(g*m*log(e)))



