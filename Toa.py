from fct.imgs.imagesearch import imagesearch,imagesearch_loop,imagesearch_count
import pyautogui
import time
from fct.function_nospot import *

pyautogui.FAILSAFE = False

#on est sur la page toa

if toa_start() == 1:

    #on est dans la liste de battle

    while 1==1:

        toa_start_battle()
        toa_auto_mode()
        toa_reward()
        toa_next_stage()

