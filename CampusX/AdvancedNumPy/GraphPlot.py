import numpy as np
# y=x graph
a = np.linspace(0,10,100)  # 100 points between 0 and 10
b = a
import matplotlib.pyplot as plt
# plt.plot(a,b) #only prepares the graph
# plt.show()  # displays the graph

# y = x^2 graph
a = np.linspace(-10,10,100)
b = a**2
# plt.plot(a,b)
# plt.show()

# y=sin(x) graph
a = np.linspace(-10,10,100) 
b = np.sin(a)
# plt.plot(a,b)
# plt.show()

# y=xlog(x) graph
a = np.linspace(0.1,10,100)  # we start from 0.1 because log(0) is undefined
b = a * np.log(a)
plt.plot(a,b)
plt.show()
