stack = []
def pushit():
    stack.append(raw_input(' Enter New string:').strip())

def popit():
    if len (stack) == 0:
        print 'Cannot pop from an empty stack'
    else:
        print 'Remove [','stack.pop()',']'

def viewstack():
    print stack   #Call str() internally

CMDs = {'u': pushit, 'o': popit, 'v':viewstack}

def showmenu():
    pr = """
    p(U) sh
    p(O) p
    (V)view
    (Q)uit

    Enter choice:
    """

    while True:
        while True:
            try:
                choice  = raw_input(pr).strip()[0].lower()

            except (EOFError, KeyboardInterrupt,IndexError):
                choice = 'q'
            print  '\n You picked : [%s]' % choice

            if choice not in 'uovq':
                print 'Involid option, try again'
            else:
                break
        if choice == "q":
            break
        CMDs[choice]()
if __name__ == '__main__':
    showmenu()