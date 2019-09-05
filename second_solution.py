def get_number():
    return int(input())

def check_numbers(number,  result, i):
    if (number == 0):
        return result
    last_number = is_number_odd(get_last_number(number))
    if (last_number != 0):
        result = get_result(result, last_number, i)
        i += 1
    return check_numbers(number // 10, result, i)

def get_degree(i, degree, multiplication):
    if (i < degree):
        return get_degree(i + 1, degree, multiplication * 10)
    else:
        return multiplication

def get_result(old_number, new_number, i):
    multiptication = get_degree(0, i, 1)
    return new_number * multiptication + old_number

def get_last_number(number):
    return number % 10

def is_number_odd(number):
    if (number % 2 == 1):
        return number
    else:
        return 0

def main():
    print(check_numbers(get_number(), 0, 0))
    return 0

main()