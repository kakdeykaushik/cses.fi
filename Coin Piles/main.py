# approach
# if both are 0 -> True
# if only 1 is 0 -> false
# if both are equal and multiple of 3 -> True
# else a+b must multiple of 3
#     and big must be less then equal twice of small
#     ex- dry run kr for below example 
#     7 2
#     7 5


# a must be less then be otherwise
# if a < b and b < 2 * a: will not behave expectedly
def canEmpty(a, b):

    if a == b == 0:
        return True

    if a == 0 or b == 0:
        return False
        
    if a == b and a % 3 == 0:
        return True

    if (a+b) % 3 == 0:
        if a < b and b <= 2 * a:
            return True
        else:
            return False

    return False

def solve(arr, _):

    results = []
    for (a, b) in arr:
        results.append(canEmpty(min(a, b), max(a, b)))

    return results



if __name__ == '__main__':
    n = int(input())
    tests = []
    for _ in range(n):
        test = list(map(int, input().split()))
        tests.append(test)
    r = solve(tests, n)
    for v in r:
        print("YES" if v else "NO")