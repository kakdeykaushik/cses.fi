

def solve(n):

    res = []
    res.append(n)
    while n != 1:
        if n % 2==0:
            n = n //2
        else:
            n = 3*n +1

        res.append(n)

    return res





if __name__ == '__main__':
    n = int(input())
    r = solve(n)
    print(" ".join(map(str, r)))