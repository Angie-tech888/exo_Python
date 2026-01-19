#question de priorité quesqui arrive quand on l'affiche chacune des instruction suivant l'orsque il executer
print(1/2+1/4)
#Le programme affiche 0.75 car:
#- la division a une priorité plus élevée que l'addition
#- donc 1/2 est calculé en premier, ce qui donne 0.5
#- ensuite, 1/4 est calculé, ce qui donne 0.25
#- enfin, les deux résultats sont additionnés: 0.5 + 0.25 = 0.75
print(1+2*1+4)
#Le programme affiche 7 car:
#- la multiplication a une priorité plus élevée que l'addition
#- donc 2*1 est calculé en premier, ce qui donne 2
#- ensuite, les additions sont effectuées de gauche à droite: 1 + 2
#  ce qui donne 3, puis 3 + 4 = 7
print(64**1/2)
#Le programme affiche 32.0 car:
#- l'exponentiation a une priorité plus élevée que la division
#- donc 64**1 est calculé en premier, ce qui donne 64
#- ensuite, 64 est divisé par 2, ce qui donne 32.
#Ainsi, l'affichage final est "32.0"
#exercice 3 objectif afficher le resultat des operations avec la priorite des operateurs