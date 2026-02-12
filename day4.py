n = int(input("Enter number of elements: "))
data = [0] * n
for i in range(n):
    value = input("Enter element " + str(i+1) + ": ")
    if value.isdigit():
        data[i] = int(value)
    else:
        data[i] = value
number_list = [0] * n
string_list = [""] * n
num_index = 0
str_index = 0
number_count = 0
string_count = 0
for i in range(n):
    element = data[i]
    if type(element) == int:
        number_list[num_index] = element
        num_index = num_index + 1
        number_count = number_count + 1
    elif type(element) == str:
        if element != "":
            string_list[str_index] = element
            str_index = str_index + 1
            string_count = string_count + 1
print("\nCount Before Removal:")
print("Total Numbers:", number_count)
print("Total Strings:", string_count)
s = input("\nWill you enter name (yes/no): ")
if s == 'yes':
    name = input("Enter the name: ")
else:
    name = "chitti"
    print("using name:",name)
length = len(name)
if length % 2 == 0:
    if num_index > 0:
        for i in range(1, num_index):
            number_list[i-1] = number_list[i]
        num_index = num_index - 1
    if str_index > 0:
        for i in range(1, str_index):
            string_list[i-1] = string_list[i]
        str_index = str_index - 1
else:
    if num_index > 0:
        num_index = num_index - 1
    if str_index > 0:
        str_index = str_index - 1
print("\nNumbers List After Removal:", number_list[:num_index])
print("Strings List After Removal:", string_list[:str_index])
print("\nCount After Removal:")
print("Total Numbers:", num_index)
print("Total Strings:", str_index)