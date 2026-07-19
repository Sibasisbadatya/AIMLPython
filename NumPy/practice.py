import numpy as np 
# custom type 
import numpy as np 
x = np.zeros((2,2), dtype=[('x', 'i4'), ('y', 'i4')])  
print(x)
print(x['x'])
print(x['y'])