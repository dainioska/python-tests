#
def stip(pazm, r1=7.5, r2=9, explain=False ):
    '''return solution
    >>> stip([9, 6, 7])
    0
    >>> stip([9, 6, 7, 10])
    100
    >>> stip([9, 10, 10])
    100

    '''
    vid =sum(pazm) / len(pazm)
    if vid > 7.5:
        return 100
    if vid > 9:
        return 200
    return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)