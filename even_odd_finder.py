
def even_odd(lst):
    even = []
    odd = []
    for j in lst:
        if j % 2 == 0:
            even.append(j)
        else:
            odd.append(j)
    len_even = len(even)
    len_odd = len(odd)
    print(f"These are the even numbers: {even} ({len_even} even numbers)")
    print(f"These are the odd numbers: {odd} ({len_odd} odd numbers)")


usr_in1 = int(input("How much value you will enter: "))
list1 = []
for i in range(usr_in1):
    usr_in2 = int(input("Enter next value of list: "))
    list1.append(usr_in2)

even_odd(list1)