n = int(input("Number: "))
l = len(str(n))
sum = 0
x = n
while (x>0):
    r = x % 10
    sum = sum + int(r**l)
    x = x//10
    l = l - 1
if (sum == n):
    print (n, "is a Disarium Number")
else:
    print (n, "is not a Disarium Number")