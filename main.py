# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# / # / # EXERCISE # / # / #

# list_student_heights = [151, 145, 179]

# # # Not sure what it did in the code. Apparently it makes up the list in Auditorium.
# student_heights = input(list_student_heights).split(", ")
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_height = 0
# number_of_students = 0

# for height in list_student_heights:
#     total_height += height
#     number_of_students += 1

# average_height = round(total_height / number_of_students)

# print(f"total height = {total_height}\nnumber of students = {number_of_students}\naverage height = {average_height}")

# / # / # / # / # / #

# / # / # EXERCISE # / # / #

# list_student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# # # Not sure what it did in the code. Apparently it makes up the list in Auditorium.
# student_scores = input().split(", ")
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# highest_score = 0

# for score in list_student_scores:
#     if score > highest_score:
#         highest_score = score

# print(f"The highest score in the class is: {highest_score}")

# / # / # / # / # / #

# # # For Loop with Range

# for number in range(1, 11, 2):
#     print(number)

# total = 0

# for number in range(0, 101):
#     total += number

# print(total)

# / # / # EXERCISE # / # / #

# target = int(input("Enter a number between 0 and 1000\n"))
# even_sum = 0

# for n in range(2, target + 1):
#     if n % 2 == 0:
#         even_sum += n

# print(even_sum)

# / # / # / # / # / #

# / # / # EXERCISE # / # / #

# for n in range(1, 101):
#     if n % 15 == 0:
#         print("FizzBuzz")
#     elif n % 5 == 0:
#         print("Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     else:
#         print(n)

# / # / # / # / # / #

# / # / # PROJECT OF DAY 5 # / # / #

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
#nr_symbols = int(input(f"How many symbols would you like?\n"))
#nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
index_letters = len(letters) - 1
random_letter_index = random.randint(0, index_letters)

for n in range(1, nr_letters + 1):
    if n in password_list:
        password_list.append(letters[random_letter_index])
print(password_list)
