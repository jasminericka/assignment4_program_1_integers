#jasmin ericka a. celebre
#bscpe 1-4


#open the numbers.txt file
with open ("numbers.txt", "r") as my_file:
#read the content of the numbers.txt file
    numbers = my_file.read()
    numbers_list = numbers.split()
#create the even.txt file
with open ("even.txt", "w") as even_file:
#create the odd.txt file
with open ("odd.txt", "w") as odd_file:
