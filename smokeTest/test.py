def flattend(nested):
    try:
        for sublist in nested:
            for element in flattend(sublist):
                yield element
                print("yield主",sublist,element)
    except TypeError:
        #print(nested)
        yield nested
        print("typeError:",nested)

nested = [[1,2],[3,4],[5,[6,7]]]

print(list(flattend(nested)))
