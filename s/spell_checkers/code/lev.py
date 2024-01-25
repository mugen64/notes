#!/usr/bin/env python

def tail(s):
    return s[1:]

def head(s):
    return s[0]

def lev(a, b):
#    print('a: ', a, 'b: ', b)
   if(len(a) == 0):
        return len(b)
   if(len(b) == 0):
      return len(a)
   if(head(a) == head(b)):
        return lev(tail(a), tail(b))
   return 1 + min(lev(tail(a), b), lev(a, tail(b)), lev(tail(a), tail(b)))
#    deletion = lev(tail(a), b)
#    insertion = lev(a, tail(b))
#    substitution = lev(tail(a), tail(b))

#    print('deletion: ', deletion, 'insertion: ', insertion, 'substitution: ', substitution)

#    return 1 + min(deletion, insertion, substitution)
    


def main():
    print(lev('kitten', 'sitting'))
    # print(lev('saturday', 'sunday'))
    # print(lev('saturday', 'saturday'))
    # print(lev('saturday', 'saturdaze'))
    # print(lev('saturday', 'saturdazee'))
    # print(lev('saturday', 'saturdazeee'))
    # print(lev('cat', 'hat'))


main();