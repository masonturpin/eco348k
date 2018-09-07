import numpy as np
print 1+1
print 1+ 0.0
print 1/2
print 1/2.0

eric = 'eric'
print eric[1]

list0 = [3.0, 'r', 1, 'c']
print list0[-1]
print list0[1:len(list0) - 1]

for i in list0:
    print i

for i in eric:
    print i

print True and True
print True and False
print True and not False

list1 = np.array( [0.0, 0.0, 0.0] )
list2 = np.array( [0, 0, .9] )
list3 = np.array( [.9, .9, .9], dtype=np.int16 )

print list1
print list2
print list3

list4 = np.array( [5, 1, 3.0], dtype = np.int16 )
print list4

matrix1 = [[ 'a', 'b', 'c'],
            ['e', 'f', 'g']]

matrix2 = [[ 'a', 'b', 'c'],
            ['e', 'f', 1.0]]

print matrix1[1][0]
print np.array(matrix1)
print np.array(matrix2)

matrix3 = [[0, 0, 0],
            [.9, .9, .9]]

matrix4 = [[.9, .9, .9],
            [.9, .9, .9]]

print np.array(matrix3)
print np.array(matrix3, dtype = object)
print np.array(matrix4, dtype = np.int16)
