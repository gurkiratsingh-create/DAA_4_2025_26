import time

operations = 0
max_depth = 0

def complexRec(n, depth=1):
    global operations, max_depth

    max_depth = max(max_depth, depth)

    if n <= 2:
        return

    p = n
    while p > 0:
        operations += 1
        temp = [0] * n
        for i in range(n):
            operations += 1
            temp[i] = i ^ p
        p >>= 1

    small = [0] * n
    for i in range(n):
        operations += 1
        small[i] = i * i

    small.reverse()
    operations += n

    complexRec(n // 2, depth + 1)
    complexRec(n // 2, depth + 1)
    complexRec(n // 2, depth + 1)
for n in [8, 16, 32, 64]:
    operations = 0
    max_depth = 0

    start = time.time()
    complexRec(n)
    end = time.time()

    print(f"n = {n}")
    print(f"Operations = {operations}")
    print(f"Recursion depth = {max_depth}")
    print(f"Time taken = {(end - start) * 1000:.2f} ms")
    print("-" * 40)

# recursion relation = T(n)=3T(n/2)+nlogn
# O(n^logbase2 3)



