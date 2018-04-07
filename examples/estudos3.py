from collections import Counter
from operator import itemgetter


def count_tops(_list, qtd):
    counter = Counter(_list)
    return counter.most_common(qtd)


def using_itemgetter(dicio, item_to_be_sorted):
    return sorted(dicio, key=itemgetter(item_to_be_sorted))


def main():
    dicio = [{'id': 1, 'item': 5}, {'id': 3, 'item': 4}]
    print(using_itemgetter(dicio, 'item'))
