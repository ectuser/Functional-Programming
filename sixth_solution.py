def read_number():
    return int(input())

def read_coordinates(i, limit, array_coordinates, j, number, main_array):
    if (j < number):
        if (i < limit):
            array_coordinates.append({"x" : int(input()), "y" : int(input())})
            return read_coordinates(i + 1, limit, array_coordinates, j, number, main_array)
        else:
            main_array.append(array_coordinates)
        return read_coordinates(0, 3, [], j + 1, number, main_array)
    else:
        return main_array

def read_coef():
    return int(input())

def multiply_lengthes(i, limit, j, main_array, coef):
    number = len(main_array)
    if (j < number):
        if (i < limit):
            main_array[j][i]["x"] *= coef
            main_array[j][i]["y"] *= coef
            return multiply_lengthes(i + 1, limit, j, main_array, coef)
        return multiply_lengthes(0, limit, j + 1, main_array, coef)
    else:
        return main_array

def loop_to_get_vectors(main_array, i, vectors_array):
    number = len(main_array)
    if (i < number):
        vectors_array.append(get_vectors(main_array[i]))
        return loop_to_get_vectors(main_array, i + 1, vectors_array)
    else:
        return vectors_array


def get_vectors(completed_array):
    first_vector = {"x" : completed_array[1]["x"] - completed_array[0]["x"], "y" : completed_array[1]["y"] - completed_array[0]["y"]}
    second_vector = {"x" : completed_array[2]["x"] - completed_array[1]["x"], "y" : completed_array[2]["y"] - completed_array[1]["y"]}
    third_vector = {"x" : completed_array[0]["x"] - completed_array[2]["x"], "y" : completed_array[0]["y"] - completed_array[2]["y"]}
    return first_vector, second_vector, third_vector

def main():
    print(
        loop_to_get_vectors(
            multiply_lengthes( 
                0, 
                3, 
                0, 
                read_coordinates(
                    0, 
                    3, 
                    [], 
                    0, 
                    read_number(), 
                    []
                ),
                read_coef()
            ), 
            0, 
            []
        )
    )
    return 0

main()

