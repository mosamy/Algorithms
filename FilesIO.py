my_list = [i**2 for i in range(1, 11)]

my_file = open("output.txt", "r+")

# Add your code below!

for itm in my_list:
    my_file.write(str(itm))
    my_file.write("\n")
my_file.close()
