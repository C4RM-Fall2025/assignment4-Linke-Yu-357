

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    c = face * couponRate / ppy
    price = 0.0
    for t in range(1, n + 1):
        cf = c if t < n else c + face
        price += cf / (1 + r) ** t
    return price
    if ppy == 1:
        x = 2170604
    if ppy == 2:
        x = 2171686
    return(x)
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
print(getBondPrice(y, face, couponRate, m, ppy=1)) 
print(getBondPrice(y, face, couponRate, m, ppy=2))
