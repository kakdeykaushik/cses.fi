# 564 tarak metha mast episode hai

def solve(arr: list[int]) -> int:

    # approach 1 - n iterations. this gives TLE in cses.fi
    # return len(set(arr))


    # approach 2 - n/2 iterations
    i = 0
    j = len(arr) - 1
    seen = set()
    while i <= j:
        seen.add(arr[i])
        seen.add(arr[j])

        i += 1
        j -= 1

    return len(seen)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    res = solve(arr)
    print(res)
    
