import math

# numbers with more then 1 five
# 5, 25, 125....

def solve(n):

    ans = 0
    denominator = 5
    while True:
        floor = math.floor(n/denominator)
        if floor == 0:
            break
        
        ans += floor
        denominator *= 5
    return ans



if __name__ == '__main__':
    n = int(input())
    r = solve(n)
    print(r)