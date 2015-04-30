#!/usr/bin/python
# Dragon curve fractal direction mapper
# F = Forward
# R = Turn right
# L = Turn left
#
# @param int num number of curve order.
def dragoncurv(num):
    command = 'Fa'
    res = []
    for x in range(num):
        for y in command:
            if y == 'a':
                res.append('aRbFR')
            elif y == 'b':
                res.append('LFaLb')
            else:
                res.append(y)
        command = ''.join(res)
        res = []
        
    return command.replace('a','').replace('b','')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Return Dragon curve direction.')
    parser.add_argument('num', metavar='N', type=int, help='Recursive to n.')

    args = parser.parse_args()
    print(dragoncurv(args.num))

