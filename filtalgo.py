def flter(X):
    target = sum(X)/2
    count = 0
    while sum(X) > target:
        X.sort()
        X[-1] = X[-1]/2
        count += 1
    return count

#def main():
print(flter([8, 9, 15, 10, 8, 22]))
print(flter([5, 19, 8, 1]))
print(flter([10, 10]))
print(flter([3, 0, 5]))
