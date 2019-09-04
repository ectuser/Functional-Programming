def read_number():
    return int(input())

def read_array(stream_array, n, i):
    if (i < n):
        stream_array.append(int(input()))
        return read_array(stream_array, n, i + 1)
    else:
        return stream_array

def show(result):
    print(result)
    
def count_sum(a, i, sum):
    n = len(a)
    if (i < n):
        return count_sum(a, i + 1, sum + a[i])
    else:
        return sum

def main():
    show(
        count_sum(
            read_array(
                [], 
                read_number(), 
                0),
            0,
            0))
    return 0

main()