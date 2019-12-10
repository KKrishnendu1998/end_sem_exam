"""question number 5
creator : Krishnendu Maji"""
from numpy import *
from scipy.interpolate import *
import matplotlib.pyplot as plt
theta= loadtxt("C:/Users/user/Desktop/data.txt",usecols=[0])
d= loadtxt("C:/Users/user/Desktop/data.txt",usecols=[1])
print(theta)
print(d)
polynomial = lagrange(theta, d)
x=linspace(0.1,10,1000)
plt.plot(x, polynomial(x),label='interpolated data')
plt.scatter(theta,d,color='red',label='theorist data')
plt.title('theorist and interpolated graphs')
plt.xlabel('theta')
plt.ylabel('d')
plt.legend(loc = 'upper right', frameon = True, shadow = True)
plt.show()
