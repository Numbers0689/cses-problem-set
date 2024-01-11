n=input()
arr=[int(x) for x in input().split(" ")]

def maxx(arr, n):
    if n == 1:
        return 0
    count = prev= 0
    for i in arr:
        if i <= prev :
            prev += 1
            count += prev-i
        else:
            prev = i
    return count

print(maxx(arr, n))      