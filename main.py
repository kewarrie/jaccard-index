'''
The Jaccard coefficient measures similarity between finite sample
sets, and is defined as the size of the intersection divided by
the size of the union of the sample sets:

            |AnB|
J(A,B) = -----------
            |AUB|

By design: 0 <= J(A,B) <= 1

'''     

A = {1, 2, 3, 4, 6}
B = {1, 2, 5, 8, 9}

# Intersaction and Union of two sets can also be done using & and | operators.
C = A.intersection(B)
D = A.union(B)
J = float(len(C))/float(len(D))

print('AnB = ', C)
print('AUB = ', D)
print('J(A,B) = ', J)
