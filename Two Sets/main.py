

#  returns bool, list, list
def solve(n):

    if n%4 != 0 and (n+1)%4 !=0:
        return False, [], []
    

    # build on top of 3' series
    if (n+1)%4 == 0:
        a = [1, 2]
        b = [3]
        start = 3

    # build on top of 4' series
    if n%4 == 0:
        a = [1, 4]
        b = [2, 3]
        start = 4

    end = n
    start = start +1 
    while start < end:
        if start %2:
            a.append(start)
            a.append(end)
        else:
            b.append(start)
            b.append(end)

        start += 1
        end -= 1

    return True, a, b



if __name__ == '__main__':
    n = int(input())
    r, a, b = solve(n)
    if r:
        print("YES")
        print(len(a))
        print(" ".join(map(str, a)))
        print(len(b))
        print(" ".join(map(str, b)))
    else:
        print("NO")