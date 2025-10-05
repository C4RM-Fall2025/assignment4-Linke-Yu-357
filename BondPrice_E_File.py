

def getBondPrice_E(face, couponRate, yc):
    c = face * couponRate         
    n = len(yc)                  
    price = 0.0
    for t, y in enumerate(yc, start=1):  
        cf = c if t < n else (c + face) 
        price += cf / (1 + y) ** t      
    return price
yc = [0.010, 0.015, 0.020, 0.025, 0.030]
face = 2000000
couponRate = 0.04

p = getBondPrice_E(face, couponRate, yc)
print(p)       
