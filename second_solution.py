def get_number():
    return int(input())

def function(number,  result):
    if (number == 0):
        return result
    res = is_number_odd(get_last_number(number))
    if (res != 0):
        print(res)
        result = get_result(result, res)
    return function(number // 10, result)

def get_result(old_number, new_number):
    return old_number * 10 + new_number

def get_modified(number):
    return number / 10

def get_last_number(number):
    return number % 10

def is_number_odd(number):
    if (number % 2 == 1):
        return number
    else:
        return 0

def main():
    print(function(get_number(), 0))
    return 0

main()