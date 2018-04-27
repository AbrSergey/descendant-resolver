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
        self.flag = flag
        self.symbol = symbol
        self.number_alt = number_alt
        self.count_alt = count_alt

# define class of stack L2
class elemL2:
    def __init__(self, flag, symbol):
        self.f = flag
        self.s = symbol

def step1(nonterm):
    alt = 0
    tmp = RULES[nonterm][alt]
    L1.append(elemL1(0, nonterm, alt, NUMBER_ALT[nonterm]))

    tmp = list(tmp)
    tmp.reverse()
    for i in tmp:
        L2.append(i)

    print(L1)
    print(L2)

def step2(term):
    global cur_pointer
    L1.append(elemL1(1, term))
    cur_pointer += 1

def point2():
    if SOS == 'q':
        data_from_L2 = L2.pop()  # data_from_L2 is terminal or nonterminal
        if data_from_L2 in TERM:    # if data_from_L2 is terminal
            global cur_pointer
            if data_from_L2 == STR[cur_pointer]:
                step2(data_from_L2)
                # some steps
            else:
                # step 4
                # sos = 'b'
                # point2
                pass
        else:   # if data_from_L2 is nonterminal
            step1(data_from_L2)
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

    RULES = {'B': ['T+B', 'T'], 'T': ['M', 'M*T'], 'M': ['a', 'b']}
    NUMBER_ALT = {'B': 2, 'T': 2, 'M': 2}
    TERM = {'!', '+', '*', 'a', 'b'}
    NONTERM = {'B', 'T', 'M'}

    STR = 'a+b'
    S = 'B'

    L1 = []
    L2 = []
    L2.append(S)

    SOS = 'q'

    cur_pointer = 0

    #str = "a+b"
    #LR = "BBTTMMM"
    #RR = [["T", "+", "B"], "T", "M", ["M", "*", "T"], "a", "b", ["(", "B", ")"]]
    #m = 3  # number of non-terminals
    #T = "!+*ab()"  # set of terminals

    #B = infNet('B', 2, 1)
    #C = infNet('C', 2, 3)
    #M = infNet('M', 3, 5)

    #N = [B, C, M]

    #S = B  # initial character
    #L1 = []
    #L2 = []

    # START

    #L2.append(S)
    #sos = 'q'  # 'q', 'b', 't'
    #i = j = k = 0
    main()