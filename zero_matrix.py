# write a function that given an MxN matirix finds the zeros
# and sets rows and columns to zeros
import unittest

def zeros(mat):
    col_to_z = set()
    row_to_z = set()

    for i, r in enumerate(mat):
        for j, c in enumerate(r):
            if c == 0:
                col_to_z.add(j)
                row_to_z.add(i)

    for i, r in enumerate(mat):
        for j, c in enumerate(r):
            if j in col_to_z:
                r[j] = 0
            if i in row_to_z:
                r[j] = 0


my_mat = [[0,0,1],
          [1,1,1],
          [1,0,1],
          [1,1,1],
          [0,1,1]]

print(zeros(my_mat))


class Test(unittest.TestCase):

  def zeros_test(self):
    mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
    mat2 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[2,0,4,0,6]]
    zeros(mat1)
    self.assertEqual(mat1, mat2)

if __name__ == "__main__":
  unittest.main()


  # TODO: fail fast, check if matrix exists