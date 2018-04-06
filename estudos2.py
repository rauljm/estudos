
def using_ordered_dict():
    from collections import OrderedDict

    orderdict = OrderedDict()
    orderdict['faa'] = 1
    orderdict['fee'] = 2
    orderdict['fii'] = 3
    orderdict['foo'] = 4
    orderdict['fuu'] = 5

    for key in orderdict:
        print (key, orderdict[key])


def using_zip_with_dicio():
    from collections import defaultdict

    dicio = defaultdict(set)
    dicio['bla'].add(1)
    dicio['ble'].add(2)
    dicio['bli'].add(3)
    dicio['blo'].add(4)

    print (max(zip(dicio.values(), dicio.keys())))


def using_slices():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = slice(2, 6)

    print (a)
    print (lista[a])
