
def print_formatted(number):
    for i in range(1 ,number +1):
        con_octal = oct(i)
        con_Hexa = hex(i)
        con_bin = bin(i)
        print(f"{i}\t{con_octal.replace('0o','')}\t{con_Hexa.replace('0x','')}\t     {con_bin.replace('0b','')}")












