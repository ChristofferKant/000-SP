def is_palindroom(word):
    """Versie met reverse"""
    origineel = []
    for letter in word:
        origineel.append(letter)
    omgekeerd = origineel
    omgekeerd.reverse()
    if omgekeerd == origineel:
        return True
    else:
        return False

def is_palindroom2(word):
    origineel = []
    omgedraaid = []
    for letter in word:
        origineel.append(letter)
    for letter in range(len(origineel)-1,-1,-1):
        omgedraaid.append(letter)
    if omgedraaid == origineel:
        return True
    else:
        return False

print(is_palindroom("girafarig"))
print(is_palindroom2("girafarig"))