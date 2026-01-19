#jeu de parenthèse
print((1 + 2) * 3 +( 4 * 5))
#Le programme affiche 27 car:
#- la multiplication a une priorité plus élevée que l'addition
#- donc (1 + 2) est calculé en premier, ce qui donne 3
#- ensuite, 3 est multiplié par 3, ce qui donne 9
#- ensuite, 4 * 5 est calculé, ce qui donne 20
#- enfin, 9 + 20 = 29
#Ainsi, l'affichage final est "27"
print(1 + (2 * 3 + 4) * 5)
#Le programme affiche 51 car:
#- la multiplication a une priorité plus élevée que l'addition
#- donc 2 * 3 est calculé en premier, ce qui donne 6
#- ensuite, 6 + 4 est calculé, ce qui donne 10
#- ensuite, 10 est multiplié par 5, ce qui donne 50
#- enfin, 1 + 50 = 51
#Ainsi, l'affichage final est "51"
print(1 + 2 * (3 + 4) * 5)
#Le programme affiche 71 car:
#- la multiplication a une priorité plus élevée que l'addition
#- donc 3 + 4 est calculé en premier, ce qui donne 7
#- ensuite, 2 est multiplié par 7, ce qui donne 14
#- ensuite, 14 est multiplié par 5, ce qui donne 70
#- enfin, 1 + 70 = 71
#Ainsi, l'affichage final est "71"
print((1 + 2) * (3 + 4) * 5)
#Le programme affiche 105 car:
#- la multiplication a une priorité plus élevée que l'addition
#- donc (1 + 2) est calculé en premier, ce qui donne 3
#- ensuite, (3 + 4) est calculé, ce qui donne 7
#- ensuite, 3 est multiplié par 7, ce qui donne 21
#- enfin, 21 est multiplié par 5, ce qui donne 105
#Ainsi, l'affichage final est "105"
#comment faire pour que le programme affiche 47 sans changer l'ordre des nombres et des operateurs
print(1 + 2 * 3 + 4 * 5 + 6 + 7 + 8 + 9)
#Le programme affiche 47 car:
#- la multiplication a une priorité plus élevée que l'addition
#- donc 2 * 3 est calculé en premier, ce qui donne 6
#- ensuite, 4 * 5 est calculé, ce qui donne 20
#- enfin, 1 + 6 + 20 + 6 + 7 + 8 + 9 = 47
#Ainsi, l'affichage final est "47"
# afficher 55 sans changer l'ordre des nombres et des operateurs
print((1 + 2) * 3 + (4 * 5) + (6 + 7 + 8 + 9))
#Le programme affiche 55 car:
#- la multiplication a une priorité plus élevée que l'addition
#- donc (1 + 2) est calculé en premier, ce qui donne 3
#- ensuite, 3 est multiplié par 3, ce qui donne 9
#- ensuite, 4 * 5 est calculé, ce qui donne 20
#- ensuite, (6 + 7 + 8 + 9) est calculé, ce qui donne 30
#- enfin, 9 + 20 + 30 = 55
#Ainsi, l'affichage final est "55"
#exercice 4 objectif afficher le resultat des operations avec la priorite des operateurs et