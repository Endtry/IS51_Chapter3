

# grade = 90
# condition = grade >=90
# if not condition:
#     # execute when true
#     print("Your grade is A")
# else:
#     # execute when False
#     print("Your grade is not A")


# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# try:
#     print("1", isinstance(num1, str))
#     print("2", isinstance(num2, str))
#     if isinstance(num1, str) or isinstance(num2, str):
#         print("Data type not allowed! Please specify a numeric value.")
#     else:
#         if num1 > num2:
#             largerVal = num1
#         else:
#             largerVal = num2

#         print("The larger value is " + str(largerVal))
# except:
#     print("Data not allowd!")

# answer = eval(input("How many gallons does a ten-gallon hat hold? "))

# if (.5 <= answer <= 1):
#     print("Good, ", end="")
# else:
#     print("No, ", end="")
# print("it holds about 3/4 of a gallon.")

# def is_greater_than10():
#     answer = eval(input("How many gallons does a ten-gallon hat hold? "))
#     if answer > 10:
#         return True
#     return False

# first_num = eval(input("Enter first number: "))
# second_num = eval(input("Enter second number: "))
# third_num = eval(input("Enter third number: "))

# max = first_num

# if second_num > max:
#     max = second_num
# if third_num > max:
#     max = third_num
# print("The largest of the three number is " + str(max) + ".")

# numbers = [1, 20, 90]

# print(max(numbers))
# numbers = []
# first_num = eval(input("Enter first number: "))
# numbers.append(first_num)
# second_num = eval(input("Enter second number: "))
# numbers.append(second_num)
# third_num = eval(input("Enter third number: "))
# numbers.append(third_num)
# msg = "The largest of the three number is " + str(max(numbers)) + "."
# print(msg)

# color = input("Enter a color (BLUE or RED): ").upper()
# mode = input("Enter a mode (STEADY or FLASHING): ").upper()

# result = ""

# if color == "BLUE":
#     if mode == "STEADY":
#         result = "Clear View"
#     else: # mode is FLASHING
#         result = "Cloud Due"
# else: #Color is RED
#     if mode == "STEADY":
#         result = "Rain Ahead"
#     else: # mode is FLASHING
#         result = "Snow Instead"


# costs = eval(input("Enter total cost: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     result = "break Even."
# else:
#     if costs < revenue:
#         profit = revenue - costs
#         result = "Profit is ${0:,.2f}}".format(profit)
#     else:
#         loss = costs - revenue
#         result = "Loss is ${0:,.2f}".format(loss)
# print(result)

# costs = eval(input("Enter total cost: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     print("break Even.")
# result =  "is ${0:,.2f}}".format(revenue - costs)
# if (revenue - costs) < 0:
#     print("Loss " + result)
# print("Profit " + result)

# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))

# if num1 > num2:
#     print("The larger value is " + str(num1) + ".")
# elif num2 > num1:
#     print("The larger value is " + str(num2) + ".")
# else:
#     print("The two numbers are equal.")

# gpa = eval(input("Enter your GPA: "))

# if gpa >= 3.9:
#     honors = " suma cum laude."
# elif gpa >= 3.6:
#     honors = " magna cum laude."
# elif gpa >= 3.3:
#     honors = " cum laude."
# else:
#     honors = "."
# print("You graduated" + honors)


# num1 = input("enter first number: ")
# num2 = input("enter second number: ")

# if num1.isdigit() and num2.isdigit():
#     print("The sum is " + str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number.")
#     print("The first entry was not a proper number")
# print("the second entry was not a proper number.")
# if 0:
#     print("This will not run...")
# if 7:
#     print("This will run...")
# if []:
#     print("This will not run...")
# if [1, 2, 99]:
#     print("This will run...")
# if True:
#     print("This will run...")
# if False:
#     print("This will not run...")


 