list = [10, 20, 30, 40]
num = 10


def test(list, num):
        if num in list:
            print(list.index(num))
        else:
            print('Element is not found in the list')


test(list, num)
