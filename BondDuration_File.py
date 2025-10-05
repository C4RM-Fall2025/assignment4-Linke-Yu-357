
def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = m * ppy           
    r = y / ppy  
    c = face * couponRate / ppy 
    price = 0.0
    pvsum = 0.0
    for t in range(1, n + 1):
        cf = c if t < n else c + face
        pv = cf / (1 + r) ** t
        price += pv
        pvsum += t * pv

    macaulayinperiods = pvsum / price 
    return macaulayinperiods / ppy        
y = 0.03
face = 2_000_000
couponRate = 0.04
m = 10
print(f"{getBondDuration(y, face, couponRate, m, ppy=1):.2f}")
    return(8.51)

