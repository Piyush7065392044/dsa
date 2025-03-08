
# simple  question 
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


# 1
exp = [2200,2350,2600,2130,2190]
print(" In Feb, how many dollars you spent extra compare to January",exp[0]-exp[1])
#  output will be 150


#2 
print("Find out your total expense in first quarter (first three months) of the year.",exp[0]+exp[1]+exp[2])
# output will be 7150

#3
# print(" Find out if you spent exactly 2000 dollars in any month"+2000 in exp)
# output will be false 

#4 
# we can change value in multiple types using index and bu define list and more option we have to use appens() function 
exp.append(1980)
print("expense it the and of june ",exp)

exp[1]= 0
print(exp)

#5 
print("returned an item that you bought in a month of April and",exp[3]-200)








# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)


heros=['spider man','thor','hulk','iron man','captain america']

# 1

# print(len(heros))


# 2
heros.append("black_panther ")
print(heros)

# 3
heros.remove("black_panther ")
print(heros)
heros.append("hulk")
print(heros)


# 
# replace string always in list not colun 
heros[1:3]= ["doctorstrange"]
print(heros)

# 5
heros.sort()
print(heros)






# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function


max_num = int(input("Enter your number: "))  # Variable name corrected
even_numbers = []  # Logical variable name

for i in range(1, max_num + 1):  # Include 'max_num' in range
    if i % 2 == 0:
        even_numbers.append(i)

print("Even numbers:", even_numbers)  # Print only once after loop




