#!/usr/bin/env python3
import time
import sys
#Version du code avec le dico des villes deja dans le .py
DicoVoisins = {'Calais': {'Nancy':534,'Paris':297,'Caen':450},
'Caen': {'Calais':450,'Paris':241,'Rennes':176},
'Brest': {'Rennes':244},
'Rennes': {'Caen':176,'Paris':348,'Nantes ':107,'Brest':244},
'Paris': {'Calais':297,'Caen':297,'Nancy':372,'Dijon':313,'Blois':196,'Rennes':348},
'Nancy': {'Strasbourg':145,'Dijon':201,'Paris':372,'Calais':534},
'Strasbourg': {'Dijon':335,'Nancy':145},
'Nantes': {'Rennes':107,'Limoges':329,'Bordeaux':329},
'Dijon': {'Nancy':201,'Strasbourg':335,'Lyon':192,'Paris':313},
'Limoges': {'Blois':200,'Lyon':389,'Toulouse':313,'Bordeaux':220,'Nantes':329},
'Lyon': {'Dijon':192,'Grenoble':104,'Avignon':216,'Limoges':389},
'Grenoble': {'Avignon':227,'Lyon':104},
'Bordeaux': {'Nantes':329,'Limoges':220,'Toulouse':259},
'Toulouse': {'Limoges':313,'Montpellier':240,'Bordeaux':259},
'Montpellier': {'Avignon':91,'Toulouse':240},
'Avignon': {'Lyon':216,'Grenoble':227,'Marseille':99,'Montpellier':91},
'Marseille': {'Nice':158,'Avignon':99},
'Nice': {'Marseille':158,'Moulin':750},
'Moulin': {'Nice':750,},
'Blois': {'Paris':196,'Limoges':200}}

def executiondebuge(ledico,debut,fin):
    return trajetlepluscourt(ledico,debut,fin,[],{},{},debut)

# trajetlepluscourt nous calcul depuis le dico les valeurs du trajet.
# On utilise pour calculer le trajet le plus court l'algorithme de dijkstra on suppose que tout nos voisins ont une distance infinie et on est obligé de les découvir 1 a 1. Une fois qu'on passe a une autre ville la distance a la ville
# d'avant est égal a 0 d'ou le dist[etape] = 0 (on garde biensur la valeur du trajet complet ) cela nous permet de ne pas nous retrouver a repasser sur la ville d'avant.
#Le trajet changera si le code trouve un candidat a une distance plus courte
#Des qu'on a tout visité on peut en utilisant la récursive une nouvelle étape qui est la plus proche.
#Les liens des vidéos utilisées: https://www.youtube.com/watch?v=JPeCmKFrKio&ab_channel=%C3%80lad%C3%A9couvertedesgraphes
def trajetlepluscourt(ledico,etape,fin,visites,dist,pere,depart):
    if etape == fin:
       return dist[fin], decouvrelesvilles(pere,depart,fin,[])
    if  len(visites) == 0 : dist[etape]=0
    for voisin in ledico[etape]:
        if voisin not in visites:
            dist_voisin = dist.get(voisin,float('inf'))
            candidat_dist = dist[etape] + ledico[etape][voisin]
            if candidat_dist < dist_voisin:
                dist[voisin] = candidat_dist
                pere[voisin] = etape
    visites.append(etape)
    non_visites = dict((s, dist.get(s,float('inf'))) for s in ledico if s not in visites)
    #float(inf) = infini
    noeud_plus_proche = min(non_visites, key = non_visites.get)
    return trajetlepluscourt(ledico,noeud_plus_proche,fin,visites,dist,pere,depart)


#decouvrelesvilles va decouvrir toutes les villes autour de notre ville de depart et va nous donner la liste des autres extremite de la ville pour trouver le chemin le plus court (Fonction récursive)
def decouvrelesvilles(pere,depart,extremite,trajet):
    if extremite == depart:
        return [depart] + trajet
    else:
        return (decouvrelesvilles(pere, depart, pere[extremite], [extremite] + trajet))

#Ici juste nos 2 imputs demandées pour definir le trajet / Pour le site web on aura 2 slide down en choix avec les villes du type : Je cherche a aller de [Choix1] a [Choix2]
choixvillededepart=str(sys.argv[1])
choixvillearrive=str(sys.argv[2])
l3,ResultatFinal = executiondebuge(DicoVoisins,choixvillededepart,choixvillearrive)
print("Le trajet le plus court entre ",choixvillededepart,"et",choixvillearrive,"est",ResultatFinal,"et a une distance de:",l3,"km")
