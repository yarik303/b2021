word = input("enter word ")

def huy(blyad):
    blyad = blyad.replace(" ", "").lower()

    return blyad == blyad[::-1]

if huy(word):
    print(f"'{word}' есть")
else:
    print(f"'{word}' нєт")
