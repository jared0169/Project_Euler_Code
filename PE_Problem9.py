# File: PE_Problem9.py
#
# Find the pythagorean triple in which a + b + c = 1000. Find product abc

def find_triples():
    n = 1
    m = 2
    while (True):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
##        print "Triple: ("+str(a)+","+str(b)+","+str(c)+")"
##        print "Sum: "+str(a+b+c)
        while (a+b+c) < 1000:
            m += 1
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
##            print "Triple: ("+str(a)+","+str(b)+","+str(c)+")"
##            print "Sum: "+str(a+b+c)
            if (a + b + c) == 1000:
                print "Triple: ("+str(a)+","+str(b)+","+str(c)+")"
                print "Sum: "+str(a+b+c)
                return a*b*c
        n+=1
        m = n + 1
        #if a + b + c == 1000:
            #break
##        if a + b + c >= 1000:
##            print "Error, exceeded 1000"
##            return
        #i += 1
    return a*b*c


def main():
    product = find_triples()
    print product


if __name__ == "__main__":
    main()
