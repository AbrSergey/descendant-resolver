

def main():
    str = "!a+b!"
    LR = "ABBTTMMM"
    RR = {"!B!", "T+B", "T", "M", "M*T", "a", "b", "(B)"}
    m = 4 // number of non-terminals

    s = "q" // q, b, t
    L1 = [] // stack
    L2 = [] // stack
    w = str
    steps = ""

    // start
    