def fibonacci(n):
    lst = [0]
    flag = 0
    while flag < n:
        if lst == [0]:
            lst.append(1)
            flag += 2
        else:
            lst.append(sum(lst))
            del lst[0]
            flag += 1
            print(lst)
    return sum(lst)

print(fibonacci(12))