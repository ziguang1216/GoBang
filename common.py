import conf
import sys


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def max_abs(vals):
    """return the item with max absolute value in the list
    """
    if not isinstance(vals, list):
        raise TypeError('input of max_abs must be list')
    if len(vals) < 1:
        raise ValueError('max_abs() arg is an empty sequence')

    ret = vals[0]
    mabs = abs(vals[0])
    for val in vals:
        if abs(val) > mabs:
            ret = val
            mabs = abs(val)
    return ret


def cprint(verbose):
    def _cprint(content):
        if verbose:
            print content
    return _cprint


def dprint(content, new_line=True):
    # debug print
    if conf.debug:
        if new_line:
            print content
        else:
            sys.stdout.write(content)


def pos2h(pos, width):
    i, j = pos
    stri = str(width - i)
    strj = chr(ord('A') + j)
    return strj + stri


def h2pos(hstr, width):
    row = width - int(hstr[1:])
    col = ord(hstr[0].lower()) - ord('a')
    return (row, col)


if __name__ == '__main__':
    print sign(4)
    print sign(0)
    print sign(-4)
    print max_abs([-5, 6])
    print max_abs([-5, 3])
    dprint('h')
    gprint = cprint(True)
    gprint('g')
    gprint = cprint(False)
    gprint('i')
    print pos2h((1, 1), 15)
