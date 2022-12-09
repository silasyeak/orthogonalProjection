##orthogonal projection
from fractions import Fraction
import numpy as np

def orthogonalProj(x, y, z):
    if z == "f":
        return np.dot(Fraction(np.dot(x,y),np.dot(y,y)), y)
    elif z == "n":
        return np.dot(np.dot(x,y)/np.dot(y,y),y)
    

def arrrayProjection():
    ##a is the projection
    
    a = np.array([2,4,0,-1])
    b = np.array([2,0,-1,-4])
    c = np.array([5,-2,2,2])

    z = input("If you want the output to show a fraction, type 'f', else 'n':")
    ##if you want to add more arrays to the dot product, and z is just the input
    ##just dot with respect to a i.e. dot_x = orthogonalProj(a, x, z)
    dot_1 = orthogonalProj(a, b, z)
    dot_2 = orthogonalProj(a, c, z)


    list = [dot_1, dot_2]
    totalSum = 0

    for i in list:
        print("Matrix:", i)
        totalSum += i

    print("Total Sum:", totalSum)


def innerProduct():
    ptp0 = 0
    p0p0 = 0
    ptp1 = 0
    ptp2 = 0
    p1p1 = 0
    p2p2 = 0
    for t in range(-2,3):
        pt = 3*t**3
        p0 = 3
        p1 = 4*t
        p2 = t**2-2
        ptp0 += pt*p0
        p0p0 += p0*p0
        ptp1 += pt*p1
        ptp2 += pt*p2
        p1p1 += p1*p1
        p2p2 += p2*p2

    print("ptp0:", ptp0)
    print("p0p0:", p0p0)
    print("ptp1:", ptp1)
    print("ptp2:", ptp2)
    print("p1p1:", p1p1)
    print("p2p2:", p2p2)

        
def main():
    x = input("if Array Projection, type 'a'. If Inner Product, type 'i':")
    if x == "a":
        arrrayProjection()
    elif x == "i":
        innerProduct()
    
    

main()
