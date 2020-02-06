"""bron:https://realpython.com/python-zip-function/#understanding-the-python-zip-function"""

string1 = str(input("Geef een string: "))
string2 = str(input("Geef een string: "))


def vind_verschil(string1, string2):
    string3 = list(zip(string1, string2))
    for i, j in string3:
        if i != j:
            print("Het eerste verschil bevindt zich op index", string1.index(i))
            break
        else:
            print("Deze regels zijn hetzelfde")

naam(string1, string2)


