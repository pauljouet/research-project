#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Paul Jouet
"""

import requests
import csv
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

# pour accéder à une def du larousse en ligne, nous utiliserons ce string,
# auquel nous ajouteront le mot dont nous cherchons la définition
filename = 'research-project\dataset\liste_mots_freq.csv'
url = "https://www.larousse.fr/dictionnaires/francais/"
liste_mots = []

def ListeMotsCourants():
    """
    Origine de la liste de mots : 'https://eduscol.education.fr/186/liste-de-frequence-lexicale'
    """
    with open(filename, encoding='utf-8', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            liste_mots.append(row)

    dico = []
    for mot in liste_mots:
        dico.append(mot[2])
    
    return dico

#print(ListeMotsCourants())

# problème de cette liste : mauvais encoding résulte des mots mal
# formatés, comme '&2tre' (au lieu de 'être') ou autres

# problème réglé en spécifiant l'encoding lors de l'ouverture du fichier

petit_dico = ['chat', 'chien', 'mammifère', 'animal', 'félin', 'canidé', 'famille']

"""
for mot in petit_dico:
    url_mot = url + mot
    req = requests.get(url_mot)
    soup = BeautifulSoup(req.text, "lxml")

    mot_bs = soup.find("h2", class_= "AdresseDefinition").text
    type_mot = soup.find("p", class_= "CatgramDefinition").text

    print(mot_bs, type_mot, '\n')
    definition_list = []
    definitions = soup.find_all("li", class_="DivisionDefinition")
    for definition in definitions:
        definition_list.append(definition.text)
    for defn in definition_list:
        print(defn, '\n')

# erreur : si le mot n'est pas bien formaté (encoding) 
# l'url ne renverra pas au bon endroit -> donc pas de def
# solution : verifier que la requete renvoie bien la bonne page
"""

def ChercherDefinitions(mot: str):
    url_mot = "https://www.larousse.fr/dictionnaires/francais/" + mot
    req = requests.get(url_mot)
    if(str(req) == '<Response [200]>'):

        soup = BeautifulSoup(req.text, "lxml")

        type_mot = soup.find("p", class_= "CatgramDefinition").text
        definition_list = []
        definitions = soup.find_all("li", class_="DivisionDefinition")
        for definition in definitions:
            definition_list.append(definition.text)

        return [mot, type_mot, definition_list]

    else:
        print(f"Aïe ! Problème d'URL (réponse != 200), le mot : '{mot}' doit être mal formaté, vérifier l'encoding")

for mot in petit_dico:
    print(ChercherDefinitions(mot))

def MotToGraph(mot: str):
    def_mot = ChercherDefinitions(mot)
    definition_token = []
    for definition in def_mot[2]:
        token_mots = word_tokenize(definition)
        definition_token.append(token_mots)

    print(definition_token)

MotToGraph('félin')