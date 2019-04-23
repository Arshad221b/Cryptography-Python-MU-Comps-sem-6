def divide_chunks(l, n): 
      for i in range(0, len(l), n):  
        yield l[i:i + n]


s  = input("Enter the string: ")

p = list(s)



k = input("enter the keyword: ")
k = list(k)

if len(p)%len(k)!= 0:
    for i in range (len(k)-len(p)%len(k)):
        p.append(" ")


n = len(k)
x = list(divide_chunks(p, n)) 


m = sorted(k)
l = []
for i in range(len(m)):
    for j in range(len(k)):
        if m[i]==k[j]:
            l.append(int(j))
print("Original text:")
print(s)
print("cipher text:")

ans = []
for i in range(len(l)):
    for j in range(len(x)):
        ans.append(x[j][l[i]])        

print(''.join(ans))
