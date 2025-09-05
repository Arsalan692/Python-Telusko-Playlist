pos = 0

def search(lst, n):
    count = 0
    while count < len(lst):
        if lst[count] == n:
            global pos
            pos = lst.index(n)
            return True
        count += 1

lst = [5, 4, 9, 7, 8, 6, 3]


if search(lst, 4):
    print("Found", f",Index value is {pos}")
else:
    print("Not Found")






