# define class of neterminal
class infNet:
    def __init__(self, nonterm, count_alt, first_pos):  # nonterminal, count alternatives, position in list
        self.n = nonterm
        self.c = count_alt
        self.f = first_pos

# define class of stack L1
class elemL1:
    def __init__(self, flag, symbol, number_alt = 0, count_alt = 0):  # flag terminal/nonterminal, symbol,
        # number current alternative, count of alternatives
        # if nonterminal then number_alt and count_alt don't use
        self.f = flag
        self.s = symbol
        self.n = number_alt
        self.c = count_alt

# define class of stack L2
class elemL2:
    def __init__(self, flag, symbol):
        self.f = flag
        self.s = symbol

def step1(nonterminal):

    alt_cur = 1
    elL1 = elemL1(0, nonterminal, alt_cur)

    for iNonterm in range(0, m):
        if nonterminal == N[iNonterm].n:
            elL1.c = N[iNonterm].c
            break

    L1.append(elL1)
    L2.append(RR[(N[iNonterm].f) + alt_cur - 2]) # replace on RR[]
    print (L2)


def point2():
    if sos == 'q':
        tmp = L2.pop()  # tmp is terminal or nonterminal
        if tmp.n in T:
            if tmp.n == str[i]:
                # step 2
                # another steps
                pass
            else:
                # step 4
                # sos = 'b'
                # point2
                pass
        else:
            step1(tmp.n)
            point2()

    if (sos == 'b'):
        # some steps
        pass

    if (sos == 't'):
        # some steps
        pass

    else:
        print ("Fatal Error in step1()")

def main():
    point2()

if __name__ == '__main__':
    # initialzation
    str = "a+b"
    LR = "BBTTMMM"
    RR = [["T", "+", "B"], "T", "M", ["M", "*", "T"], "a", "b", ["(", "B", ")"]]
    m = 3  # number of non-terminals
    T = "!+*ab()"  # set of terminals

    B = infNet('B', 2, 1)
    C = infNet('C', 2, 3)
    M = infNet('M', 3, 5)

    N = [B, C, M]

    S = B  # initial character
    L1 = []
    L2 = []

    # START

    L2.append(S)
    sos = 'q'  # 'q', 'b', 't'
    i = j = k = 0
    main()