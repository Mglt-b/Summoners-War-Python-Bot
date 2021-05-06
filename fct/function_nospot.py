from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearch_loop
import pyautogui
import time
import random

pyautogui.FAILSAFE = False

def random_sleep():

    a = random.randint(1,11)
    pyautogui.moveTo(10, 10)

    if a < 11:
        rdm_time = random.uniform(1.1014324,2.8244330)
        print("sleep",rdm_time,"seconds")
        time.sleep(rdm_time)
    else :
        rdm_time = random.randint(15,90)
        print("Simmulation humain : sleep",rdm_time,"seconds")
        time.sleep(rdm_time)
        
def refresh_list():

    random_sleep()  
    refresh_list_pos = imagesearch_loop("./img/refresh_list.png",1)

    if refresh_list_pos[0] != -1:

        print("on refresh la list")
        random_sleep()  
        pyautogui.click(refresh_list_pos[0], refresh_list_pos[1])
        pyautogui.moveTo(10, 10)
        time.sleep(5)
        

        refresh_list2_pos0 = imagesearch("./img/refresh_list2.png",0.9)
        time.sleep(1)
        print(refresh_list2_pos0)
        refresh_list_load = imagesearch("./img/refresh_list_load.png",0.9)
        time.sleep(2)
        print(refresh_list_load)

        if refresh_list2_pos0[0] != -1 or refresh_list_load[0] != -1:
            
            print("Le refresh est en attente, on passe a l etape suivante")
            refresh_list2_pos = imagesearch_loop("./img/refresh_list2.png",10,0.9)
            print("On a trouvé le bouton pour refresh etape 2")
            random_sleep()  
            pyautogui.click(refresh_list2_pos[0], refresh_list2_pos[1])
            random_sleep()  

            #puis on quitte le menu

            #exit_list_fight_pos = imagesearch_loop("./exit_list_fight.png",1)

            #if exit_list_fight_pos[0] != -1: 
                #random_sleep()  
                #pyautogui.click(exit_list_fight_pos[0], exit_list_fight_pos[1]) 

def go_to_battle_list():
        random_sleep()
        battle_pos = imagesearch("./img/battle.png")
        if battle_pos[0] != -1:
            print("Menu vers liste de combat trouvé, on entre dedans.")
            random_sleep()
            pyautogui.click(battle_pos[0], battle_pos[1])
            return "1"
        else:
            print('Lien vers menu non trouvé. On est dans le mauvais menu ? Placez vous dans le menu arène.')
            time.sleep(2)
            return "0"
