'''Various numpy helper functions''''
import numpy as np

def sort_array(array):
    '''returns a sorted numpy array'''
    indices = np.argsort(array)
    return(array[indices])

def euclidian_distance(vector1, vector2):
    return(np.linalg.norm(vector1-vector2))
