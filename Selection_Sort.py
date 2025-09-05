

def selection_sort(lst):
    for i in range(6):
        min_pos = i
        for j in range(i, 7):
            if lst[j] < lst[min_pos]:
                min_pos = j

        temp = lst[i]
        lst[i] = lst[min_pos]
        lst[min_pos] = temp
    return lst

lst = [5, 9, 7, 8, 2, 3, 6]

print(selection_sort(lst))







