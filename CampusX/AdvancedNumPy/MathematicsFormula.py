import numpy as np

# numpy has some its builtin mathematical functions which are very useful and we can directly use them without writing the code for it
# but for customise function we have to write the code from our own. 
# Sigmoid (1/(1+e^-x))

def sigmoid(x):
    return 1/(1+np.exp(-x))

a = np.arange(10)
sigmoid_a = sigmoid(a)
print(sigmoid_a)

# Mean squared error
# MSE measures how far your predictions are from actual values

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

a = np.random.randint(1,100,20)
b = np.random.randint(1,100,20)

mse = mse(a,b)
print(mse)




