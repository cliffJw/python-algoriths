def solution(A):
    count = 0
    while len(set(A) != 1:
        A.sort()
        if A[-1] - 2 >= A[0]:
            A[-1] -= 1
            A[0] += 1
            count += 1
        else:
            A[0] += 1
            count += 1
    return count


print(solution([1, 2, 2, 4]))
print(solution([4, 2, 4, 6]))
print(solution([1, 1, 2, 1]))


