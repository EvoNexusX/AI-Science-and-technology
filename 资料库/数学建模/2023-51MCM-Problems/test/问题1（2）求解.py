# from math import e
# from math import sqrt
# from math import log
from sympy import exp,ln,sqrt
h=300
v0=300/3.6
k=0.04
g=9.8
m=50
vf=5
# def ln(x):
#     return log(x,e)

t=ln(exp(k*h/m)+sqrt(exp(2*k*h/m)-1))/(sqrt(k*g/m))

# 无风速初始值
Sx=m/k*ln(v0*sqrt(k/(m*g))*ln(exp(k*h/m)+sqrt(exp(2*k*h/m)-1))+1)
print(Sx)
Sy=0
Sz=h
x=sqrt(Sx**2+Sy**2)
d=sqrt(Sx**2+Sy**2+Sz**2)

print("物资飞行时间:",t)
print("无风速情况下物体沿水平面移动距离为:",x)
print("无风苏情况下直线距离为:",d)
print()
# 风速与飞行速度同向

Sx1=Sx+vf*t
Sy1=Sy
Sz1=Sz
x1=sqrt(Sx1**2+Sy1**2)
d1=sqrt(Sx1**2+Sy1**2+Sz1**2)

print("风向与飞行速度方向同向情况下物体沿水平面移动距离为:",x1)
print("风向与飞行速度方向同向情况下投放距离为:",d1)
print()
# 风速与飞行速度方向反向

Sx2=Sx-vf*t
Sy2=Sy
Sz2=Sz
x2=sqrt(Sx2**2+Sy2**2)
d2=sqrt(Sx2**2+Sy2**2+Sz2**2)

print("风向与飞行速度方向反向情况下物体沿水平面移动距离为:",x2)
print("风向与飞行速度方向反向情况下投放距离为:",d2)
print()

# 风速与飞行速度方向垂直
Sx3=Sx
Sy3=Sy+vf*t
Sz3=Sz
x3=sqrt(Sx3**2+Sy3**2)

d3=sqrt(Sx3**2+Sy3**2+Sz3**2)
print("风向与飞行速度方向垂直情况下物体沿水平面移动距离为:",x3)
print("风向与飞行速度方向垂直情况下投放距离为:",d3)
print()
