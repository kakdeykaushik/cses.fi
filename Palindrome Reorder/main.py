
def preparePalindrome(m):
    center = ""
    ans = ""
    for k, v in m.items():
        if v % 2 ==1:
            # CADDDAC
            # if we do `k` instead of `k * v` output is
            # CADAC
            center = k * v
            continue

        s = k * (v//2)
        ans = s + ans

    return ans + center + ans[::-1] 


def solve(s):
    
    m = {}
    for a in s:
        m[a] = m.get(a, 0) + 1

    odd_count = 0
    for _, value in m.items():
        if value%2 == 1:
            odd_count += 1
            if len(s) %2 == 0 and odd_count > 0:
                return ""
            if len(s) %2 == 1 and odd_count > 1:
                return ""

    return preparePalindrome(m)



if __name__ == '__main__':
    s = input()
    r = solve(s)
    print(r if r !="" else "NO SOLUTION")
    assert r == r[::-1]