from itertools import compress


def gerenate_a_big_list():
    array = []
    for num in range(10000):
        array.append(num)
    return array


def gerenate_a_bigger_list():
    array = []
    for num in range(10000, 20000):
        array.append(num)
    return array


def generator_expression():
    array = gerenate_a_big_list()
    gen_expr = (n for n in array if n % 2 == 0)
    for num in gen_expr:
        print (num)


def generator_list_comprehensions_if_pair():
    array = gerenate_a_big_list()
    return [n for n in array if n % 2 == 0]


def generator_list_comprehensions_treating_pair():
    array = gerenate_a_bigger_list()
    return [n % 2 == 0 for n in array]


def is_number_greater_than_9990(num):
    if num > 9990:
        return True
    return False


def using_filter_with_gererator_expression():
    num_greater_than_9998 = list(filter(is_number_greater_than_9990, generator_list_comprehensions_if_pair()))
    for num in num_greater_than_9998:
        print(num)


def using_compress_operator():
    compressed = list(compress(gerenate_a_bigger_list(), generator_list_comprehensions_treating_pair()))
    print(compressed)
