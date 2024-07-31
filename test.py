test_cases = int(input())

for _ in range(test_cases):
    inp = input().split()
    n, m, k = int(inp[0]), int(inp[1]), int(inp[2])
    arr = []
    while n > m:
        arr.append(n)
        n -= 1
    if n == m:
        for i in range(1,n+1):
            arr.append(i)
    print(" ".join(str(el) for el in arr))