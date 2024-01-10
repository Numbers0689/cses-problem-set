n = int(input()) 
numstr = [int(x) for x in input().split(" ")]
print(int((n*(n+1)/2)-(sum(numstr))))

# sum of n numbers = n*(n+1)/2