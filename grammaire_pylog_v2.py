#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Paul Jouet
"""

from typing import List
from pylog.sequence_options.linked_list import LinkedList
from pylog.logic_variables import unify
from grammaire_pylog import Terminal_pylog

class Verbe():
    
    def __init__(self, racine: str, transitif: bool = True):
        self.racine = racine
        self.transitif = transitif
        
    def conjuguer(self, sujet: 'Gnominal'):
        pass
    
class Nom():
    
    def __init__(self, racine: str, genre: bool = True, nombre: str = "singulier"):
        self.racine = racine
        if genre:
            self.genre = "masculin"
        else:
            self.genre = "feminin"
        self.nombre = nombre
    
class Determinant():
    
    def __init__(self, racine: str, genre: bool = True, nombre: str = "singulier"):
        self.racine = racine
        if genre:
            self.genre = "masculin"
        else:
            self.genre = "feminin"
        self.nombre = nombre
        
class GVerbal():  
    def __init__(self):
        pass
    
class Gnominal():
    def __init__(self, nom: 'Nom', det: 'Determinant'):
        self.nom = nom
        self.det = det
        
