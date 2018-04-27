# define class of neterminal
class neterminal:
    def __init__(self, neterm, count_alt, first_pos):  # neterminal, count alternatives, position in list
        self.n = neterm
        self.c = count_alt
        self.f = first_pos

# define class of stack L1
class L1:
    def __init__(self, flag, symbol, number_alt, count_alt):  # flag terminal/neterminal, symbol,
        # number current alternative, count of alternatives
        # if neterminal then number_alt and count_alt don't use
        self.f = flag
        self.s = symbol
        self.n = number_alt
        self.c = count_alt

# define class of stack L2
class L2:
    def __init__(self, flag, symbol):
        self.f = flag
        self.s = symbol

def main():
    # initialzation
    str = "!a+b!"
    LR = "ABBTTMMM"
    RR = ["!B!", "T+B", "T", "M", "M*T", "a", "b", "(B)"]
    m = 4 # number of non-terminals
    sos # q, b, t
    T = "!+*ab()" # set of terminals

    A = neterminal('A', 1, 0)
    B = neterminal('B', 2, 1)
    C = neterminal('C', 2, 3)
    M = neterminal('M', 3, 5)

    S= 'A'  # initial character

if __name__ == '__main__':
    main()