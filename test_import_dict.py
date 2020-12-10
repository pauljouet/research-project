#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Paul Jouet
"""

import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.larousse.fr/dictionnaires/francais/%c3%a9tape/31313?q=%c3%a9tape#31245")
soup = BeautifulSoup(req.text, "lxml")

#definitions = soup.find("ul", {"class": "Definitions"})
mot = soup.find("h2", class_= "AdresseDefinition").text
type_mot = soup.find("p", class_= "CatgramDefinition").text

print(mot, type_mot, '\n')
definition_list = []
definitions = soup.find_all("li", class_="DivisionDefinition")
for definition in definitions:
    definition_list.append(definition.text)
for defn in definition_list:
    print(defn, '\n')
    
"""
A faire :
    - formater les string
    - fnct pour avoir accès à tous les mots du dico
    - reflechir à une représentation (graph ?) 
      qui lieraient les mots entre eux via leurs occurrences dans les defs du dico
"""