# Multinomial Coefficient Formula
def uniqueStrs(s: str) -> int:
    dp = {0: 1, 1: 1}
    def fact(n: int) -> int:
        if n in dp:
            return dp[n]

        f = n * fact(n-1)
        dp[n] = f
        return f
    

    m = len(s)
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    ans = fact(m)
    for _, v in freq.items():
        ans = ans / fact(v)

    return int(ans)
    


def removeChr(s: str, ch: str) -> str: 
    for i in range(len(s)):
        if ch == s[i]:
            return s[:i] + s[i+1:]

    return s


# this is core of this code
def perm(s) -> set[str]:
    if len(s) == 1:
        return set(s)

    result = set()
    for ch in s:
        rem_str = removeChr(s, ch)
        perms = perm(rem_str)

        for p in perms:
            result.add(ch + p)

    return result



def solve(s: str) -> list[int, list[str]]:
    # math lol
    total_unique_str = uniqueStrs(s)

    # get all permutations
    # perms have unique as set is used
    perms = perm(s)

    # sort
    sorted_perms = sorted(list(perms))

    return [total_unique_str, sorted_perms]


if __name__ == '__main__':
    s = input()
    count, strs = solve(s)
    print(count)
    for s in strs:
        print(s)
    
