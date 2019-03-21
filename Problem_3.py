#Required Packages
import numpy as np
from matplotlib import pyplot as pt

#Predefined Quantities
#Mesh sizes in a decreasing order
h = [1*10**-1,5*10**-2,1*10**-2,5*10**-3,1*10**-5]

#Function and Analytic Derivative
f = lambda x: 4*np.cos(x)+3*np.sin(x)+2
fp= lambda x:-4*np.sin(x)+3*np.cos(x)

#Finite Difference Operators
Dp= lambda x, h: (f(x+h)-f(x))/h
Dm= lambda x, h: (f(x)-f(x-h))/h
D0= lambda x, h: (f(x+h)-f(x-h))/(2*h)

#Error Calculation
x_bar = 1.2   #PArticular Point

#Error calculation loop
E = []
for i in xrange(5):

    #Errors in the L^2 norm
    E = E + [np.array([np.linalg.norm(fp(x_bar)-Dp(x_bar,h[i])),
                       np.linalg.norm(fp(x_bar)-Dm(x_bar,h[i])),
                       np.linalg.norm(fp(x_bar)-D0(x_bar,h[i]))])]
E = np.array(E)
print E

#Convergence Plots
pt.loglog(h,E.T[0])
pt.loglog(h,E.T[1])
pt.loglog(h,E.T[2])
pt.legend([r'$D_+$',r'$D_-$',r'$D_0$'])
pt.title('Convergence Log-Log Plots')
pt.xlabel(r'h')
pt.ylabel(r'E')

#Order of Accuracy
print 'Convergence rates of the operators:'
print r'for $D_+$ {}'.format(np.log(E.T[0][0]/E.T[0][4])/np.log(h[0]/h[4]))
print r'for $D_-$ {}'.format(np.log(E.T[1][0]/E.T[1][4])/np.log(h[0]/h[4]))
print r'for $D_0$ {}'.format(np.log(E.T[2][0]/E.T[2][4])/np.log(h[0]/h[4]))
