# creating a while loop

while True:
    print('this is marketing program')
    break

# define function
list1 = [1, 2, 3, 4, 5]


def new_func(numbers):
    result = [(lambda x: x ** 2)(x) for x in list1]
    result1 = [x ** 2 for x in list1]
    result2 = list(map(lambda x: x ** 2, list1))
    print('result', result)
    print('result1', result1)
    print('result2', result2)


if __name__ == '__main__':
    new_func(list1)
