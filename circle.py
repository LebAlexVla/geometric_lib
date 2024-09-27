import math


def area(r):
    '''
    Returns the area of a circle with a given radius

        Parameters:
            r (double): floating point radius

        Constants:
            math.pi (double): number pi
        
        Return values:
            circle_area (double): floating point area of a cicle
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Returns the perimeter of a circle with a given radius

        Parameters:
            r (double): floating point radius

        Constants:
            math.pi (double): number pi

        Return values:
            circle_perimeter (double): floating point perimeter of a cicle
    '''
    return 2 * math.pi * r

