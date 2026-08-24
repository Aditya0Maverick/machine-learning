import numpy as np 
array = np.array([[['A','B',''],['W','R',''],['Q','U','']],
                  [['C','D',''],['E','F',''],['A','B','']],
                  [['S','B',''],['A','B',''],['A','B','']]])
print(array.ndim)
print(array.shape)
print(array[0,0,0] + array[2,0,0]+ array[2,0,0])