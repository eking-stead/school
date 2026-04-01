import numpy as np

mat1 = [
        [30, 45, 30],
        [28, 32, 25]
        ]

mat2 = [
        [1, 0, 0],
        [.7, .4, 0],
        [.9, 0, .15]
        ]

# top left: 30*1+45*.7+30*.9

mat = np.dot(mat1, mat2)

print(mat)

print("====")

mat1Flipped = [
        [1, .7, .9],
        [0, .4, 0],
        [0, 0, .15]
        ]

mat2Flipped = [
        [30, 28],
        [45, 32],
        [30,25]
        ]





matOut = np.dot(mat1Flipped, mat2Flipped)

print(matOut)
