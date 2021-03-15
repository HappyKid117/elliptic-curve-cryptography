# Y^2 = X^3 + aX + b
# p = modulus
p = 9739
a = 497
b = 1768
O = "O" #point at infinity

def modInverse(a, m):
	for x in range(1, m):
		if (((a%m) * (x%m)) % m == 1):
			return x
	return -1

def div(a, b):
    x = modInverse(b, p)
    if(x==-1):
        print("error")
        return -1
    return a*x

def addPoints(P, Q):
    if(P==O):
        return Q
    if(Q==O):
        return P
    else:
        x1 = P[0]
        y1 = P[1]
        x2 = Q[0]
        y2 = Q[1]
    
    if(x1==x2 and y1==-y2):
        return O
    else:
        if(P==Q):
            l = div((3*x1*x1+a),(2*y1))%p
        else:
            l = div((y2-y1),(x2-x1))%p
    x3 = (l*l - x1 - x2)%p
    y3 = (l*(x1-x3)-y1)%p
    return [x3,y3]

print("X = ",end="")
X = list(map(str, input().split()))
print("Y = ",end="")
Y = list(map(str, input().split()))
if(X[0]==O):
    X = O
else:
    X[0] = int(X[0])
    X[1] = int(X[1])
if(Y[0]==O):
    Y = O
else:
    Y[0] = int(Y[0])
    Y[1] = int(Y[1])
print("X+Y = ", end="")
R = addPoints(X,Y)
print(R)

