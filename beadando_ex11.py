import random


def beadando1(n):
    player_1 = 0
    player_2 = 0
    kor = 1
    x=0
    while x!=n:
        elso = random.choice(["kő", "papír", "olló"])
        masodik = random.choice(["kő", "papír", "olló"])
        if elso == 'olló' and masodik == 'papír':
            print(str(kor) + '. forduló: ' + elso + ' | ' + masodik + ' 1. játékos nyert')
            player_1+= 1
            kor += 1
            x+=1
        elif elso == 'kő' and masodik == 'olló':
            print(str(kor) + '. forduló: ' + elso + ' | ' + masodik + ' 1. játékos nyert')
            player_1+= 1
            kor += 1
            x += 1
        elif elso == 'papír' and masodik == 'kő':
            print(str(kor) + '. forduló: ' + elso + ' | ' + masodik + ' 1. játékos nyert')
            player_1+= 1
            kor += 1
            x += 1
        elif elso == masodik:
            print(str(kor) + '. forduló: ' + elso + ' | ' + masodik + ' Döntetlen')
            kor+=1

        else:
            print(str(kor) + '. forduló: ' + elso + ' | ' + masodik + ' 2. játékos nyert')
            kor += 1
            x+=1
            player_2+=1




    if player_1< player_2:
        print('2. játékos nyert')
    elif player_1 >p2:
        print('1. játékos nyert')
    else:
        print('döntetlen')

beadando1(8)
