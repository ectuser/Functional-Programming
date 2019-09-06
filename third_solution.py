def read_number():
    return int(input())

def read_km(i, number, km_array):
    if (i < number):
        km_array.append(int(input()))
        return read_km(i + 1, number, km_array)
    else:
        return km_array

def read_price_for_km(i, number, price_array):
    if (i < number):
        price_array.append(int(input()))
        return read_price_for_km(i + 1, number, price_array)
    else:
        return price_array

def read_all_data(number):
    return read_km(0, number, []), read_price_for_km(0, number, [])

def sort_arrays(number):
    first, second = read_all_data(number)
    return sorted(first), sorted(second, reverse=True)

def combine_and_show(arrays, i):
    first = arrays[0]
    second = arrays[1]
    number = len(first)
    if (i < number):
        print(first[i], " ", second[i])
        return combine_and_show(arrays, i + 1)
    

def main():
    combine_and_show(sort_arrays(read_number()), 0)
    


main()