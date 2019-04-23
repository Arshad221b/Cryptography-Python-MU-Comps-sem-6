P = int(input("Enter P modulo:"))
G = int(input("Ente primitive root:"))

a = int(input("enter first secret:"))
b = int(input("enter second secret:"))

x = (G**a) % P
y = (G ** b) % P


if (y**a)%P == (x**b)%P:
    print("Alice and Bob can communicate with each other")
    print("their secret key is " + str((x**b)%P))

