N, C = 5, 3
A = [1,2,4,8,9]

start = A[0]
end = A[-1] - A[0]
ans = 0

if C == 2:
    ans = end
else:
    while start <= end:
        route = 1
        mid = (start+end) // 2
        current = A[0]
        
        for i in A:
            if current + mid <= i:
                route += 1
                current = i
        
        if route >= C :
            start = mid + 1
            ans = mid
        elif route < C :
            end  = mid - 1

print(ans)