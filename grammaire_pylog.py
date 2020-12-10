#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Paul Jouet
"""

from pylog.logic_variables import unify, n_Vars, Var
from pylog.sequence_options.linked_list import LinkedList
#from pylog.sequence_options.sequences import PyTuple

def Phrase_pylog(L0, L):
    """
    phrase(L0,L) :- gnominal(L0,L1), gverbal(L1,L).
    """
    
    L1 = Var()
    
    for _ in Gnominal_pylog(L0,L1):
        yield from Gverbal_pylog(L1,L)
            
def Gnominal_pylog(L0, L):
    """
    gnominal(L0,L) :- det(Genre,L0,L1),
                      nom(Genre,L1,L).
    """
    (L1, Genre) = n_Vars(2)
    
    for _ in Determinant_pylog(Genre, L0, L1):
        yield from Nom_pylog(Genre, L1, L)

def Gverbal_pylog(L0, L):
    """
    gverbal(L0,L) :- verbe(_,L0,L).
    gverbal(L0,L) :- verbe(transitif,L0,L1), gnominal(L1,L).
    """
    yield from Verbe_pylog(Var(), L0, L)
        
    L1 = Var()
    
    for _ in Verbe_pylog("transitif", L0, L1):
        yield from Gnominal_pylog(L1, L)

def Determinant_pylog(Genre: str, L0: LinkedList, L: LinkedList):
    """
    det(masculin,L0,L) :- terminal(le,L0,L).
    det(feminin,L0,L) :- terminal(la,L0,L).
    """
    for _ in unify(Genre, "masculin"):
        yield from Terminal_pylog("le", L0, L)
    for _ in unify(Genre, "feminin"):
        yield from Terminal_pylog("la", L0, L)

def Nom_pylog(Genre, L0, L):
    """
    nom(feminin,L0,L) :- terminal(souris,L0,L).
    nom(masculin,L0,L) :- terminal(chat,L0,L).
    """
    for _ in unify("masculin", Genre):
        yield from Terminal_pylog("chat", L0, L)
    for _ in unify("feminin", Genre):
        yield from Terminal_pylog("souris", L0, L)

def Verbe_pylog(Role: str, L0, L):
    """
    verbe(transitif,L0,L) :- terminal(mange,L0,L).
    verbe(intransitif,L0,L):-terminal(trottine,L0,L).
    """
    for _ in unify("transitif", Role):
        yield from Terminal_pylog("mange", L0, L)
    for _ in unify("intransitif", Role):
        yield from Terminal_pylog("trottine", L0, L)
    for _ in unify("intransitif", Role):
        yield from Terminal_pylog("court", L0, L)

def Terminal_pylog(Mot: str, L0: LinkedList, L: LinkedList):
    """
    terminal(Mot,[Mot|L],L). 
    """
    yield from unify(LinkedList(Mot, L), L0)
    
def test_grammaire():
    X = Var()
    Y = LinkedList([])
    for _ in Nom_pylog("masculin", X, Y):
        print(f'X: {X} Y: {Y}')
        
    for _ in Verbe_pylog("transitif", X, Y):
        print(f'X: {X} Y: {Y}')
    
    for _ in Gnominal_pylog(X, Y):
        print(f'X: {X} Y: {Y}')
        
    for _ in Gverbal_pylog(X, Y):
        print(f'X: {X} Y: {Y}')
        
    print("\n\n-------------------------------------\n\n")
    
    for _ in Phrase_pylog(X, Y):
        print(f'X: {X} Y: {Y}')
        
    R = Var()
    L0 = LinkedList('le', R)
    
    for _ in Phrase_pylog(L0, Y):
        print(f'R: {R} L0: {L0}')
        
    #dans ce cas de figure, ne sont renvoyées que les combinaisons de mots avec la même longueur que la liste L1
    L1 = LinkedList(['le', 'chat', Var()])
    x = []
    y = []
    for _ in Phrase_pylog(L1, Y):
        print(f'L0: {L1}')
        y.append(str(L1))
        for element in L1:
            x.append(str(element))
    print(x, '\n', y)
        
test_grammaire()

"""
Problème à régler : 
    Les variables pylog sont instanciées localement dans un for, 
    comment créer un objet dont les propriétés changent globalement selon des règles 
    qui sont traitées localement ?
Piste :
    Récupérer le string de la variable logique dans la requête ?- pylog
    
Problème à régler :
    Les verbes ou noms sont instanciés grâce à une règle. Comment importer des données
    (par exemple avec BeatifulSoup depuis le site du Larousse) concernant les noms et leur genre
    ou les verbes et leur conjugaison
"""