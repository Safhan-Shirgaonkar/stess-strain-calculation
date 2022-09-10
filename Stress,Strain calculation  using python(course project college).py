'''calculation of principal stress,inclation of principal stress,maximum shear stress'''

import math
from sympy import *   #sympy library

print("CALCULATION OF PRINCIPAL STRESS,INCLINATION OF PRICIPAL STRES,MAXIMUM SHEAR STRESS")
print("Unit of principal stress is MPa")
print("σ1 (Major principal stress) , σ2 (Minor principal stress)")



#Taking value of principlanes from user suig input function
σx=int(input("Enter The Value Of Principal Plane(σx) in MPa: "))
a=print(f"{σx} MPa")

σy=int(input("Enter The Value of principal Plane(σy) in MPa: "))
b=print(f"{σy} MPa")

τ=int(input("Enter The Value of shear stress(τ) in MPa: "))
c=print(f"{τ} MPa")



σ1=(σx+σy)/2+(math.sqrt((σx-σy)**2 + 4*τ**2)/2)  #formula for calculating major principal stress
print(f"The value of Major principal stress (σ1) is {σ1} MPa")


σ2=(σx+σy)/2-(math.sqrt((σx-σy)**2 + 4*τ**2)/2) #Formula For calculating minor principal stress
print(f"The value of Minor principal stress (σ2) is {σ2} MPa")

#inclination of principal stress
tan2θ=(2*τ)/(σx-σy)   

#calculation of inlcination of principal stresses
e = atan((tan2θ))
pi=22/7
f= (e/2)*(180/pi)
print(f"Inclination of principal stresses {f}°")


#calculating maximum shear stress
τmax=(σ1-σ2)/2
print(f"The value maximum Shear stress is {τmax} Mpa ")





