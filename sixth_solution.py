def read_coordinates(i, limit, array_coordinates):
    if (i < limit):
        array_coordinates.append(int(input()))
        return read_coordinates(i + 1, limit, array_coordinates)
    else:
        return array_coordinates

def get_triangles():
    first = read_coordinates(0, 3, [])
    second = read_coordinates(0, 3, [])
    return first, second

def read_coef():
    return int(input())

def multiply_lengthes(arrays, coef, i, limit):
    if (i < limit):
        arrays[0][i] *= coef
        arrays[1][i] *= coef
        return multiply_lengthes(arrays, coef, i + 1, limit)
    else:
        return arrays

def get_vectors(arrays, i, limit, vector_array):
    if (i < limit):
        vector_array.append(arrays[1][i] - arrays[0][i])
        return get_vectors(arrays, i + 1, limit, vector_array)
    else:
        return vector_array

def main():
    print(get_vectors(multiply_lengthes(get_triangles(), read_coef(), 0, 3), 0, 3, []))

main()

