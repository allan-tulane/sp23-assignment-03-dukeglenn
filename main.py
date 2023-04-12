# assignment-03

# no other imports needed
from collections import defaultdict
import math

### PARENTHESES MATCHING

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

#### Iterative solution
def parens_match_iterative(mylist):
  result = iterate(parens_update, 0, mylist)
  return result == 0
  pass


def parens_update(current_output, next_input):
    if next_input in '([{':
      return current_output + 1
    if next_input in ')]}':
      return current_output - 1
    else:
      return current_output
    
def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False


#### Scan solution

def parens_match_scan(mylist):
  mappedList = list(map(paren_map, mylist))
  scanMap = scan(lambda x,y: x+y, 0, mappedList)
  scanReduce = reduce(min_f, 0, scanMap[0])
  if scanReduce >= 0 and (scanMap[1] == 0):
    return True
  else:
    return False
  pass

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False

#### Divide and conquer solution

def parens_match_dc(mylist):
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
  if len(mylist) == 0:
    return (0,0)
  elif len(mylist) == 1:
    if mylist[0] == '(':
      return (0,1)
    elif mylist[0] == ')':
      return (1,0)
    else:
      pass
    return (0,0)

  L0, L1 = parens_match_dc_helper(mylist[0:len(mylist)//2])
  R0, R1 = parens_match_dc_helper(mylist[len(mylist)//2:])

  return (L1 - R0, L0 - R1)
    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False

test_parens_match_iterative()
test_parens_match_scan()
test_parens_match_dc()

