from fct.imgs.imagesearch import imagesearch
from fct.imgs.imagesearch import imagesearch_loop
from fct.imgs.imagesearch import imagesearch_count
import pyautogui
import time
from fct.function_nospot import *
next_fight_pos = []

pyautogui.FAILSAFE = False

#1 on est dans la page arène

while 1>0:


    #2 on clique sur le battle

    if go_to_battle_list() == "1":
        
        while 1>0:

            is_rival = there_is_rival()

            #on est dans la liste de combat, on check la position des 4 ailes.
            time.sleep(5)
            ailes_count_pos = imagesearch_count("./img/next_battle.png",0.9)
            nb_ailes = len(ailes_count_pos)
            
            print("il y a ",nb_ailes," adversaires a fight")
            print(ailes_count_pos)

            if nb_ailes == 0 and is_rival == 1:

                print("On scroll pour regarde plus bas")
                random_sleep()
                a_rival_pos = imagesearch("./img/a_rival.png")
                random_sleep()
                b_rival_pos = imagesearch("./img/b_rival.png")

                if a_rival_pos[0] != 0:

                    pyautogui.moveTo(a_rival_pos[0], a_rival_pos[1])
                    print("on est en haut de la liste rival, on scroll")
                    time.sleep(1)
                    pyautogui.scroll(-100)
                    random_sleep()

                if b_rival_pos[0] != 0:

                    pyautogui.moveTo(b_rival_pos[0], b_rival_pos[1])
                    print("on est en bas de la liste rival, on continue")
                    time.sleep(1)
                    pyautogui.scroll(-120)
                    random_sleep()
                


            if nb_ailes > 0:

                debut_liste = 1
                do_wings(is_rival,ailes_count_pos,debut_liste)







