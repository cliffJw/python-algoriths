def flter(X):
    trgt = sum(X)/2
    return solv(X, trgt, cnt=0)


def solv(X, trgt, cnt=0):
    X.sort(reverse=True)
    X[0]=X[0]/2
    cnt += 1
    if sum(X)>trgt:
        return solv(X, trgt, cnt)
    else:
        return cnt
    return cnt
    print(cnt)
    

#def main():
print(flter([8, 9, 15, 10, 8, 22]))
print(flter([5, 19, 8, 1]))
print(flter([10, 10]))
print(flter([3, 0, 5]))
