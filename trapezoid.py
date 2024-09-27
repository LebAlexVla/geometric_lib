def area(a, b, h):
    '''
    Returns the area of a trapezoid with given bases and height

        Parameters:
            a (double): floating point base
            b (double): floating point another base
            h (double): floating point height
        
        Return values:
            trapezoid_area (double): floating point area of a trapezoid
    '''
    return (a + b) * h / 2

def perimeter(a, b, c, d):
    '''
    Returns the perimetr of a trapezoid with given sides and bases

        Parameters:
            a (double): floating point side 1
            b (double): floating point side 2
            c (double): floating point base 1
            d (double): floating point base 2
        
        Return values:
            trapezoid_perimeter (double): floating point perimeter of a trapezoid
    '''
    return a + b + c + d