# ran_file = open("Random_Data.txt", "r")
# read = ran_file.read()
#
#
# data_file = open("new file.txt", "a")
# data_file.write(read)


file_path = "Pi_digits.txt"

with open(file_path) as file_object:
    content = file_object.readlines()

var1 = ""
for i in content:
    var1 += i.strip()

if '69' in var1:
    print("yeah it is")

print(var1)