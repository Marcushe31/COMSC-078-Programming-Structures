# Marcus Hernandez
# COMSC 078
# Week 9 Lab (Generic Matrix) - TESTING PROGRAM

# this makes two integer matrices and two rational matricies, then adds and 
# multiplies each pair and prints them side by side like the example. 

from Genericmatrix import IntegerMatrix, RationalMatrix, Rational



# prints m1, m2, and the answer next to each other (with the sign in the middle row)

def print_result(m1, m2, result, op):
    for i in range(len(m1)):
        
        
        line = ""
        for x in m1[i]:
            
            line = line + str(x) + "\t"
        if i == 1:
            line = line + op + "\t"
        else:
            line = line + "\t"
            
        for x in m2[i]:
            line = line + str(x) + "\t"
        if i == 1:
            line = line + "=" + "\t"
        else:
            line = line + "\t"
        for x in result[i]:
            line = line + str(x) + "\t"
        print(line)
        
    print()
 
 
def main():
    # integer matrices
    m1 = IntegerMatrix([[1, 2, 3], [4, 5, 6], [1, 1, 1]])
    
    m2 = IntegerMatrix([[1, 1, 1], [2, 2, 2], [0, 0, 0]])
 
    print("m1 + m2 is")
    print_result(m1.matrix, m2.matrix, m1.__addMatrix__(m2), "+")
    print("m1 * m2 is")
    
    print_result(m1.matrix, m2.matrix, m1.__multiplyMatrix__(m2), "*")
 
 
 
    # rational matrices
    r1 = RationalMatrix([[Rational(1, 5), Rational(1, 6), Rational(1, 7)],
                         [Rational(2, 5), Rational(1, 3), Rational(2, 7)],
                         
                         [Rational(3, 5), Rational(1, 2), Rational(3, 7)]])
    r2 = RationalMatrix([[Rational(1, 6), Rational(1, 7), Rational(1, 8)],
                         
                         [Rational(1, 3), Rational(2, 7), Rational(1, 4)],
                         [Rational(1, 2), Rational(3, 7), Rational(3, 8)]])
 
    print("m1 + m2 is")
    print_result(r1.matrix, r2.matrix, r1.__addMatrix__(r2), "+")
    print("m1 * m2 is")
    print_result(r1.matrix, r2.matrix, r1.__multiplyMatrix__(r2), "*")
 
 
main()