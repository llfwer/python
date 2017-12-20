import numpy as np

x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]])
print(x)
print(x.T)
print(x.flat[2:4])
print(x.size)
print(x.shape)
