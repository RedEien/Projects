import numpy as np
import matplotlib.pyplot as plt 
from scipy import special
import time
import matplotlib
# plot the function 
x = np.linspace(-1.5, 1.5, 100)
y = np.exp(-x**2)
plt.plot(x,y)
# init params for trapezoid method
x_start = -1
y_start = np.exp(-x_start**2)
x_end = 1
y_end = np.exp(-x_end**2)
h = 1000 #steps
solutions = []
start_time = time.time()
def trapez():
    # area f a trapez = 0.5*(y1 + y0)*(x1 - x0)
    x_h = (x_end - x_start) / h # step size x_start + 
    x_0 = x_start
    y_0 = y_start
    x_1 = x_0 + x_h
    # solution loop for trapez
    for _ in range(h):
        y_1 = np.exp(-x_1**2) 
        # plot trapez
        plt.fill_between([x_0, x_1], [y_0, y_1])
        # list with solutions
        solution = 0.5 * (y_1 + y_0) * (x_1 - x_0)
        solutions.append(solution)
        x_0 += x_h
        y_0 = y_1
        x_1 += x_h
# main
trapez()
plt.xlim([-1.5, 1.5])
plt.ylim([0, 1.5])
# accuracy of the trapezoid method
A_analytical = np.sqrt(np.pi) * special.erf(1) # * 0.5 für 0 -> 1
A_numerical = sum(solutions)
accuracy = A_numerical / A_analytical * 100
print("Sum of trapezoid areas: ", A_numerical)
print("Calculated area: ", A_analytical)
print("the accuracy of the trapezoid method is","{:10.10f}".format(accuracy),"% with ",h," steps in ",time.time()-start_time," seconds")
plt.show()