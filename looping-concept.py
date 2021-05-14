# Looping Concept in Python

# Looping -> Doing a work continuously can be called as looping.


# Assignment Section
# 1. Write a program to print the multiplication table of any user input.
# 2. Take the range from user and add them all.


# 1. For Loop -> The for loop is used for iterating over a sequence
# (i.e., either a list, tuple, set, dictionary, string)
# 0 - 100, 1 - 1000, 5- 100, 100-100000

# start, stop


# range -> range(start=0, stop, step=1)
# range(start=0,stop=10,step=1) -> [0-9]


# i - It means iterator
# 0,1,2,3,4,5,6,7,8,9
# for i in range(10):
#     print(i)


# for x in range(100, 200):
#     print(x)

# for x in range(100, 201, 5):
#     print(x)


# Examples: Sum of All Numbers through for loop
# [1,2,4,6,8,10,4]
# total_sum = 35


# average of n number -> (n * (n+1))/2
# n = 10
# (10 * 11)/2 = 110/2 == 55

# total_sum = 55
# for i in range(1, 11):
#     total_sum += i
# print("Sum of all numbers :", total_sum)

# range -> 1-10


# ls = [1, True, 3.76, "John", 5 + 6j]
# for l in ls:
#     print(l)

# str = "banana"
# for i in str:
#     print(i)


# for-else
# for i in range(1,101,2):
#     print(i)
# else:
#     print("For loop ended")


# Nested for loop
# for i in range(0,5):  # 0
#     for j in range(0,5):  # 1
#         print(i, j)




# int->float   5, float(5)
# Type Casting -> Converting a data type into another one is known as type casting.
# x = 10   # 10.0
# y = 10.5   # int(y) -> 10
# print(type(x))
# print(type(y))
#
# x = float(x)
# y = int(y)
# print(type(x))
# print(type(y))

# converting int/float to str

# float/int -> string
# x = 15
# print(type(x))
# x = str(x)
# print(x, type(x))


# converting str to int/float
# Example-1:
# x = '15'
# print(type(x))
# x = int(x)
# print(type(x))

# Example-2:
x = 'cat'
x = int(x)
print(type(x))



# if x < y:
#     print(str(x) + " is less than " + y)

# 2. While loop
