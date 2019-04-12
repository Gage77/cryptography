import binascii

mult_mat = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

inv_mat = [
    [14, 11, 13, 9],
    [9, 14, 11, 13],
    [13, 9, 14, 11],
    [11, 13, 9, 14]
]

# Transpose the matrix to swap columns with rows
def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

# Perform multiplation withing galois field
def galois_multiplation(x, y):
    k = 0
    n = 0
    for i in range(8):
        if y & 1 == 1:
            k ^= x
        n = x & 0x80
        x <<= 1
        if n == 0x80:
            a ^= 0x1b
        y >>= 1
    return k % 256

def mix_columns(matrix):
    tmat = transpose(matrix)
    print(tmat)
    # Convert each element in matrix to hex value
    for row in matrix:
        for i in range(len(row)):
            row[i] = binascii.hexlify(row[i])
    for col in tmat:
        temp_mat = col.copy()
        col[0] = galois_multiplation(temp_mat[0], 2) ^ galois_multiplation(temp[3], 1) ^ galois_multiplation(temp[2], 1) ^ galois_multiplation(temp[1], 3)
        col[1] = galois_multiplation(temp_mat[1], 2) ^ galois_multiplation(temp[0], 1) ^ galois_multiplation(temp[3], 1) ^ galois_multiplation(temp[2], 3)
        col[2] = galois_multiplation(temp_mat[2], 2) ^ galois_multiplation(temp[1], 1) ^ galois_multiplation(temp[0], 1) ^ galois_multiplation(temp[3], 3)
        col[3] = galois_multiplation(temp_mat[3], 2) ^ galois_multiplation(temp[2], 1) ^ galois_multiplation(temp[1], 1) ^ galois_multiplation(temp[0], 3)

    tmat = transpose(tmat)
    print(tmat)

def main():

    final_mat = [
        [b'O', b'K', b'L', b'A'],
        [b'H', b'O', b'M', b'A'],
        [b'I', b'L', b'L', b'I'],
        [b'N', b'O', b'I', b'S']
    ]

    mix_columns(final_mat)

if __name__ == '__main__':
    main()
