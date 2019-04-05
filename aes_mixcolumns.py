import binascii

def mix_columns(matrix):
    print(matrix)
    # Convert each element in matrix to hex value
    for row in matrix:
        for i in range(len(row)):
            row[i] = binascii.hexlify(row[i])
    print(matrix)

def main():
    mat = [
        [b'O', b'K', b'L', b'A'],
        [b'H', b'O', b'M', b'A'],
        [b'I', b'L', b'L', b'I'],
        [b'N', b'O', b'I', b'S']
    ]

    mix_columns(mat)

if __name__ == '__main__':
    main()
