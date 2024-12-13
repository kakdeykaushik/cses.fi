

def solve(n):

    if n == 1:
        return [1]
    
    if n <= 3:
        return []
    
    if n == 4:
        return [3, 1, 4, 2]
    

    ans = []
    if n % 2 == 0:
        delta = n // 2    
    else:
        delta = 1 + (n // 2)

    for i in range(1, delta+1):
        ans.append(i)
        if i+delta <= n:
            ans.append(i+ delta)

    return ans



if __name__ == '__main__':
    n = int(input())
    r = solve(n)
    if r == []:
        print("NO SOLUTION")
    else:
        print(" ".join(map(str, r)))