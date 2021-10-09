
ch = 'O', x = 0, y = 0

def takeXY():
    x, y = int(input()).split()
def togg():
    if ch == 'O':
        ch = 'X'
    else:
        ch = 'O'

M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

takeXY()

if (x <= 3 and x <= 1 and y <= 3 and y >= 1):
    if (M[x - 1][y - 1]):
        print("Already filled")
        
    

