from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearch_loop
from python_imagesearch.imagesearch import imagesearch_count
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


            #on est dans la liste de combat, on check la position des 4 ailes.
            time.sleep(5)
            ailes_count_pos = imagesearch_count("./img/next_battle.png",0.9)
            nb_ailes = len(ailes_count_pos)
            
            print("il y a ",nb_ailes," adversaires a fight")
            print(ailes_count_pos)

            if nb_ailes > 0:

                x_ailes_count_pos_list = []
                y_ailes_count_pos_list = []

                for (x_ailes_count, y_ailes_count) in ailes_count_pos : 


                    next_fight_pos = [x_ailes_count,y_ailes_count]

                    random_sleep()
                    pyautogui.click(next_fight_pos[0], next_fight_pos[1])
                    random_sleep()
                    #check si monodef

                    solo_def_pos = imagesearch("./img/solo_def.png")
                    random_sleep()
                    solo_def2_pos = imagesearch("./img/solo_def2.png")

                    if solo_def_pos[0] != -1 or solo_def2_pos[0] != -1:

                        print("Il y a un seul mob en def")

                    
                        random_sleep()       

                        start_battle_pos = imagesearch_loop("./img/start_battle.png",1)

                        if start_battle_pos[0] != -1:

                            random_sleep()  
                            pyautogui.click(start_battle_pos[0], start_battle_pos[1])

                            #puis lancer mode auto

                            auto_mode_pos = imagesearch_loop("./img/auto_mode.png",5)

                            if auto_mode_pos[0] != -1:

                                random_sleep()  
                                pyautogui.click(auto_mode_pos[0], auto_mode_pos[1]) 

                                end_fight_pos = imagesearch_loop("./img/end_fight.png",5)

                                if end_fight_pos[0] != -1:

                                    random_sleep()  
                                    pyautogui.click(end_fight_pos[0], end_fight_pos[1])
                                    random_sleep()  

                                    end_fight2_pos = imagesearch_loop("./img/end_fight2.png",1)

                                    if end_fight2_pos[0] != -1:

                                        random_sleep()  
                                        pyautogui.click(end_fight2_pos[0], end_fight2_pos[1])
           
                    else:
                        print("Il semble y avoir une vraie def, def suivante.")
                        exit_menu_fight_pos = imagesearch_loop("./img/exit_menu_fight.png",1)

                        if exit_menu_fight_pos[0] != -1:

                            random_sleep()  
                            pyautogui.click(exit_menu_fight_pos[0], exit_menu_fight_pos[1])
                        else:
                            exit_menu_fight2_pos = imagesearch_loop("./img/exit_menu_fight2.png",1)

                            if exit_menu_fight2_pos[0] != -1:

                                random_sleep()  
                                pyautogui.click(exit_menu_fight2_pos[0], exit_menu_fight2_pos[1]) 
                refresh_list()






