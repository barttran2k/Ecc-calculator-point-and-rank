# define the function to check if a point is on the elliptic curve
def is_on_curve(x, y,a,b,p):
    return (y * y - x * x * x - a * x - b) % p == 0

def findpoint(a,b,p,points):
    # iterate over all possible x values in the range [0, p]
    for x in range(p):
        # compute the corresponding y value using the equation
        y_sq = (x * x * x + a * x + b) % p
        # check if y^2 is a quadratic residue modulo p
        if pow(y_sq, (p - 1) // 2, p) == 1:
            # compute the two possible values of y
            y1 = pow(y_sq, (p + 1) // 4, p)
            y2 = p - y1
            # check if each of the two possible points is on the curve
            if is_on_curve(x, y1,a,b,p):
                points.append((x, y1))
            if is_on_curve(x, y2,a,b,p):
                points.append((x, y2))
    return points
# print the list of points on the curve
def get_points():
    
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    p = int(input("Enter p: "))
    
    # initialize the list of points on the curve
    points = findpoint(a,b,p,[])
    print("Points on the curve:")
    i = 0
    for point in points:
        i+=1
        print(point)
    print("Total points on the curve y^2 = x^3 + {}x + {} (mod {}): ".format(a,b,p),i+1)