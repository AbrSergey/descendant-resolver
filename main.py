# define class of neterminal
class infNet:
    def __init__(self, nonterm, count_alt, first_pos):  # nonterminal, count alternatives, position in list
        self.n = nonterm
        self.c = count_alt
        self.f = first_pos

# define class of stack L1
class elemL1:
    def __init__(self, flag, symbol, cur_alt = 0, count_alt = 0):  # flag terminal/nonterminal, symbol,
        # number current alternative, count of alternatives
        # if nonterminal then number_alt and count_alt don't use
        self.flag = flag
        self.symbol = symbol
        self.cur_alt = cur_alt
        self.count_alt = count_alt

# define class of stack L2
# class elemL2:
#     def __init__(self, flag, symbol):
#         self.flag = flag
#         self.symbol = symbol

def step1(nonterm):
    print('step1')

    alt = 0
    tmp = RULES[nonterm][alt]
    L1.append(elemL1(0, nonterm, alt, NUMBER_ALT[nonterm] - 1))

    tmp = list(tmp)
    tmp.reverse()
    for i in tmp:
        L2.append(i)

    print(L2)

def step2(term):
    print('step2')

    global cur_pointer
    L1.append(elemL1(1, term))
    cur_pointer += 1

def step3():
    print('step3')

    global SOS
    SOS = 't'

def step3a():
    print('step3a')

    global SOS
    SOS = 'b'

def step4():
    print('step4')

    global SOS
    SOS = 'b'

def step5(term):
    print('step5')

    global cur_pointer
    L2.append(term)
    cur_pointer -= 1
    print(L2)   # for debugging

def step6a(nonterm):
    print('step6a')

    global SOS

    # change data in L1
    alt = nonterm.cur_alt + 1
    assert (alt <= nonterm.count_alt)  # alternative value check
    L1.append(elemL1(0, nonterm.symbol, alt, NUMBER_ALT[nonterm.symbol] - 1))

    # change data in L2
    tmp = RULES[nonterm.symbol][alt]
    tmp = list(tmp)
    tmp.reverse()
    for i in tmp:
        L2.append(i)
    print(L2)   # for debugging

    SOS = 'q'

def step6b():
    print('step6b')

    print ("ERROR: output for the chain is not")

def step6c(nonterm):
    print('step6c')

    if RULES[L1[L1.__len__() - 1].symbol][L1[L1.__len__() - 1].cur_alt] == L2[L2.__len__() - 1]:  # for pop element in L1
        L2.pop()

    L2.append(nonterm.symbol)
    print(L2)   # for debugging

def point2():
    if SOS == 'q':
        data_from_L2 = L2.pop()  # data_from_L2 is terminal or nonterminal
        if data_from_L2 in TERM:    # if data_from_L2 is terminal
            global cur_pointer
            if data_from_L2 == STR[cur_pointer]:
                step2(data_from_L2)
                if cur_pointer == STR.__len__():
                    if L2:
                        step3a()
                        point2()
                        return
                    else:
                        step3()
                        point2()
                        return
                else:
                    if L2:
                        step3a()
                        point2()
                        return
                    else:
                        point2()
                        return
            else:
                step4()
                point2()
                return
        else:   # if data_from_L2 is nonterminal
            step1(data_from_L2)
            point2()
            return

    if SOS == 'b':
        data_from_L1 = L1.pop()
        if data_from_L1.symbol in TERM:
            step5(data_from_L1.symbol)
            point2()
            return
        else:
            if data_from_L1.cur_alt < data_from_L1.count_alt:
                if RULES[data_from_L1.symbol][data_from_L1.cur_alt] == L2[L2.__len__() - 1]:    # for pop element in L1
                    L2.pop()
                step6a(data_from_L1)
                point2()
                return
            else:
                if data_from_L1.symbol == S and data_from_L1.cur_alt == data_from_L1.count_alt:
                    step6b()
                    return
                else:
                    step6c(data_from_L1)
                    point2()
                    return
        pass

    if SOS == 't':
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

    # шаг 1 и шаг 2 сделаны