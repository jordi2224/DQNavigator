def reverse(list):
    print(list)
    s = len (list)
    output = []
    if s <= 1 :
        return list
    elif s == 2:
        return [list[1], list[0]]
    else:
        output.append(list[s-1])
        output.extend(reverse(list[0:s-1]))
        return output



print(reverse([1,2,3,4,5,6,7]))