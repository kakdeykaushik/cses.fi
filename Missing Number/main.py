


def solve(arr, n):

    required = (n * (n+1)) // 2
    actual = sum(arr)

    return required - actual



if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    r = solve(arr, n)
    print(r)