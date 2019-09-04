def readNumber():
    return int(input())

def readArray(streamArray, n, i):
    if (i < n):
        streamArray.append(int(input()))
        return readArray(streamArray, n, i + 1)
    else:
        return streamArray

def show(result):
    print(result)
    
def countSum(a, i, sum):
    n = len(a)
    if (i < n):
        return countSum(a, i + 1, sum + a[i])
    else:
        return sum

def main():
    show(
        countSum(
            readArray(
                [], 
                readNumber(), 
                0),
            0,
            0))
    return 0

main()