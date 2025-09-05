user_input = input("Enter your number (5 digits or less): ")

lst1 = list(user_input)
num_of_ones = {"0": "","1": "One","2": "Two","3": "Three","4": "Four","5": "Five","6": "Six","7": "Seven","8": "Eight","9": "Nine"}
num_of_tens = {"2": "Twenty","3": "Thirty","4": "Forty","5": "Fifty","6": "Sixty","7": "Seventy","8": "Eighty","9": "Ninety","0": ""}

if len(lst1) == 1:
    print(num_of_ones[lst1[-1]])
elif len(lst1) == 2:
    print(num_of_tens[lst1[-2]], num_of_ones[lst1[-1]])
elif len(lst1) == 3:
    if lst1[-1] and lst1[-2] == "0":
        print(f"{num_of_ones[lst1[-3]]} Hundred")
    else:
        print(f"{num_of_ones[lst1[-3]]} Hundred and {num_of_tens[lst1[-2]]} {num_of_ones[lst1[-1]]} ")
elif len(lst1) == 4:
    if lst1[-1] and lst1[-2] and lst1[-3] == "0":
        print(f"{num_of_ones[lst1[-4]]} Thousand")
    if lst1[-1] and lst1[-2] == "0":
        print(f"{num_of_ones[lst1[-4]]} Thousand and {num_of_ones[lst1[-3]]} Hundred")
    else:
        print(f"{num_of_ones[lst1[-4]]} Thousand, {num_of_ones[lst1[-3]]} Hundred and {num_of_tens[lst1[-2]]} {num_of_ones[lst1[-1]]}")
