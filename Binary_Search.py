

pos = -1

def search(lst, n):
    lower = 0
    upper = len(lst) - 1
    while lower <= upper:
        mid = (lower + upper) // 2

        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1
    return False


lst = [5, 4, 9, 7, 8, 6, 3]


if search(lst, 9):
    print("Found", f",Index value is {pos}")
else:
    print("Not Found")




















