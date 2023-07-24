"""
Transpose means is to interchange rows and columns of a two-dimensional array matrix.
[AT]ij=[A]ji
ie: Formally, the i th row, j th column element of AT is the j th row, i th column element of A:

Example :
[[1,2,3],[4,5,6]].transpose() //should return [[1,4],[2,5],[3,6]]

Write a prototype transpose to array in JS or add a .transpose method in Ruby or create a transpose function in
Python so that any matrix of order ixj 2-D array returns transposed Matrix of jxi .
"""
def transpose(arr):
    new_arr = []
    for i in range(0, len(arr[0])):
        new_line = []
        for j in range(0, len(arr)):
            new_line.append(arr[j][i])
        new_arr.append(new_line)
    return new_arr



print(transpose([[1,2], [3, 4], [5,6]]))


"""
solution from codewars:
return [list(i) for i in zip(*arr)]
"""