
M = 10**9 + 7

def solve(n):
    return (2**n) % M




if __name__ == '__main__':
    n = int(input())
    r = solve(n)
    print(r)