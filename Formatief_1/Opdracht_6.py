def gemiddeld(lst):
    """Berekend het gemiddelde van een lijst"""
    aantal = len(lst)
    totaal = sum(lst)
    uitkomst = totaal / aantal
    return uitkomst


def gemiddelde_lijsten(lists):
    """Berekend het gemiddelde per lijst in een lijst van lijsten"""
    for lst in lists:
        print(sum(lst) / len(lst))


lijst1 = [1, 2, 3, 4, 5, 6, 7]
print(gemiddeld(lijst1))
lijst2 = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
gemiddelde_lijsten(lijst2)