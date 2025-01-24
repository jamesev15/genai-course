numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# for element in numbers:
#     print(element)


# for i in range(len(numbers)):
#     print(numbers[i])

# for element in numbers:
#     if element % 2 == 1:
#         print(element)

while len(numbers) < 13 or len(numbers) > 10:
    numbers.pop()
    print(numbers)