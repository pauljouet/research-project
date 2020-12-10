#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Paul Jouet
"""

from pylog.logic_variables import unify, unify_pairs, n_Vars, Var
from pylog.sequence_options.linked_list import LinkedList

#def inverse_pylog(L: LinkedList, Inv_L: Var):
    
    #Could be improved using *args in order to switch from 2 arguments to 3
    #yield from inverse_pylog(L, LinkedList([]), Inv_L)
    
def inverse_pylog(L: LinkedList, Acc: LinkedList, Inv_L: Var):
    """
    inverse([],Acc,Acc).
    inverse([H|T],Acc,Result):-inverse(T,[H|Acc],Result).
    """
    # corresponds to inverse([],Acc,Acc).
    # we unify L with [] and Acc with Inv_L
    yield from unify_pairs([
        (L, LinkedList([])),
        (Acc, Inv_L)])
    
    (H, T) = n_Vars(2) # we instantiate the logic variables that still are not
    # here it is H and T (in [H|T])
    for _ in unify(L, LinkedList(H,T)):
        yield from inverse_pylog(T, LinkedList(H,Acc), Inv_L)
        
def inverse_pylog2(L: LinkedList, *args):
    """
    
    inverse(L1,L2):-inverse(L1,[],L2).
    inverse([],Acc,Acc).
    inverse([H|T],Acc,Result):-inverse(T,[H|Acc],Result).

    Parameters
    ----------
    L : LinkedList
        The list to invert.
    *args : Var
        When calling the function, args must be a Var.
        When the function will call itself recursively, args will contain the accumulator as well as the Var


    """
    if len(args) == 1:
        yield from inverse_pylog2(L, LinkedList([]), args[0])
    
    else:
        yield from unify_pairs([
            (L, LinkedList([])),
            (args[0], args[1])])
        
        (H, T) = n_Vars(2)
        for _ in unify(L, LinkedList(H,T)):
            yield from inverse_pylog2(T, LinkedList(H,args[0]), args[1])
  
def test_inv_pylog():
    (X,Y,Z) = n_Vars(3)
    l = [1, 2, X, 4]
    inv_l = [Y, 3, 2, Z]
    (L, Inv_L) = (LinkedList(l), LinkedList(inv_l))
    for _ in inverse_pylog(L, LinkedList([]), Inv_L): # ?- inv([1,2,X,4], [], [Y,3,2,Z])
        print(f'L = {L}\nInv_L = {Inv_L}\n')
        print(f'X = {X}\nY = {Y}\nZ = {Z}')
        print(L[0],L[1],L[2],L[3])
        print()
        
    for _ in inverse_pylog2(L, Inv_L): # ?- inv2([1,2,X,4], [Y,3,2,Z])
        print(f'L = {L}\nInv_L = {Inv_L}\n')
        print(f'X = {X}\nY = {Y}\nZ = {Z}')
        print(L[0],L[1],L[2],L[3])
        
test_inv_pylog()