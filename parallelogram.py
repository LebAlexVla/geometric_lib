def area(a, h):
    '''
    Returns the area of a parallelogram with a given base and height

        Parameters:
            a (double): floating point base
            h (double): floating point height
        
        Return values:
            parallelogram_area (double): floating point area of a parallelogram
    '''
    return a * h

def perimeter(a, b):
    '''
    Returns the perimetr of a parallelogram with given sides

        Parameters:
            a (double): floating point side
            b (double): floating point adjacent side
        
        Return values:
            parallelogram_perimeter (double): floating point perimeter of a parallelogram
    '''
    return 2 * (a + b)