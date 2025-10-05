

def getBondPrice_Z(face, couponRate, times, yc):
    c = face * couponRate
    price = 0.0
    n = len(times)
    for k, (t, y) in enumerate(zip(times, yc), start=1):
        cf = c if k < n else (c + face)       
        price += cf / (1 + y) ** t        
    return price
yc = [0.010, 0.015, 0.020, 0.025, 0.030]
times = [1, 1.5, 3, 4, 7]
face = 2_000_000
couponRate = 0.04
p = getBondPrice_Z(face, couponRate, times, yc)
print(p)
