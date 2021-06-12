# 25P
# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have their length counted
# The function will return a list with all int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]
# 25P - (use recursion)
# After reading the above articles try creating a function to calculate the series (1^2)+(2^2)+(3^2)...(n^2)
# The function will receive an int that indicate the number of iterations, or how many times we have (x^2)+
# when resolving try using this logic: 1^2+2^2 is 1^2+(1^2+1^2)^2
# 25P
# Write a function that will calculate factorial of numbers squared.
# For n = 3 the function should calculate (1^2)(2^2)(3^2)
#1
input_list = [1, True, '123', False, 6, ()]

def ordered_ints(list_of_objects: list):
    ints_list = []
    for object in list_of_objects:
        if type(object) == tuple: #count the lenght if it can't be directly converted to int
            object_lenght = len(object)
            ints_list.append(object_lenght)
            continue
        if type(object) == str or True or False: # convert to int if possible
            object = int(object)
            ints_list.append(object)
    ints_list.sort()
    ints_list.reverse()
    return ints_list

result = ordered_ints(input_list)
print(result)
#2
def sum_of_square(n: int):
    if n <= 1 :
        return 1
    else:
        return sum_of_square(n-1) + n ** 2

print(sum_of_square(10))
#3
def factorial_of_squares(n: int):
    factorial = 1
    for number in range(1, n+1):
        factorial = number * 2
    return factorial

print("my result:",factorial_of_squares(3))