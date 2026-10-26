# Marcus Hernandez
# COMSC 078
# Week 9 Lab (Generic Matrices)

# This file has my GenericMatrix class which does the actual matrix adding and multiplying. 
# Additionally, it has IntegerMatrix and RationalMatrix, which just say how to add and multiply the matrices.
# There's also a small Rational class for the fractions. 

# please note thatThe test program that runs everything is in the TestGenericMatrix.py file

from math import gcd # needed to reduce the fractions down

# simple fraction class, same idea as the Rational class from the book
class Rational: 
    #constructor, reduces the fraction right away
    def __init__(self, numer, denom): # 
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g
        
    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)
    
    def mul(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)
    
    #prints the fraction liek 1/5
    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)
    
#abstract class, I only ever make the subclasses
class GenericMatrix(object):
    """Abstract class that operates on matrices with the saem types of numbers """
    
    def __add__(self, a, b):
        """"adds two elements drawn from matrices"""
        pass # overriden in the subclass

    def __mul__(self, a, b):
        """For multiplying two elements drawn from matrices"""
        pass # overridden in the subclass

    def __zero__(self):
        """Abstract method for defining the zero element for the type of matrix."""
        pass # overridden in the subclass

    def __addMatrix__(self, other):
        """Adds two matrices with the same types of elements and returns the resulting matrix."""
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.__add__(self.matrix[i][j], other.matrix[i][j]))
            result.append(row)
        return result

    def __multiplyMatrix__(self, other):
        """Multiplies two matrices with the same types of elements and returns the resulting matrix."""
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                total = self.__zero__()
                # cij = ai1 * b1j + ai2 * b2j + ... + ain * bnj
                for k in range(len(other.matrix)):
                    total = self.__add__(total, self.__mul__(self.matrix[i][k], other.matrix[k][j]))
                row.append(total)
            result.append(row)
        return result

    def __str__(self):
        """Returns the string representation of the result"""
        text = ""
        for row in self.matrix:
            for x in row:
                text = text + str(x) + "\t"
            text = text + "\n"
        return text
 
 
class IntegerMatrix(GenericMatrix):
    """Allows you to add and multiply the elements in an IntegerMatrix"""
 
    def __init__(self, matrix):
        self.matrix = matrix
 
    def __add__(self, a, b):
        """Adds two integers and return the sum"""
        return a + b
 
    def __mul__(self, a, b):
        """Multplies two integers and returns the product"""
        return a * b
 
    def __zero__(self):
        """Returns 0 for as an integer"""
        return 0
 
 
 
class RationalMatrix(GenericMatrix):
    """Allows you to add and multiply two elements in a RationalMatrix"""
 
    def __init__(self, matrix):
        self.matrix = matrix
 
    def __add__(self, a, b):
        """Add and return the sum of two rational numbers"""
        return a.add(b)
 
    def __mul__(self, a, b):
        """Multiply and return the product of two rational numbers"""
        return a.mul(b)
 
    def __zero__(self):
        """Returns the zero for rational numbers (0/1)."""
        return Rational(0, 1)