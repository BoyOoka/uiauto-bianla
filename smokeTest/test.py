def flattend(nested):
    try:
        try:
            nested + ""
            print(nested)
        except TypeError:
            print("1:",nested)
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flattend(sublist):
                yield element
    except TypeError:
        yield nested

print(list(flattend(["abd",[3,4],[5,6]])))