"""the prgramme to know the mass enclosed within a given distance from the centre of this distribution casting the problem as aquadrature problem and solving it numerically .Plot the mass as a function of distance from the centre out to 10 m."""
from scipy.integrate import *
from numpy import *
import matplotlib.pyplot as plt
p=10.0   #density of the distribution #
def fun(x):
    return 4*pi*x*x
x=linspace(0,10,1000)
M=[]
for i in x:
    m=romberg(fun,0,i)
    M= append(M,m)          #creating the array for the mass #
    
plt.plot(x,M)
plt.xlabel("distance in meter from the centre of the distribution(x)")
plt.ylabel("mass enclosed(M)")
plt.title("MASS in kg AS A FUNCTION OF TIME ")
plt.Axes.autoscale
plt.show()
