"""Bron:https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/"""
def count(x, lst):
    """Telt hoevaak x voorkomt in lst"""
    numbers = []
    for num in lst:
        if num == x:
            numbers.append(x)
    return len(numbers)


def diff(lst):
    """Bepaalt het grootste verschil tussen twee op een volgende getallen"""
    a = max(lst)
    b = min(lst)
    return a-b

def ones(lst):
    """Checkt in een lijst met enen en nullen of het aantal enen groter is"""
    zero = count(0, lst)
    one = count(1, lst)
    numbers = [3, 4, 5, 6, 7, 8, 9]
    if any(x in lst for x in numbers):
        return "Fout invoer lijst"
    elif zero > 12:
        return "Te veel nullen"
    elif zero > one:
        return False
    else:
        return True

getallen = [1, 2, 2, 2, 2, 2, 3, 1, 4, 1, 1]
getallen2 = [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1]
print(count(1, getallen))
print(diff(getallen))
print(ones(getallen2))