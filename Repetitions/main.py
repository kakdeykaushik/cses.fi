

def solve(s):
    ans = 1

    if len(s) == 1:
        return ans  # 1

    # len is greater then 2
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1

    ans = max(ans, cnt)
    return ans


if __name__ == '__main__':
    s = input()
    r = solve(s)
    print(r)