


def solve(arr, n):
    ans = 0

    if len(arr) == 1:
        return 0

    for i in range(1, n):
        if arr[i-1] > arr[i]: 
            # update on if it needs to be
            diff = arr[i-1] - arr[i]
            arr[i] += diff
            ans += diff
    return ans



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    r = solve(arr, n)
    print(r)