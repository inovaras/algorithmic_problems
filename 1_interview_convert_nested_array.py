# написать функцию, которая выполнит преобразование переданного массива с вложенными массивами в плоский список

def make_lst(l):
    lst = []
    for elem in l:
        if isinstance(elem, list):
            lst.extend(make_lst(elem))
        else:
            lst.append(elem)
    return lst


print(make_lst([[1], 2, 3, [7, 9]]))
print(make_lst([[1], 2, 3, [7, [[9]]]]))
print(make_lst([[1], 2, 3, [7, 9]]))
