# - variable declaration
num1 = 42
# - variable declaration
num2 = 2.3

#      - Boolean
boolean = True
#   - Strings
string = 'Hello World'

#        - List
#   - initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
#  - access value
print(type(fruit))
#  - access value
print(pizza_toppings[1])
#  - change value
pizza_toppings.append('Mushrooms')
#  - access value
print(person['name'])
#  - change value
person['name'] = 'George'
# - add value
person['eye_color'] = 'blue'
# - access value
print(fruit[2])

# - conditional
#     - if
if num1 > 45:
    print("It's greater")
#     - else
else:
    print("It's lower")
#   - if
if len(string) < 5:
    print("It's a short word!")
#   - else if
elif len(string) > 15:
    print("It's a long word!")
#   - else
else:
    print("Just right!")
# - for loop
#     - start
#     - stop
for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):
    print(x)

#     - start
x = 0
#     - while loop
while x < 5:
    #     - stop
    print(x)
#     - increment
x += 1

# - delete value
pizza_toppings.pop()
# - delete value
pizza_toppings.pop(1)

# access value
print(person)
#   - delete value
person.pop('eye_color')
#   - access value
print(person)

# conditional
for topping in pizza_toppings:
    #   -if
    if topping == 'Pepperoni':
        #   -continue
        continue
    print('After 1st if statement')
    #   -if
    if topping == 'Olives':
        #   - break
        break


# - function
#     - parameter
def print_hello_ten_times():
    # argument
    for num in range(10):
        # return
        print('Hello')


print_hello_ten_times()


# function parameter
def print_hello_x_times(x):
    # argument
    for num in range(x):
        print('Hello')


print_hello_x_times(4)


# function parameter
def print_hello_x_or_ten_times(x=10):
    # argument
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
