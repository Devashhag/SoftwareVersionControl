import math

def heurestic_fn(a, b):

    distance = math.sqrt((a.i - b.i)**2 + (a.j - b.j)**2)
    return distance

def manhattan(a,b):
    distance=abs(a.i-b.i)+abs(a.j-b.j)
    return distance/2