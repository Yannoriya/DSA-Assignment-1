import random
the_list = []
summed_elements = []
# Ask  for the number of values in the list
list_length = int(input("Enter the number of values in your list:"))
for first_length in range(list_length):
    # Ask for the values in the list
    the_list.append(int(input("Enter the value element in the list:")))
print(f"The inserted list is: {the_list}")
the_list.sort(reverse=True)
# pick a random value from the list
random_number = random.randint(1, list_length)
the_sum = 0
# pick random values that will be summed
for iterator in range(random_number):
    the_sum += the_list[iterator]
    summed_elements.append(the_list[iterator])
    # display random value
print(f"The random number used is: {random_number}")
    # display random values to be summed
print(f"The list used in summation is: {summed_elements}")
    # display sum
print(f"The final sum:{the_sum}")
