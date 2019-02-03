class ListDivideException(Exception):
    pass

def listDivide(numbers,divide=2):
    count = 0
    for x in numbers:
        if x%divide==0:
            count = count+1
    return count

def testListDivide():
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException

    if listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException

    if listDivide([30, 54, 63,98, 100], divide=10) != 2:
        raise ListDivideException

    if listDivide([]) != 0:
        raise ListDivideException

    if listDivide([1, 2, 3, 4, 5], 1) !=5:
        raise ListDivideException

if __name__ == "__main__":
    
    testListDivide()

