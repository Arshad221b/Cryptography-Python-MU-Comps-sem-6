def gcd( a, b):
    while(b != 0):
        a , b = b , a%b
    return a 

def encrypted(e, s , n):
    
    c  =  (int(s)**e) % n
    return c 

def decrypted(c , d, n):
    D = (c ** d)%n
    return D

def main():
    print("Enter the scentence that to be encrypted:")
    s = int(input())
    p = int(input('Enter the first prime no:'))
    q = int(input('Enter the second prime no:'))
    
    n = p * q
    phi = (p-1) * (q- 1)
    E =0
    for e in range(2, q):
        if gcd(e, phi)==1:
            E = e
            break
    print("value of e is:" + str(E))

    
  
    for i in range(1, 9):
        x = (i * phi) + 1
        if x%E == 0:
            d = x/E
            break
    print("The value of D is " + str (d))

    C = encrypted(e , s , n)
    print("encrypted message is "  + str (C))
    D = decrypted(int(C), int(d) , int(n))
    print("decrypted message is " + str(D))


main()