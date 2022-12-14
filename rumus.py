class Fuzzy:

    def linearturun(a, b, x):
        if x <= a:
            return 1
        elif x >= b:
            return 0
        elif x > a and x < b:
            return (b-x)/(b-a)

    def linearnaik(a, b, x):
        if x <= a:
            return 0
        elif x >= b:
            return 1
        elif x > a and x < b:
            return (x-a)/(b-a)

    def sigmoidturun(a, b, c, x):
        if x <= a:
            return 1
        elif x > a and x <= b:
            return 1-2*((x-a)/(c-a))**2
        elif x > b and x < c:
            return 2*((c-x)/(c-a))**2
        elif x >= c:
            return 0

    def sigmoidNaik(a, b, c, x):
        if x < a:
            return 0
        elif x >= a and x <= b:
            return 2*((x-a)/(c-a))**2
        elif x >= b and x <= c:
            return 1-2*((c-x)/(c-a))**2
        elif x > c:
            return 1

    def Segitiga(a, b, c, x):
        if x <= a or x >= c:
            return 0
        elif x == b:
            return 1
        elif x >= a and x < b:
            return (x-a)/(b-a)
        elif x > b and x <= c:
            return (c-x)/(c-b)

    def trapesium(a, b, c, d, x):
        if x <= a or x >= d:
            return 0
        elif x > a and x < b:
            return (x-a)/(b-a)
        elif x >= b and x <= c:
            return 1
        elif x > c and x < d:
            return (d-x)/(d-c)

    def sigmoid(a, b, c, d, e, x):
        if x <= a:
            return 0
        elif x >= a and x <= b:
            return 2*((x-a)/(c-a))**2
        elif x >= b and x < c:
            return 1-2*((c-x)/(c-a))**2
        elif x == c:
            return 1
        elif x > c and x <= d:
            return 1-2*((x-c)/(e-c))**2
        elif x >= d and x < e:
            return 2*((e-x)/(e-c))**2
        elif x >= e:
            return 0