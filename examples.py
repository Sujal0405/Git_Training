
def pythogras_theorm(a,b,c):
    if c**2 == a**2 + b**2:
        return True
    else:
        return False

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if pythogras_theorm(a,b,c):
     print("Yes , the sides satisfy pythagoras theorm")
else:
    print("No, the sides doesn't satisfy pythagoras theorm")