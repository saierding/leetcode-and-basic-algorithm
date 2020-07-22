
t = int(input().strip())
for line in range(t):
    num = list(map(int, input().split()))
    n = num[0]
    nums = num[1:]

    minus = {}
    page_fin = [0]*n
    ans = 1
    for i in range(n):
        if i > 0:
            page_fin[i] = page_fin[i-1]+nums[i]
            fin = (page_fin[i] - 1) // 60
            minus[fin] = 0
        else:
            page_fin[i] = nums[i]
            fin = (page_fin[i] - 1) // 60
            minus[fin] = 0

    for i in range(n):
        fin = (page_fin[i]-1)//60
        minus[fin] += 1
        if minus[fin] > 4:
            ans = 0
    print(ans)