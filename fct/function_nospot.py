from .imgs.imagesearch import imagesearch, imagesearch_loop, imagesearch_count
import pyautogui
import time
import random

pyautogui.FAILSAFE = False

def random_sleep():

    a = random.randint(1,500)
    pyautogui.moveTo(10, 10)

    if a < 495:
        rdm_time = random.uniform(0.6014324,2.4244330)
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

def there_is_rival():
        random_sleep()
        rival_pos = imagesearch("./img/rival_needed.png")
        if rival_pos[0] != -1:
            print("Il y a des rivaux a fight.")
            random_sleep()
            pyautogui.click(rival_pos[0],rival_pos[1])
            return 1

        else:

            print('Pas de rival a fight, on continue.')
            time.sleep(2)

            match_up_pos = imagesearch("./img/match_up.png")
            if match_up_pos[0] != -1:
                print("On retourne dans liste arene.")
                random_sleep()
                pyautogui.click(match_up_pos[0],match_up_pos[1])

            return 0

def do_wings(is_rival,ailes_count_pos,debut_liste):

    if 1==1:
        if 1==1:
            if 1==1:

                if debut_liste == 2:
                    ailes_count_pos = imagesearch_count("./img/next_battle.png",0.9)
                    debut_liste = 0

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

                    if is_rival == 1 or solo_def_pos[0] != -1 or solo_def2_pos[0] != -1:

                        print("Il y a un seul mob en def, ou bien rival.")

                    
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
                                    
                                    if is_rival == 0:
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
                
                
                if debut_liste == 1:
                    print('On a anylsé toutes les def, on scroll check la suite de la liste')

                    search_one_wing_pos = imagesearch("./img/next_battle.png")

                    if search_one_wing_pos[0] != -1:

                        pyautogui.moveTo(search_one_wing_pos[0], search_one_wing_pos[1])
                        print("on est en haut de la liste arene, on scroll")
                        time.sleep(1)
                        pyautogui.scroll(-350)
                        random_sleep()
                        debut_liste = 2
                        do_wings(is_rival,ailes_count_pos,debut_liste)


                            
                if is_rival == 0 and debut_liste == 0:
                    refresh_list()
                else :
                    random_sleep()
                    match_up_pos = imagesearch("./img/match_up.png")
                    if match_up_pos[0] != -1:
                        print("On retourne dans liste arene.")
                        random_sleep()
                        pyautogui.click(match_up_pos[0],match_up_pos[1])

def toa_start():

    random_sleep()
    print("recherche de la case ready")
    toa_ready_pos = imagesearch_loop("./img/toa_ready.PNG",5)

    if toa_ready_pos[0] != -1:

        print("On a trouvé la case active du toa, on debute.")
        random_sleep()

        pyautogui.click(toa_ready_pos[0], toa_ready_pos[1])
        return 1

def toa_start_battle():

    random_sleep()
    toa_start_battle_pos = imagesearch_loop("./img/toa_start_battle.PNG",5)

    if toa_start_battle_pos[0] != -1:

        print("On a trouvé le start battle, debut fight.")
        random_sleep()

        pyautogui.click(toa_start_battle_pos[0], toa_start_battle_pos[1])
        random_sleep()
        return 1

def toa_auto_mode():

    random_sleep()
    toa_auto_mode_off_pos = imagesearch("./img/toa_play_auto.PNG")
    #toa_auto_mode_on_pos = imagesearch_loop("./img/toa_auto_ok.PNG",5)

    if toa_auto_mode_off_pos[0] != -1:

        print('le mode auto est en off, turn play')
        random_sleep()

        pyautogui.click(toa_auto_mode_off_pos[0],toa_auto_mode_off_pos[1]) 
        random_sleep()

def toa_next_stage():
    random_sleep()

    toa_next_stage_pos = imagesearch_loop("./img/toa_next_stage.PNG",5)

    if toa_next_stage_pos[0] != -1:

        print('on a trouvé le next stage, on click')
        random_sleep()

        pyautogui.click(toa_next_stage_pos[0],toa_next_stage_pos[1]) 
        random_sleep()

def toa_reward():
    random_sleep()

    toa_reward_pos = imagesearch_loop("./img/toa_reward.PNG",10)

    if toa_reward_pos[0] != -1:

        print('on a trouvé la fin du combat, on click')
        random_sleep()

        pyautogui.click(toa_reward_pos[0],toa_reward_pos[1]) 
        random_sleep()
        pyautogui.click(toa_reward_pos[0],toa_reward_pos[1]) 
        random_sleep()

        toa_reward_ok_pos = imagesearch_loop("./img/toa_ok_reward.PNG",5)

        if toa_reward_ok_pos[0] != -1:

            print('on a trouvé le bouton ok du reward, on click')
            random_sleep()

            pyautogui.click(toa_reward_ok_pos[0],toa_reward_ok_pos[1]) 
            random_sleep()

