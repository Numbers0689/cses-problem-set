n=int(input("Enter an int: "))

while True:
    if n==1:
        break
    if n%2==0:
        n /= 2
    else:
        n = n*3 + 1

    print(int(n))