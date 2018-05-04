# define class of stack L1
class elemL1:
    def __init__(self, flag, symbol, cur_alt = 0, count_alt = 0):  # flag terminal/nonterminal, symbol,
        # number current alternative, count of alternatives
        # if nonterminal then number_alt and count_alt don't use
        self.flag = flag
        self.symbol = symbol
        self.cur_alt = cur_alt
        self.count_alt = count_alt

def step1():
    print('step 1')

    nonterm = L2.pop()
    alt = 0
    tmp = RULES[nonterm][alt]
    L1.append(elemL1(0, nonterm, alt, NUMBER_ALT[nonterm] - 1))

    tmp = list(tmp)
    tmp.reverse()
    for i in tmp:
        L2.append(i)

    print(L2)

def step2():
    print('step 2')

    term = L2.pop()
    global cur_pointer
    L1.append(elemL1(1, term))
    cur_pointer += 1

    print(L2)

def step3():
    print('step 3')

    global SOS
    SOS = 't'

def step3a():
    print('step 3a')

    global SOS
    SOS = 'b'

    print(L2)

def step4():
    print('step 4')

    global SOS
    SOS = 'b'

    print(L2)

def step5(term):
    print('step 5')

    global cur_pointer
    L2.append(term)
    cur_pointer -= 1
    print(L2)

def step6a(nonterm):
    print('step 6a')

    global SOS

    # change data in L1
    alt = nonterm.cur_alt + 1
    assert (alt <= nonterm.count_alt)  # alternative value check
    L1.append(elemL1(0, nonterm.symbol, alt, NUMBER_ALT[nonterm.symbol] - 1))

    # change data in L2
    x = len(RULES[nonterm.symbol][nonterm.cur_alt])
    for i in range (0, x):
        L2.pop()

    tmp = RULES[nonterm.symbol][alt]
    tmp = list(tmp)
    tmp.reverse()
    for i in tmp:
        L2.append(i)
    print(L2)

    SOS = 'q'

def step6b():
    print('step 6b')
    print ("ERROR: output for the chain is not")

def step6c(nonterm):
    print('step 6c')

    x = len(RULES[nonterm.symbol][nonterm.cur_alt])
    for i in range (0, x):
        L2.pop()

    L2.append(nonterm.symbol)
    print(L2)

def point2():
    if SOS == 'q':
        data_from_L2 = L2[L2.__len__() - 1]
        if data_from_L2 in TERM:    # if data_from_L2 is terminal
            global cur_pointer
            if data_from_L2 == STR[cur_pointer]:
                step2()
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
                    if not L2:
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
            step1()
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
        # print string of parse from L1
        output = ''
        for i in L1:
            if i.flag == 0:
                output += str(First_PLACE_in_RULES[i.symbol] + i.cur_alt) + ' '

        print(output)

    else:
        print ("Fatal Error in step1()")

def main():
    point2()

if __name__ == '__main__':

    # initialization

    RULES = {'B': ['T+B', 'T'], 'T': ['M', 'M*T'], 'M': ['a', 'b']}
    NUMBER_ALT = {'B': 2, 'T': 2, 'M': 2}
    TERM = {'!', '+', '*', 'a', 'b'}
    NONTERM = {'B', 'T', 'M'}
    First_PLACE_in_RULES = {'B': 1, 'T': 3, 'M': 5}

    STR = 'a+b'
    S = 'B'

    L1 = []
    L2 = []
    L2.append(S)
    SOS = 'q'
    cur_pointer = 0

    main()