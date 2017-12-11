'''Various numpy helper functions''''

def sort_array(array):
    '''returns a sorted numpy array'''
    indices = np.argsort(array)
    return(array[indices])
