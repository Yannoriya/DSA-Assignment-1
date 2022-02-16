the_list = []
list_length = int(input("Enter the number of values in your list:")) #Asking the user how many values are in his list
for first_length in range(list_length):
    the_list.append(int(input("Enter the values for the list:"))) #Ask for the values in the user's list7 and add them to our list
print(f"The inserted list is: {the_list}")
checker = []


for an_element in the_list:
    if the_list.count(an_element) % 2 != 0:
        checker.append(True) # marks the list as fullfilling the rule
    else:
        checker.append(False) # marks the list as not fulfilling the rule

if False in checker:
    print("Your list does not fulfill the rule of 'The values should occur in an odd number of times' ")

else:
    print("Your list fulfills the rule of 'The values should occur in an odd number of times' ")
