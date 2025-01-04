
def match(applicant, aprtment, margin): 
    return abs(applicant - aprtment) <= margin


def solve(applicants: list, aprtments: list, margin):
    applicants.sort()
    aprtments.sort()

    ans = 0
    i = j = 0
    while i < len(applicants) and j < len(aprtments):
        if match(applicants[i], aprtments[j], margin):
           i += 1
           j += 1 
           ans += 1
        else:
            if aprtments[j] < applicants[i]:
                j += 1
            else:
                i += 1

    return ans



if __name__ == '__main__':
    _, _, margin = map(int, input().split())
    applicants = list(map(int, input().split()))
    aprtments = list(map(int, input().split()))
    r = solve(applicants, aprtments, margin)
    print(r)