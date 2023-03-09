from findpoint import findpoint

# define the function to add two points on the elliptic curve
def point_addition(P, Q,a,p):
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P
    if P == Q:
        # point doubling
        if P[1] == 0:
            return (0, 0)
        m = (3 * P[0] * P[0] + a) * pow(2 * P[1], -1, p) % p
    else:
        # point addition
        if P[0] == Q[0]:
            return (0, 0)
        m = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p) % p
    x = (m * m - P[0] - Q[0]) % p
    y = (m * (P[0] - x) - P[1]) % p
    # print("{},{}".format(x,y))
    return (x, y)

# define the function to double a point on the elliptic curve
def point_doubling(P,a,p):
    if P[1] == 0:
        return (0, 0)
    m = (3 * P[0] * P[0] + a) * pow(2 * P[1], -1, p) % p
    x = (m * m - 2 * P[0]) % p
    y = (m * (P[0] - x) - P[1]) % p
    
    return (x, y)

# define the function to compute the rank of a point on the elliptic curve
def rank_point(P,a,p):
    Q = P
    R = point_doubling(P,a,p)
    i = 0
    while Q != R:
        Q = point_addition(Q, P,a,p)
        R = point_addition(R, P,a,p)
        R = point_addition(R, P,a,p)
        i += 1
        print("Point {}: {}".format(i+1,Q))
    return i + 1 

def get_rank():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    p = int(input("Enter p: "))
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    # define the point P
    P = (x, y)
    if findpoint(a,b,p,[P]) == []:
        print("This point is not on the curve")
        return
    print("y^2 = x^3 + {}x + {} (mod {})".format(a,b,p),"Rank of P=({},{}): ".format(x,y),rank_point(P,a,p))
